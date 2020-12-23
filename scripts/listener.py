#!/usr/bin/env python



import rospy
import message_filters
from std_msgs.msg import Int16

#function that checks if num is Prime
def isPrime(num):
    # prime numbers are greater than 1
    if num > 1:
         # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                return False

            else:
                return True
       
    # if input number is less than
    # or equal to 1, it is not prime
    else:
        return False


#function that checks which num to print
def compare(num1,num2):
    if num1 == num2:
        return num1
    
    big = max(num1,num2)
    small = min(num1,num2)

    if isPrime(small):
        if isPrime(big):
            return big
        else:
            return small
    else:
        return big


#callback function for publisher 1
def callback1(data):

    global pub1_data
    pub1_data = data.data
   

#callback function for publisher 1
def callback2(data):
    
    global pub1_data
    
    data_to_print = compare(pub1_data,data.data)
    rospy.loginfo('I heard %s', data_to_print)
    


def listener():

    rospy.init_node('listener', anonymous=True)

    node1 = rospy.Subscriber('chatter1', Int16, callback1)
    node2= rospy.Subscriber('chatter2', Int16, callback2)
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    print("I am the subscriber.\n")
    listener()
