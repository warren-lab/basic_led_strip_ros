#!/usr/bin/env python3
import datetime
import time
import sys
import rospy
import numpy as np
from copy import copy
from std_msgs.msg import Header #Need this for SunInfo? 2/9
from std_msgs.msg import String
from  basic_led_strip_proxy import BasicLedStripProxy
from basic_led_strip import BasicLedStrip
from basic_led_strip_ros.msg import StripLEDInfo
from basic_led_strip_ros.msg import SunInfo
from collections.abc import Iterable
#from datetime import datetime

class Random_LED:


    def __init__(self):

        # publishing to the topic sun position
        # and using the message type of sun info
        # additinally the queue size limits the number of queued messages if a subscriber is not recieving fast enough
        self.led_position_pub = rospy.Publisher('sun_position', SunInfo, queue_size=10)
        

        # ROS rate will choose correct amount of time to sleep in order to complete 50ms... so if code takes longer then sleep will be shorter..
        rate = rospy.Rate(5) #Rate we want to publish message in Hz #added 1/20

        # What does use_thread mean?
        self.led_strip = BasicLedStripProxy(use_thread=True) #True? False?

        # initialized the number of leds... 0 to 143...
        self.led_index_list = range(144)

        # the specfic positions of LEDs that will be utilized.
        self.led_positions = [19, 57, 93, 129] 
        
        # also set the iniital led position to zero so that it can be set to a value based on experiment...
        self.led_sun_position = 0

        # Maybe do something different
        np.random.shuffle(self.led_positions)

    def PublishMessage(self):
        # the message that has been referenced can be imported...
        ledmsg = 

    def dark_test(self):
    
    def led_test(self):

    def publish_sun_position(self):
        sun_msg = SunInfo()
        sun_msg.header.stamp = rospy.Time.now()
        sun_msg.sun_position = self.current_sun_position
        rospy.loginfo('Sun Info:' + str(sun_msg)) #shows what is being published as a message
        self.sun_position_pub.publish(sun_msg)
    
    def dark(self):
        self.led_strip.set_all((  0,   0,   0))
        self.current_sun_position = 0
    def sun_sample_no_replacement(self):
        for sun_position in self.sun_positions:
            self.current_sun_position = sun_position
            self.led_strip.set_led(sun_position,(0,128,0))
            yield sun_position

    def run(self):
         while not rospy.is_shutdown():

            """
            This experiment consists of the following procedure:
                1) Dark period                                                      - 30 seconds
                2) Random light from positions [19, 57, 93, 129]                    - 5 minute
                3) Random light from positions [19, 57, 93, 129] w/o replacement    - 5 minute
                4) Dark period                                                      - 30 seconds
            
            """
            sun_sampling = self.sun_sample_no_replacement()
            procedure = [
                            [sun_sampling,300],
                            [sun_sampling,300],
                            [self.dark,30],
                        ]
            self.experiment(procedure)
            sys.exit()

    def experiment(self,procedure):
        for step, timestep in procedure:
            if isinstance(step,Iterable):
                if any(step):
                    next(step)
                else:
                    print("step {} is no longer iterable".format(step.__name__))
            else:
                step()
            self.publish_sun_position()
            print('sun_position: ' + str(self.current_sun_position))
            time.sleep (timestep)

#-------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    rospy.init_node('shuffle_sun')
    node = ShuffleSun()
    node.run()
    rospy.spin()
    # try: 
        
    # except rospy.ROSInterruptException:
    #     pass
