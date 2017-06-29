#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class My_Invest_Profit_Detailed_page(BasePage):
    """
         describe:月月付息收益明细
       """

    #收益金额
    @property
    def el_my_money_btn(self):
         return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/text_money")




    def logic_get_sum_money(self):
        sum_money=0
        for i in self.el_my_money_btn:
            strmoney=i.text[:-4]
            #print  strmoney
            sum_money  += int(strmoney)
           # a =+ int(i.text)

        return sum_money


    def test01(self):

        for i in self.el_my_money_btn:
             a =i.text
             print a

