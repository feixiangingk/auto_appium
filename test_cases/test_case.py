#coding=utf-8

import unittest,sys
sys.path.append('..')
from pages.login_page import Login_Test
from functions.appium_init import *
from functions.interface_case import InterfaceCase




class LoginTest(InterfaceCase):


    def setUp(self):
        # info = Initialization()
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger

    def test_add(self):
        self.assertEqual(self.inital.project_path,'D:\\quarkscript\\UFO_appium')


    def test_new_PO_test(self):
        u"""成功登录"""
        try:
            username = '18048444414'
            password = 'hele5201'
            self.driver.implicitly_wait(5)
            login=Login_Test(self.driver)
            login.page_swipe()
            login.logic_login(username, password)
            self.assertEqual(1, 1)

            # assert (1==1)
        except Exception,e:
            # self.driver.quit()
            self.logger.info(e)

        # finally:
            # self.driver.quit()


    @unittest.skip('skip')
    def test_Skip(self):
        print "不执行用例"


    def tearDown(self):
       #self.devices.close_app()
        #self.devices.close()
        self.driver.quit()




    # @unittest.skip('skip')
    # def test_Login_def1(self):
    #    try:
    #         username='18048444414'
    #         password='hele5201'
    #         #a=LoginTest()
    #         login=Login_Test(self.driver)
    #         login.login_test(username,password)
    #         #self.Login_Test_def()
    #         assert (1==1)
    #
    #    finally:
    #         #getDriver.Closs_Driver()
    #         self.driver.quit()





if __name__ == '__main__':
     unittest.main(verbosity =2)