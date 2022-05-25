#!/usr/bin/env python3

# Need to improve start up tie



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

# Created a class for the random LED
class LED_Run:

    def init(self):
        # initialization of the node
        rospy.init_node('led_run', anonymous=True)

        ## set the publisher object
        ## # publishing to the topic led_position
        ## # and using the message type of sun info
        ## # additinally the queue size limits the number of 
            # # queued messages if a subscriber is not recieving fast enough
        self.led_pos_pub = rospy.Publisher('led_position',LEDinfo, queue_size = 10)

        # initialized the main control aspect of the package:
        self.led_strip = BasicLedStripProxy(use_thread=True) 

        # initialized the rate... didn't use
        # #  10hz or 5 hz...
        # # Ros rate chooses the correc time to sleep based on how long it takes for it to run code..
        # ### this will help to keep all nodes synchonized if every node is using same rate
        self.rate = rospy.Rate(5)

        # Set Constant Variables:
        ## Set current led to be zero
        self.led_current = 0
        ## color of dark led
        self.dark_led = (0,0,0)
        ## color of led when on
        self.light_led = (0,128,0)
        ## array of all the LED's that will be turned on at random
        self.led_array = np.array([10, 32, 54, 76, 98, 120])
        ## LED Time ON
        self.LED_time = 30 # seconds
        ## Dark Time (TIME LED OFF)
        self.DARK_time = 30 # seconds 

    def main_run(self):

        while not rospy.is_shutdown():
            self.dark_run()
            self.led_run()
            self.dark_run()
            
            sys.exit()
        # This try statement could be reconfigured possibly?

            # try: 
                
            # except ROSInterruptException:
            #     pass

    def publish(self):
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
        led_msg.led_position = self.led_current
        
        # Next will log this information...
        ## basically printing
        rospy.loginfo("LED Information")
        rospy.loginfo(str(led_msg))
        
        # finally publish the result to the message
        ## using the publisher
        ## published to the message LEDinfo
        self.led_pos_pub.publish(led_msg)

    def led_run(self):
        """
        Randomizes the Led that is selected...
        Also makes sure that there is a 1 minute time for each led..
        """
        # randomly selected without replacement... basically just shuffling..
        led_rand_array = np.random.choice(self.led_array,len(self.led_array), replace=False)
        init_val=0
        while init_val <= (len(led_array)-1):
        #for led_num in led_rand_array:  ## loop through the new random values//
        # Looped through random 6 values
            led_num = led_rand_array[init_val]
            self.led_strip.set_led(led_num,self.light_led) # 10, 32, 54, 76, 98, 120
            self.led_current = led_num
            self.publish()
            # added a 5 seconds
            # slept based on rate
            time.sleep(self.LED_time)
            init_val += 1
        self.led_strip.reset_led(self.led_current)
    def dark_run(self):
        """
        publish only once...
        """
        # set the led position to be zero
        self.led_current = 0
        # set all leds to be dark...
        self.led_strip.set_all(self.dark_led)
        time.sleep(self.time_dark)
        self.publish() 
    
if __name__ == '__main__':
    LED_Run.main_run()
    # except rospy.ROSInterruptException:
    #     pass