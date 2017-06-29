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


    #理财名称和金额
    @property
    def el_name_and_amount(self):
        return  self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount']/android.widget.TextView")

    #时间和状态
    @property
    def el_date_and_status(self):
        return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_date_and_status']/android.widget.TextView")
        #return self.base_find_elements(By.XPATH,"//*[resource-id='com.quarkfinance.ufo:id/text_date_and_status']/android.widget.TextView[1]")

    #交易流水
    @property
    def el_transaction_flowing(self):
        return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_transaction_flowing']/android.widget.TextView")
        #return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_transaction_flowing']/android.widget.TextView")


    #合同编号
    @property
    def el_contract_no(self):
        return self.base_find_elements(By.XPATH,
                                       "//*[@resource-id='com.quarkfinance.ufo:id/text_contract_no']/android.widget.TextView")
        #return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_contract_no']/android.widget.TextView")


    # 续投合同编号
    @property
    def el_reinvest_contract_no(self):
        return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_reinvest_contract_no']/android.widget.TextView")

    #续投方式
    @property
    def el_reinvest_way(self):
        return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_reinvest_way']/android.widget.TextView")

    #预期收益
    @property
    def el_expect_incomeself(self):
        return self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_expect_income']/android.widget.TextView")



    #我知道了 确认按钮
    @property
    def el_tv_know(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_know")

    #咨询
    @property
    def el_trade_Consultation_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'咨询')]")


    #咨询列表
    @property
    def el_trade_Consultation_list(self):
        return self.base_find_elements(By.ID,"com.quarkfinance.ufo:id/layout_item_head")

    # 预约编号
    @property
    def el_trade_Consultation_inquiry_no(self):
            return self.base_find_elements(By.XPATH, "//*[@resource-id='com.quarkfinance.ufo:id/text_inquiry_no']/android.widget.TextView[2]")

    #点击列表
    @property
    def el_trade_list_image(self):

        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/layout_item_head")
        #return  self.base_find_elements(By.XPATH,"//android.widget.RelativeLayout[contains(@id,'com.quarkfinance.ufo:id/layout_item_head')]")


    #点击咨询列表
    def logic_get_Consultation_list(self):
        self.el_trade_Consultation_list[0].click()


    #获取私募预约编号
    def logic_get_inquiry_no_test(self):
        inquiry_no=self.el_trade_Consultation_inquiry_no[0].text
        return  inquiry_no




    @property
    def el_trade_Consultation_btn111(self):
        self.logic_trade_btn_click()
        self.el_trade_list_image[1].click()
        time.sleep(2)

        #el_trade_list_image1=self.el_trade_list_image
        #el_trade_list_image1[1].click()
        #a=self.base_find_element(By.XPATH,"//android.widget.LinearLayout[{index}]/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.TextView".format(index=1))

        #b=self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount'][{id}]/android.widget.TextView".format(id=2))
        b = self.base_find_elements(By.XPATH,
                                    "//android.widget.LinearLayout[{id}]/android.widget.RelativeLayout/android.widget.TextView".format(id=2))
        return  b[0].text

        #return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'咨询')]")


    #进入交易list
    def logic_trade_btn_click(self):
          self.el_trade_btn[0].click()


    def logic_trade_list(self,index=0):
        #self.logic_trade_btn_click
        self.el_trade_list_image.click()
        time.sleep(2)
        trade_dict={}
        txtinvestapply =self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_contract_no']/android.widget.TextView")[1].text
        paymentno = self.base_find_elements(By.XPATH, "//*[@resource-id='com.quarkfinance.ufo:id/text_transaction_flowing']/android.widget.TextView")[1].text
        trade_list=[txtinvestapply,paymentno]

       # trade_dict[u'产品名称']=self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount'][{id}]/android.widget.TextView".format(id=index))[0].text
       # trade_dict[u'金额'] = self.base_find_elements(By.XPATH,"//*[@resource-id='com.quarkfinance.ufo:id/text_name_and_amount']/android.widget.TextView")[1].text

        #print txtinvestapply,paymentno
        return trade_list


    #交易回款列表列表数据获取
    def logic_get_trade_list(self):
        trade_list_dict={}
        #产品名称
        name=self.el_name_and_amount[0].text
        #产品金额
        amount=self.el_name_and_amount[1].text
        #理财时间
        time.sleep(0.2)
        data1=self.el_date_and_status[0].text
        #状态
        status=self.el_date_and_status[1].text
        #流水编号
        flowing=self.el_transaction_flowing[1].text
        #合同编号
        contract_no=self.el_contract_no[1].text
        trade_list_dict={"name":name,"amount":amount,"data":data1,"status":status,"flowing":flowing,"contract_no":contract_no}

        return trade_list_dict


    def logic_get_reinvest_way(self):
        trade_list_dict = {}
        reinvest_way=self.el_reinvest_way[1].text
        expect_incomeself=self.el_expect_incomeself[1].text
        reinvest_contract_no=self.el_reinvest_contract_no[1].text
        trade_list_dict={"reinvest_way":reinvest_way,"expect_incomeself":expect_incomeself,"el_reinvest_contract_no":reinvest_contract_no}

        return  trade_list_dict







if __name__ == '__main__':

    from pages.startup_page import StartupPage
    from functions.appium_init import Initialization
    Init()
    driver = appium_init.inital.get_driver()
    startupPage = StartupPage(driver)
    homepage = startupPage.page_swipe()
    loginPage = homepage.logic_link_login_page()
    homepage = loginPage.logic_login()
    mypage = homepage.click_el_my_btn()
    mypage.el_tv_know.click()
    mytraderecordpage=mypage.logic_my_transactionRecord_btn_click()
    time.sleep(2)
    a=mytraderecordpage.logic_trade_list()

   # print a.items()





