#coding=utf-8

import unittest,sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.entry_page import Entry_page
from  pages.converged_page import ConvergedPage
from functions.appium_init import *


class Private_fund(InterfaceCase):
    """私募预约模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger

    @unittest.skip("t")
    def test_private_fund_list(self):
        """私募预约-私募预约列表验证"""

        entry_page = Entry_page(self.driver)
        private_Offering_Fund_Page=entry_page.open_Private_Offering_Fund_Page()

        entry_page.saveScreenshot("private_fund_list")
        self.assertEquals(len(private_Offering_Fund_Page.el_private_fund_list),2)



    def test_private_fund_details(self):
        """私募预约-私密预约验证"""

        convergedPage = ConvergedPage(self.driver)
        (user_phone, pwd) = convergedPage.register_customer()

        self.driver = appium_init.inital.get_driver()
        entry_page = Entry_page(self.driver,phone=user_phone,pwd=pwd)

        private_Offering_Fund_Page = entry_page.open_Private_Offering_Fund_Page()
        private_Offering_Fund_Page.el_Popup_btn.click()
        private_Fund_Details_Page=private_Offering_Fund_Page.logic_private_fund_lis_click()
        private_Fund_Details_Page.el_input_consultation.click()
        private_Fund_Details_Page.el_input_password.send_keys(pwd)
        private_Fund_Details_Page.el_input_btn.click()
        message=private_Fund_Details_Page.el_text_message_text.text
        private_Fund_Details_Page.el_confirm_btn.click()

        entry_page.saveScreenshot("private_fund_details")

        self.assertEquals("您已预约咨询本产品，理财经理会尽快与您联系，谢谢！",message)
        #print message




    def tearDown(self):
         self.driver.quit()



if __name__ == '__main__':
    Init()
    unittest.main()