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

    #资产详情title
     @property
     def el_invest_title(self):
         return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tb_title")

     # 我知道了 浮层
     @property
     def el_tv_know(self):
         return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_know")

    #产品名称
     @property
     def el_invest_text_name(self):
         return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/text_name")

    # 合同编号
     @property
     def el_invest_product_no(self):
             return self.base_find_elements(By.ID, "com.quarkfinance.ufo:id/text_product_no")

    #起息日
     @property
     def el_start_income_day(self):
         return self.base_find_elements(By.XPATH, "//*[@resource-id='com.quarkfinance.ufo:id/text_start_income_day']/android.widget.TextView")

     # 结息日
     @property
     def el_end_income_day(self):
        return self.base_find_elements(By.XPATH,
                                            "//*[@resource-id='com.quarkfinance.ufo:id/text_end_income_day']/android.widget.TextView")

     #实际投资
     @property
     def el_reality_invest(self):
         return self.base_find_elements(By.XPATH,
                                        "//*[@resource-id='com.quarkfinance.ufo:id/text_reality_invest']/android.widget.TextView")

    #意向投资
     @property
     def el_expected_invest(self):
         return self.base_find_elements(By.XPATH,
                                        "//*[@resource-id='com.quarkfinance.ufo:id/text_expected_invest']/android.widget.TextView")




     def logic_invest_list_click(self,index=0):
         time.sleep(0.5)
         self.el_invest_list[0].click()
         return MyAssetDetailsPage(self.driver)

     def logic_get_invest_title(self):
         title=self.el_invest_title.text
         return title

     #获取列表
     def logic_get_invest_value(self,index=0):
         invest_dic={}
         invest_text_name=self.el_invest_text_name[index].text
         invest_product_no=self.el_invest_product_no[index].text
         start_income_day=self.el_start_income_day[index*2+1].text
         end_income_day=self.el_end_income_day[index*2+1].text
         reality_invest=self.el_reality_invest[index*2+1].text
         expected_invest=self.el_expected_invest[index*2+1].text
         invest_dic={"invest_text_name":invest_text_name,"invest_product_no":invest_product_no,"start_income_day":start_income_day,"end_income_day":end_income_day,"reality_invest":reality_invest,"expected_invest":expected_invest}

         return invest_dic









if __name__ == '__main__':

    from entry_page import Entry_page
    Init()
    driver = appium_init.inital.get_driver()

    Entry_page=Entry_page(driver)
    myinvsetrecorepage=Entry_page.open_my_invset_recore_Page()
    dic1=myinvsetrecorepage.logic_get_invest_value(index=1)

    print  dic1.items()



    
    "17712345606 qwe123"


