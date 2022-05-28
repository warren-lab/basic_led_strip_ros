#!/usr/bin/env python3



import time
from  basic_led_strip_proxy import BasicLedStripProxy
import numpy as np
led_strip = BasicLedStripProxy(use_thread=False)

# led_index_list = list(range(50))
led_array = np.array([31,67,106,139])
for i in led_array:
    led_strip.set_led(i,(0,128,0)) 
    time.sleep(2)
# for i in led_index_list:
#     print(i)
#     led_strip.set_led(i,(100,0,0))
#     time.sleep(0.1)


# for i in reversed(led_index_list):
#     print(i)
#     led_strip.set_led(i,(0,0,100))
#     time.sleep(0.1)


# led_strip.set_all((100, 100,   0))
# time.sleep(1.0)
# led_strip.set_all((  0, 100, 100))
# time.sleep(1.0)
# led_strip.set_all((100,   0, 100))
# time.sleep(1.0)
# led_strip.set_all((100,   0, 100))
# time.sleep(1.0)
# led_strip.set_all((  0,   0,   0))




