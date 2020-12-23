#!/usr/bin/env python

import rospy
from std_msgs.msg import Int16
from random import seed 
from random import randint
seed(1)


def talker():
    pub = rospy.Publisher('chatter2', Int16, queue_size=10)
    rospy.init_node('talker2', anonymous=True)
    rate = rospy.Rate(0.2) # hz
    while not rospy.is_shutdown():
        num = randint(1,1000)
        rospy.loginfo(num)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        print("I am publisher 2.\n")
        talker()
    except rospy.ROSInterruptException:
        pass
