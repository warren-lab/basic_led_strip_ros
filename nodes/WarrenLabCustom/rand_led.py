#!/usr/bin/env python3

from datetime import datetime
import time
import sys
import rospy
import numpy as np
from copy import copy
from std_msgs.msg import Header #Need this for SunInfo? 2/9
from std_msgs.msg import String
from  basic_led_strip_proxy import BasicLedStripProxy
from basic_led_strip import BasicLedStrip
from basic_led_strip_ros.msg import LEDinfo
#from basic_led_strip_ros.msg import SunInfo
#from collections.abc import Iterable
def main_run():
    # publishing to the topic led_position
    # and using the message type of sun info
    # additinally the queue size limits the number of 
        # # queued messages if a subscriber is not recieving fast enough
    led_pos_pub = rospy.Publisher('led_position',LEDinfo, queue_size = 10)

    # initialized the main control aspect of the package:
    led_strip = BasicLedStripProxy(use_thread=True) 

    # next the node (function) was initialized..
    rospy.init_node('led_run', anonymous=True)

    # then the rate was established to be
    #  10hz or 5 hz...
    ## Ros rate chooses the correc time to sleep based on how long it takes for it to run code..
    #### this will help to keep all nodes synchonized if every node is using same rate
    rate = rospy.Rate(1)



    while not rospy.is_shutdown():
        led_run(led_strip,led_pos_pub, rate)
        
        
        sys.exit()
    # This try statement could be reconfigured possibly?

        # try: 
            
        # except ROSInterruptException:
        #     pass

def publish(led, pub):
    """
    This function deals with 
    publishing to the message 

    Message has the following that needs to be published..
    - header -> time stamp
    - led light position -> led_position

    """    
    # first iniitalized the message
    led_msg = LEDinfo()

    # after message initialization then needed to get the parameters that the message requires
    ## The current time for the header time stamp
    current_time = datetime.now().strftime("%Y%M%D_%H%M%S")
    led_msg.header.stamp = current_time
    ## The position of the LED as in the number of the LED
    led_msg.led_position = led
    
    # Next will log this information...
    ## basically printing
    rospy.loginfo("LED Information")
    rospy.loginfo(str(led_msg))
    
    # finally publish the result:
    pub.publish(led_msg)

def led_run(led_strip,pub, rate):
    """
    Randomizes the Led that is selected...
    Also makes sure that there is a 1 minute time for each led..
    """
    dict_led = {
        "led_array": np.array([10, 32, 54, 76, 98, 120]),
        'times':np.array([30,150]),
        'led_color':np.array([0,128])
    }
    led_array = dict_led['led_array']
    # randomly selected without replacement... basically just shuffling..
    led_rand_array = np.random.choice(led_array,len(led_array), replace=False)
    led = 0
    init_val=0
    while init_val <= (len(led_array)-1):
    #for led_num in led_rand_array:  ## loop through the new random values//
        led_num = led_rand_array[init_val]
        led_strip.set_led(led_num,(0,128,0)) # 10, 32, 54, 76, 98, 120
        led = led_num
        publish(led, pub)
        # added a 5 seconds
        # slept based on rate
        rate.sleep()
        init_val += 1
    led_strip.reset_led(led)
    

if __name__ == '__main__':
    main_run()
    # except rospy.ROSInterruptException:
    #     pass