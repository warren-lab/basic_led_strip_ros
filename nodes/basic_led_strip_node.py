#!/usr/bin/env python
from __future__ import print_function
import threading
import roslib
import rospy

from basic_led_strip import BasicLedStrip
from basic_led_strip_ros.msg import LEDValue 

class BasicLedStripNode(object):


    def __init__(self):
        rospy.init_node('basic_led_strip')
        self.port = rospy.get_param('port', '/dev/ttyUSB0')
        self.led_strip = BasicLedStrip(self.port)
        self.led_strip.off()
        self.led_value_sub = rospy.Subscriber('set_led_value', LEDValue, self.set_led_value_callback)

    def set_led_value_callback(self,msg):
        self.led_strip.set(msg.led_number, (msg.red, msg.green, msg.blue), mode='exclusive')

    def run(self):
        while not rospy.is_shutdown():
            rospy.sleep(0.1)


# -------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    node = BasicLedStripNode()
    node.run()

