#coding:utf-8
import sys
sys.path.append('..')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.my_trade_record_page import MyTradeRecordPage

from pages.my_opinion_page import Opinionpage
from pages.my_bankcard_page import MyBankCardPage

class MyPage(BasePage):
    """
    describe：登录后个人信息页面
    """

    #个人中心
    @property
    def el_my_personalCenter(self):
        #return self.base_find_element(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/img_my')]")
       return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/img_my")

    #我的银行卡
    @property
    def el_my_bankCard(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'我的银行卡')]")

    # 我的银行卡张数
    @property
    def el_my_bankcard_num(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/text_bank_num")

    #交易记录
    @property
    def el_my_transactionRecord_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'交易记录')]")

    #投资记录
    @property
    def el_my_investmentRecord(self):
         return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'投资记录')]")

    #我知道了 浮层
    @property
    def el_tv_know(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_know")

    #意见反馈
    @property
    def el_view_msg(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/re_feedback")


    # 关于我们
    @property
    def el_about_us(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/re_about_us")



    #关于我们详情
    @property
    def el_about_us_deilt(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/img_content")


    # 帮助中心
    @property
    def el_Help_center(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/re_help_center")


    # 帮助中心详情
    @property
    def el_Help_center_deil(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/img_content")


    # 隐藏金额
    @property
    def el_Amount_hidden(self):
        return self.base_find_elements(By.XPATH,"//android.widget.RelativeLayout[contains(@resource-id,'com.quarkfinance.ufo:id/re_img_can_see')]")
        #return self.base_find_elements(By.ID, "com.quarkfinance.ufo:id/re_img_can_see")


    # 金额
    @property
    def el_my_money(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_wealthAmount")

    # 收益
    @property
    def el_Profit_money(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_profitTotal")



    #投资记录快捷入口
    @property
    def el_financial_img(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/return_money_btn")




    #点击投资记录
    def click_my_investmentRecord(self):
        self.el_my_investmentRecord.click()
        return MyInvsetRecorePage(self.driver)

    #点击我的银行卡
    def logic_my_bankCard_click(self):
        self.el_my_bankCard.click()
        return MyBankCardPage(self.driver)

     #投资记录快捷入口
    def logic_financial_img_click(self):
        self.el_financial_img.click()
        return MyInvsetRecorePage(self.driver)


    #点击交易记录
    def logic_my_transactionRecord_btn_click(self):
        self.el_my_transactionRecord_btn.click()
        return MyTradeRecordPage(self.driver)

    def logic_link_myCenter(self):
        from pages.my_personal_center_page import MyPersonalCenterPage
        self.el_my_personalCenter.click()
        return MyPersonalCenterPage(self.driver)

    def logic_view_msg_click(self):
        self.el_view_msg.click()
        return Opinionpage(self.driver)





if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login=LoginPage(driver)
    a=login.logic_login('14488888098','qwe123')
    b=a.click_el_my_btn()
    time.sleep(3)
    b.test_t()





