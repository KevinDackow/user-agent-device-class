# user-agent-device-class
Utilities for parsing a User Agent String to get device specific memory and cpu data.

Known Software Dependencies:
[GSMArena API](https://github.com/ramtin2025/gsmarena-API)
[php-curl](http://php.net/manual/en/book.curl.php)

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
