# user-agent-device-class
Utilities for parsing a User Agent String to get device specific memory and cpu data.

Known Software Dependencies:
- [GSMArena API](https://github.com/ramtin2025/gsmarena-API)
- [php-curl](http://php.net/manual/en/book.curl.php)

With thanks to Facebook for the [following chart](https://github.com/facebook/device-year-class/blob/master/README.md), used to calculate device year:

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

Given the limitations of User Agent Strings, we assume the most base level memory and processor speed.

Example:
```
>> Input User Agent: Mozilla/5.0 (Linux; Android 4.3; en-us; SAMSUNG SCH-I545 Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36
Samsung SCH-I545
2013
>> Input User Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_3; en-us; Silk/1.1.0-80) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16 Silk-Accelerated=true
Kindle
2010
>> Input User Agent: BlackBerry9700/5.0.0.862 Profile/MIDP-2.1 Configuration/CLDC-1.1 VendorID/331 UNTRUSTED/1.0 3gpp-gba
BlackBerry 9700
2009
>> Input User Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1
iPhone
2009
```
