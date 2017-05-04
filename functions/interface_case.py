#coding:utf-8
from appium_init import *
import unittest
class InterfaceCase(unittest.TestCase):
    """docstring for InterfaceCase"""
    def __init__(self, methodName='runTest', inital=None):
        super(InterfaceCase, self).__init__(methodName)
        if isinstance(appium_init.inital,Initialization)!=True:
            Init()
        self.inital=appium_init.inital
