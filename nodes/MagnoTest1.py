#!/usr/bin/env python3

# there are 144 leds numbver from 0 to 143 

import time
import numpy as np
from basic_led_strip_proxy import BasicLedStripProxy

led_strip = BasicLedStripProxy(use_thread=False)


## Led Strip 10 seems to be first one on the farthest most end
# from 0 to 9 those are unused (10 Leds not in use)
## The other end seems to end around 120
# from 120 there are 24 unused Leds



####################################

##                TEST 1            ###

######################################### 
#led_strip.set_led(10,(100,0,0)) # technially number 11

#led_strip.set_led(120,(100,0,0)) # technically 121


#time.sleep(10)

#led_strip.reset_led(10)
#led_strip.reset_led(120)


############################################

##       TEST 2: Iterate Through 5 LEDs ###
####################################################





# So the number of leds inbetween the two outer points is 110..
### so we could have it go every 22 leds... this means there are 5 stages...




# we can just start at 10 and then add 22 every time...

## initialized starting led

led_num_on = 10

increase_val = 22

num_led = 6  # 6 led will be on

it_val = 0

while it_val in np.arange(num_led): # loops through 6 times...
	
	## first would reference the led_num_on... and then call that and the we will set it to be on
	led_strip.set_led(led_num_on,(100,0,0)) # 10, 32, 54, 76, 98, 120


	# added a 5 seconds
	time.sleep(5)


	# after iteration go to the next one..
	## add 22...
	led_num_on += 22
	## add 1
	print(it_val) 
	it_val += 1

led_strip.reset_led(led_num_on)



