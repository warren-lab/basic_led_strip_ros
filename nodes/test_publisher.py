#!/usr/bin/env python
from __future__ import print_function
import threading
import roslib
import rospy
import std_msgs.msg
import random

from basic_led_strip_ros.msg import LEDValue 

class LedTestPubNode(object):


    def __init__(self):
        rospy.init_node('led_value_test_pub')
        self.led_value_pub = rospy.Publisher('set_led_value', LEDValue, queue_size=10)
        self.num_led = 144 # Temporary get from service later


    def run(self):
        led_pos = 0
        red, green, blue = self.get_random_color()
        while not rospy.is_shutdown():
            header = std_msgs.msg.Header()
            header.stamp = rospy.Time.now()
            self.led_value_pub.publish(LEDValue(header,led_pos,red,green,blue))
            rospy.sleep(0.02)
            led_pos += 1
            if led_pos >= self.num_led-1:
                led_pos = 0
                red, green, blue = self.get_random_color()

    def get_random_color(self):
        r,g,b = 0,0,0
        i = random.randint(0,3)
        if i%3 == 0:
            r = random.randint(0,100)
            g = random.randint(0,100)
        elif i%3 == 1:
            r = random.randint(0,100)
            b = random.randint(0,100)
        else:
            g = random.randint(0,100)
            b = random.randint(0,100)
        return r,g,b

# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    node = LedTestPubNode()
    node.run()
