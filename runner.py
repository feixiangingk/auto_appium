#coding=utf-8

import  unittest,os,time
from functions.exec_Suitecase import exec_sutiecase
from functions.appium_init import *
from functions.load_case import LoadCase
from functions.send_mail import SendMail
from functions.AppiumServer import AppiumServer
# case_path="test_cases"
# # result = "D:\\CodeWork\\quarkUFO\\result\\"
#
#
# def Creatsuite():
#     #定义单元测试容器
#     testunit = unittest.TestSuite()
#
#     #定搜索用例文件的方法
#     discover = unittest.defaultTestLoader.discover(case_path, pattern='cases_*.py', top_level_dir=None)
#
#     #将测试用例加入测试容器中
#     for test_suite in discover:
#         for casename in test_suite:
#             testunit.addTest(casename)
#         print testunit
#     return testunit
#
# test_case = Creatsuite()
if __name__ == '__main__':
    if isinstance(appium_init.inital,Initialization)!=True:
        Init()
    testSuite = LoadCase.get_cases(appium_init.inital.desired_caps['testsuite'])

    # 启动appium 服务
    appiumServer = AppiumServer()
    appiumServer.start_server()

    exec_result=exec_sutiecase()
    exec_result.exec_cases(testSuite)
    mail = SendMail()
    # type =0 发送正式邮件  type=1发送测试邮件
    mail_type=str(appium_init.inital.desired_caps['test_mail'])
    mail.send(mail_type)
    appiumServer.stop_server()

    




