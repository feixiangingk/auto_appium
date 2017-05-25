#coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class MyAssetDetailsPage(BasePage):
    """
    describe:资产详情页面
    """


    #资产详情title
    @property
    def el_pact_title_btn(self):
        return self.base_find_element(By.XPATH,
                                      "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")


    # 合同编号
    @property
    def el_pact_number_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/text_reinvest_contract_no')]")


    #电子合同
    @property
    def el_Asset_pact_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'电子合同查询')]")


    def click_pact(self):
        self.el_Asset_pact_btn.click()


        #资产详情投资记录明细
    def get_assetdetails_list(self,index=0):
        product_name=self.base_find_elements(By.ID,'com.quarkfinance.ufo:id/text_reinvest_product_name')[index].text
        contract_number=self.base_find_elements(By.ID,'com.quarkfinance.ufo:id/text_reinvest_contract_no')[index].text
        Asset_list=[product_name,contract_number]

        return Asset_list
    
    
    
    def openpage(self):
        
        
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login()
        mypage = homepage.click_el_my_btn()
        mypage.el_tv_know.click()
        myinvsetrecorepage=mypage.click_my_investmentRecord()
        myinvsetrecorepage.el_tv_know.click()
        return  myinvsetrecorepage





if __name__ == '__main__':
    Init()
    driver = appium_init.inital.get_driver()
    from pages.startup_page import StartupPage
    startupPage = StartupPage(driver)
    homepage = startupPage.page_swipe()
    loginPage = homepage.logic_link_login_page()
    homepage = loginPage.logic_login()
    time.sleep(1)
    MyPage=homepage.click_el_my_btn()
    MyPage.el_tv_know.click()
    myinvsetrecorepage=MyPage.click_my_investmentRecord()
    myinvsetrecorepage.el_tv_know.click()
    MyAssetDetailsPage=myinvsetrecorepage.logic_invest_list_click()
    assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()
    
    print assetdetails_list[0]
    print assetdetails_list[1]
    


    
  