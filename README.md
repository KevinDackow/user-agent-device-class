# user-agent-device-class
Utilities for parsing a User Agent String to get device specific memory and cpu data.


Known Software Dependencies:
https://github.com/ramtin2025/gsmarena-API

With thanks to Facebook for the following chart, used to calculate device year:

Mappings as of this writing (RAM is a ceiling):

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
