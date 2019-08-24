#!/usr/bin/env python
import math
import numpy as np

class BaseFilter(object):
    """ Interface of filter
    """
    def __init__(self, *arg, **kwarg):
        """ initialize some args """
        pass
    def run(self):
        """ run the filter """
        raise('not implement')

class AKF(BaseFilter):
    """ Adaptive Kalman Filter class """
    def __init__(self, *arg, **kwarg):
        super(AKF, self).__init__(self, *arg, **kwarg)
        self.input_num = kwarg.setdefault('input_num', 1)
        print(self.input_num)
        self.__kp = 2
        self.__a = math.pow(3.0, self.__kp)
        self.__mea_p = arg[0][:self.input_num]
        self.__mea = np.zeros([self.input_num])
        self.__kg = np.zeros([self.input_num])
        self.__est = arg[0][:]
        self.__fp = np.zeros([self.input_num])
    def run(self, pos):
        self.__mea = pos[:self.input_num]
        for i in range(self.input_num):
            self.__fp[i] = abs(self.__est[i] - self.__mea_p[i])
            self.__mea_p[i] = self.__mea[i]
            self.__kg[i] = (self.__a*self.__kg[i]+self.__fp[i])/\
                (self.__a*(1+self.__kg[i])+self.__fp[i])
            self.__est[i] = self.__est[i]+(self.__a*self.__kg[i]+self.__fp[i])*\
                (self.__mea[i]-self.__est[i])/(self.__a*(1+self.__kg[i])+\
                self.__fp[i])
        print("est: ", self.__est, end='\r')
        return (self.__est)
