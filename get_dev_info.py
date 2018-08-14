"""Gets device info as a JSON and assigns year class"""
import subprocess
import json
from user_agents import parse

def to_megabytes_factor(unit):
    """Gets the factor to turn kb/gb into mb"""
    lower = unit.lower()
    if lower == 'gb':
        return 1000
    if lower == 'kb':
        return 0.001
    return 1

def get_dev_data(device, output_file):
    """Gets info for a device, returned as:
    (title, data) """
    args = ["php", "get_dev_json.php", output_file]
    args.extend(device.split(" "))
    subprocess.run(args)
    with open(output_file +  '.json') as f:
        phone = json.load(f)
    subprocess.run(['rm', '-rf', output_file + '.json'])
    return (phone['title'], phone['data'])

def get_memory(data):
    """Given data from GSMArena, get memory info, if it exists.
    data is returned in get_dev_data[1]"""
    try:
        memory_info = data['memory']
        try:
            return memory_info['internal']
        except (KeyError, TypeError):
            return memory_info
    except (KeyError, TypeError):
        return None

def get_ram(mem_info):
    """Gets RAM in MBs from the given memory info
    (mem_info is outputt by get_memory)"""
    if mem_info is None:
        return None
    try:
        info = mem_info.split(',')
        all_rams = list()
        for substr in info:
            if "RAM" in substr:
                #<N> <units> RAM
                subs = list(filter(lambda x: x != '', substr.split(' ')))
                all_rams.append(int(subs[0]) * to_megabytes_factor(subs[1]))
        try:
            return min(all_rams)
        except ValueError:
            return None
    except (KeyError, TypeError):
        return None

def get_cpu(data):
    """Given data from GSMArena, get processor speed info, if it exists.
    data is returned in get_dev_data[1]"""
    try:
        cpu_info = data['platform']
        try:
            return cpu_info['cpu']
        except (KeyError, TypeError):
            return cpu_info
    except (KeyError, TypeError):
        return None

def get_clock_speed(cpu):
    """Gets clockspeed in GHz from given cpu data (returned by get_cpu)"""
    try:
        splitt = cpu.split(' ') #Quad-core ... GHz)
        hz_index = -1
        counter = 0
        for stri in splitt:
            lowered = stri.lower()
            if 'ghz' in lowered or 'mhz' in lowered:
                hz_index = counter
                break
            counter += 1
        if hz_index < 0:
            return None
        if splitt[hz_index].lower() == 'mhz':
            return float(splitt[hz_index -1]) * 0.001
        return float(splitt[hz_index - 1])
    except Exception: #a bit janky so catch all for now
        return None

def get_cores(cpu):
    """Gets number of cores from given cpu data (returned by get_cpu)"""
    try:
        splitt = cpu.split(' ') #QuadCore ... x GHz
        for ln in splitt:
            lowered = ln.lower()
            if 'core' in lowered:
                if 'dual' in lowered:
                    return 2
                if 'quad' in lowered:
                    return 4
                if 'hexa' in lowered:
                    return 6
                if 'octa' in lowered or 'octo' in lowered:
                    return 8
        return None
    except Exception: #this is kind of janky, so we have to catch all
        return None

def get_release_date(data):
    """gets device release date"""
    try:
        launch = data['launch']
        splt = launch.split(' ')
        return int(float(splt[0]))
    except (KeyError, TypeError):
        return None

def get_year_class(data):
    """Returns the device yearclass of the given device
    as per Facebook's Device-Year-Class chart:
    https://github.com/facebook/device-year-class
    Attempts to base on clock speed and RAM, if one doesn't exist, uses the other,
    if neither exists, uses release date"""
    ram = get_ram(get_memory(data))
    cpu = get_cpu(data)
    clock_speed = get_clock_speed(cpu)
    num_cores = get_cores(cpu)
    #all data is available
    if ram is not None and clock_speed is not None:
        if ram <= 768:
            if num_cores is None or num_cores == 1:
                return 2009
            return 2010
        if ram <= 1000:
            if clock_speed < 1.3:
                return 2011
            return 2012
        if ram <= 1500:
            if clock_speed < 1.8:
                return 2012
            return 2013
        if ram <= 2000:
            return 2013
        if ram <= 3000:
            return 2014
        if ram <= 5000:
            return 2015
        return 2016
    #only ram is defined
    if ram is not None:
        if ram <= 768:
            if num_cores is None or num_cores == 1:
                return 2009
            return 2010
        if ram <= 1000:
            return 2011
        if ram <= 1500:
            return 2012
        if ram <= 2000:
            return 2013
        if ram <= 3000:
            return 2014
        if ram <= 5000:
            return 2015
        return 2016
    #only clock speed is defined
    if clock_speed is not None:
        if clock_speed < 1.3:
            if num_cores is None or num_cores < 2:
                return 2009
            return 2010
        if clock_speed < 1.8:
            return 2012
        return 2013
    #none are defined, so we use when it was released
    return get_release_date(data)

def ua_to_device_name(user_a):
    """gets the device name from the user agent string, as best as it can"""
    user_agent = parse(user_a)
    uastr = str(user_agent).split(' / ') #e.g. iPhone / iOS 5.1 / Mobile Safari
    return uastr[0]
