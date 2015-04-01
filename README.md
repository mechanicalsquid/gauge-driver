# gauge-driver
Code from my wind gauge project

A Raspberry Pi grabs wind data from a weather station website and feeds it to currently two Arduino devices which in turn drive X27.768 stepper motors to display the data on a gauge.

big-gauge and little-gauge is the code for the Arduinos. The python code runs on the Pi.

Both Arduinos are driven by the same serial line. Messages are identified for one or the other by a prefixed character. 'a' and 'b' have been chosen so far. A '!' will cause each gauge to zero itself.

The project writeup can be found: http://hackaday.io/project/345
