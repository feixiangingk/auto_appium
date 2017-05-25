#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *


class MyTradeRecordPage(BasePage):

    """
      describe：交易记录页面
    """

    #交易
    @property
    def el_trade_btn(self):
        return self.base_find_elements(By.XPATH, "//android.widget.TextView[contains(@text,'交易')]")

    #我知道了 确认按钮
    @property
    def el_tv_know(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_know")

    #咨询
    @property
    def el_trade_Consultation_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'咨询')]")


    #进入交易list
    def el_trade_btn_click(self):
          self.el_trade_btn[1].click()




if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b=a.click_el_my_btn()
    b.test_t()

    c=MyTradeRecordPage(driver)
    c.el_trade_Consultation_btn.click()
    time.sleep(3)
    c.el_trade_btn[1].click()

