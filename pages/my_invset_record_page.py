#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.my_asset_details_page import MyAssetDetailsPage

class MyInvsetRecorePage(BasePage):
     """
      describe:投资记录页面
    """

    #理财中
     @property
     def el_my_financial_btn(self):
         return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'理财中')]")

     #退出中
     @property
     def el_drop_out_btn(self):
         return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'退出中')]")

     #已退出
     @property
     def el_exited_btn(self):
         return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'已退出')]")


     #投资记录 ，理财中，退出中，已退出的理财产品列表
     @property
     def el_invest_list(self):
         return self.base_find_elements(By.XPATH,"//android.widget.LinearLayout[contains(@resource-id,'com.quarkfinance.ufo:id/item_view')]")

     # 我知道了 浮层
     @property
     def el_tv_know(self):
         return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_know")


     def logic_invest_list_click(self,index=0):
         self.el_invest_list[index].click()
         return MyAssetDetailsPage(self.driver)



if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    b = a.click_el_my_btn()
    time.sleep(3)
    e=b.test_t()
    time.sleep(2)
    e.press_TouchAction()
    e.el_drop_out.click()
    time.sleep(3)
    #e.el_exited.click()
    #time.sleep(3)
    #e.el_my_financial.click()
    e.invest_list_click()
    
    "17712345606 qwe123"


