# user-agent-device-class
Utilities for parsing a User Agent String to get device specific memory and cpu data.

## Requirements:
deviceatlas.config with your username and password (see deviceatlas.config.example for formatting)

## Usage:
```
./process_ua.sh [-h] [-s] [-m] [-c] [-y] [-u UA] [-o OUTPUT_FILE]

Get information from UA String

optional arguments:
  -h, --help            show this help message and exit
  -s                    Begins a UA parsing REPL
  -m, --memory          Get memory information for device
  -c, --cpu             Get cpu information for a UA string
  -y, --yearclass       Get yearclass for a UA string
  -u UA, --useragentfile UA
                        Provide a file path with user agents to be
                        automatically processed.
  -o OUTPUT_FILE, --outputfile OUTPUT_FILE
                        Output file path for processed data.

```

## Known Software Dependencies:
- [GSMArena API](https://github.com/ramtin2025/gsmarena-API)
- [php-curl](http://php.net/manual/en/book.curl.php)


Given the limitations of User Agent Strings, we assume the most base level memory and processor speed.

## Example I/O: 
```
$ ./process_ua.sh -c -m -y -u examples/simple_file_io.txt
Device Identified: Samsung Galaxy S4 CDMA
RAM:
  2000 MB
CPU:
  Clock speed: 1.9 GHz
  Number of Cores: 4
YearClass:
  2013

```

## Misc.
Thanks to Facebook for the [following chart](https://github.com/facebook/device-year-class/blob/master/README.md), used to calculate device year:

| RAM | condition | Year Class |
|----:|----------:|-----------:|
|768MB| 1 core    | 2009 |
|     | 2+ cores  | 2010 |
|  1GB| <1.3GHz   | 2011 |
|     | 1.3GHz+   | 2012 |
|1.5GB| <1.8GHz   | 2012 |
|     | 1.8GHz+   | 2013 |
|  2GB|           | 2013 |
|  3GB|           | 2014 |
|  5GB|           | 2015 |
| more|           | 2016 |
