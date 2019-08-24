#!/usr/bin/env python3
from custom_filter import AKF
import numpy as np
import sys
import rospy
from std_msgs.msg import Float32MultiArray
from robotiq_force_torque_sensor.msg import ft_sensor
# from nav_msgs.msg import Odometry
class FileterFactory(object):
    """ Return the filter you want """
    def __init__(self, input):
        self.input = input
    def __call__(self, filter_name):
        dict_filter = {
            'AKF': lambda: AKF.AKF(self.input, input_num=len(self.input))
            }.get(filter_name, lambda: print('Unexist filter'))
        return dict_filter()

def readPos(path):
    """ read the pos file
    args:
        path: the path of the pos file
    """
    pos = []
    with open(path, 'r') as fd:
        for i in fd:
            i = i.strip('\n')
            i = i.split(',')
            i = np.asarray(i)
            i = i.astype(float)
            pos.append(i)
    return pos

class RosCom(object):
    """ Ros comminucate class """
    def __init__(self):
        self.__subscribe()
        self.__publisher()
    def __subscribe(self):
        """ all subscriber declare here """
        # rospy.Subscriber("odom", Odometry, self.__subOdom)
        rospy.Subscriber("robotiq_force_torque_sensor", ft_sensor, self.__subOdom)
    def __publisher(self):
        """ all publisher declare here """
    def __subOdom(self, msg):
        ft_Fx = msg.Fx
        ft_Fy = msg.Fy
        ft_Fz = msg.Fz
        ft_Mx = msg.Mx
        ft_My = msg.My
        ft_Mz = msg.Mz
        # odom_x = msg.pose.pose.position.y
        # odom_y = msg.pose.pose.position.y
        self.__ft = [ft_Fx, ft_Fy, ft_Fz, ft_Mx, ft_My, ft_Mz]
        # self.__odom = [odom_x, odom_y]
    def getOdom(self):
        return self.__ft
        # return self.__odom

if __name__ == '__main__':
    rospy.init_node('filter', anonymous=True)
    ros_node = RosCom()
    # rospy.wait_for_message('odom', Odometry)
    rospy.wait_for_message("robotiq_force_torque_sensor", ft_sensor, self.__subOdom)
    filter_factory = FileterFactory(ros_node.getOdom())
    akf_filter = filter_factory('AKF')
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
        akf_pos = akf_filter.run(ros_node.getOdom())
        rate.sleep()
