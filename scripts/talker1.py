#!/usr/bin/env python


import rospy
from std_msgs.msg import Int16
from random import seed 
from random import randint
seed(42)

def talker():
    pub = rospy.Publisher('chatter1', Int16, queue_size=10)
    rospy.init_node('talker1', anonymous=True)
    rate = rospy.Rate(0.2) # hz
    while not rospy.is_shutdown():
        num = randint(1,1000)
        rospy.loginfo(num)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        print("I am publisher 1.\n")
        talker()
    except rospy.ROSInterruptException:
        pass
