#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *


class Electronic_contract_page(BasePage):
    """
      describe:电子合同页面
    """

    # title
    @property
    def el_contract_title(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tb_title")

    # no1 -4
    @property
    def el_contract_no1(self):

        return  self.base_find_elements(By.XPATH,"//android.widget.ListView/android.widget.LinearLayout")
        #return self.base_find_element(By.XPATH, "//android.widget.LinearLayout[contains(@text,'《出借咨询与服务协议》')]")



    # 合同详情页title
    @property
    def el_contract_details_title(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tb_title")


    def logic_contract_no1_click(self,index):
        self.el_contract_no1[index].click()


    def logic_get_contract_details_title(self):
        return self.el_contract_details_title.text


