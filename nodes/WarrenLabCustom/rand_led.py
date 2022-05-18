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
#led_position = 0
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
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        led_run(led_strip,led_pos_pub, rate)



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
    led_list = [10, 32, 54, 76, 98, 120]

    led_num_on = 0

    increase_val = 22

    num_led = 6  # 6 led will be on

    it_val = 0

    for led_num_on in np.choice(led_list, replace = False): ## loop through 6 times..
        
        ## first would reference the led_num_on... and then call that and the we will set it to be on
        led_strip.set_led(led_num_on,(100,0,0)) # 10, 32, 54, 76, 98, 120
        led = led_num_on
        publish(led, pub)

        # added a 5 seconds
        # slept based on rate
        rate.sleep()

        # after iteration go to the next one..
        ## add 22...
        led_num_on += increase_val
        ## add 1
        print(it_val) 
        it_val += 1

    led_strip.reset_led(led_num_on)




if __name__ == '__main__':
    try:
        main_run()
    except rospy.ROSInterruptException:
        pass