#!/usr/bin/env python3



import time
from  basic_led_strip_proxy import BasicLedStripProxy
import numpy as np
led_strip = BasicLedStripProxy(use_thread=False)

# led_index_list = list(range(50))
#led_array = np.array([35,69,104,138])


led_array = np.array([32,68,105,138])
#led_array = np.array([143])
#led_array = np.arange(3,144) ### for rotation

#2022/11/20
#LED138->180 degree
#LED105->+90 degree
#LED68->0 degree
#LED32->-90 degree
#LED0-2 covered by LED141-143


# led_strip.set_led(32, (0,128,0))

for i in led_array:
    led_strip.set_led(i,(0,128,0)) 
    #time.sleep(10)
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


