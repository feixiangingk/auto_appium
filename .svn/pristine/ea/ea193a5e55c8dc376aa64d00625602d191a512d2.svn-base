#coding=utf-8
#coding=utf-8

import unittest,sys
# sys.path.append('..')
from functions.appium_init import Initialization
from pages.login_page import Login_Test



class LoginTest(unittest.TestCase):


    def setUp(self):
        info=Initialization()
        self.driver=info.get_driver()
        self.logger=info.logger



    def test_Login_def1(self):
       try:
           d=Login_Test(self.driver)
           username = '18048444414'
           password = 'hele5201'
           self.logger.info(username+password)
           d.logic_login(username,password)
           self.assertEquals(1==1)
           self.logger.info('LoginTest | exec test_Login_def1')

       except Exception,e:
           self.logger.debug('LoginTest | exception is %s' %e)
           self.driver.quit()

       def tearDown(self):
           self.driver.quit()


if __name__ == '__main__':
     unittest.main()

