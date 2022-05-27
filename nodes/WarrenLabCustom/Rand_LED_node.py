#!/usr/bin/env python3

# Experiment:
## Length of Time: 5 min
#### Dark Time: 2, 30 sec periods
#### LED Time: 4, 1 min periods

# will publish data on the led position to the topic of 'led_position'

# LED control shuts off the magno tether...
## if this ROS node shuts down need to commuynicate with the other node to stop,

# Number of LEDS: 144
# Values of LEDS range from 0 to 143


# NEED to Save this node with the TWYG

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
    def __init__(self):
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
        self.dark_led = 0 #(0,0,0)
        ## color of led when on
        self.light_led = 128 #(0,128,0)
        ## array of all the LED's that will be turned on at random
        #self.led_array = np.array([10, 32, 54, 76, 98, 120])
        ## array of the four LED's
        self.led_array = np.array([0,36,72,108])
        ## LED Time ON
        self.time_LED = 60 # seconds
        ## Dark Time (TIME LED OFF)
        self.time_dark = 30 # seconds 

    def main_run(self):

        while not rospy.is_shutdown():
            rospy.sleep(1)
            print("Starting Experiment..."+"\n")
            self.dark_run()
            self.led_run()
            self.dark_run()
            
            sys.exit()
        # This try statement could be reconfigured possibly?

            # try: 
                
            # except ROSInterruptException:
            #     pass

    def publish_msg(self):
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
        #led_msg.header.stamp = current_time
        led_msg.header.stamp=rospy.Time.now()
        ## The position of the LED as in the number of the LED
        led_msg.led_position = self.led_current
        
        # Next will log this information...
        ## basically printing
        #rospy.logwarn('publishing message')
        
        rospy.loginfo("\n"+"LED Information:")
        print(str(led_msg))
        
        # finally publish the result to the message
        ## using the publisher
        ## published to the message LEDinfo
        self.led_pos_pub.publish(led_msg)
        rospy.logwarn('message published')

    def led_run(self):
        """
        Randomizes the Led that is selected...
        Also makes sure that there is a 1 minute time for each led..
        """
        print("\n"+"Random LED:")
        # randomly selected without replacement... basically just shuffling..
        led_rand_array = np.random.choice(self.led_array,len(self.led_array), replace=False)
        init_val=0
        while init_val <= (len(self.led_array)-1):
        #for led_num in led_rand_array:  ## loop through the new random values//
        # Looped through random 6 values
            led_num = led_rand_array[init_val]
            self.led_strip.set_led(led_num,(0,128,0)) 
            self.led_current = led_num
            led_ang = (led_num/144)*360 # degrees
            print("\n"+"Current LED Angle:"+str(led_ang))
            self.publish_msg()
            # added a 5 seconds
            # slept based on rate
            time.sleep(self.time_LED)
            init_val += 1
        self.led_strip.reset_led(self.led_current)
    def dark_run(self):
        """
        publish only once...
        """
        print("Dark Data:"+"\n")
        # set the led position to be dark, and that being a positive value...
        ## Errors will occur if it is negative.
        ## Additionally the value of 150 was set such that it is not within the scope of the LED 
        self.led_current = 150
        # set all leds to be dark...
        self.led_strip.set_all((0,0,0))
        self.publish_msg() 
        time.sleep(self.time_dark)

    def get_current_led(self):
        """
        Method that returns the current led_number
        """
        return self.led_current
    def set_led_off(self,led_num):
        """
        When the experiment is ended early all LEDs need to be turned off

        Takes input of the current led and turns that off.
        """
        self.led_strip.reset_led(led_num)
        
    
if __name__ == '__main__':
    led_node = LED_Run()
    try :
        led_node.main_run()
    except rospy.ROSInterruptException:
        # Resets the current LED...
        sys.exit()
        # led_reset = LED_Run.get_current_led()
        # LED_Run.set_led_off(led_reset)
    # except rospy.ROSInterruptException:
    #     pass

    # INJECT A ROS RUN FUNCTION THAT WILL BE FOR JUST THE led and dark functions
    ## Then maybe do a try with that?