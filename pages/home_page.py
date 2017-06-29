#coding:utf-8

import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')

from functions.BasePage import BasePage
from selenium.webdriver.common.by import By

from functions.appium_init import *
from pages.product_list_page import ProductListPage
from pages.news_page import NewsPage
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.my_page import MyPage
from pages.banner_pages import BannerPages
from pages.product_beauti_page import ProductBeautiPage


class HomePage(BasePage):

    context='im home page'


    #获取有多少Banner广告  ;这里获取的页面的元素属性，命名还是一个el开头。返回的是一个元素，而不是xpath,稍作修改
    @property
    def el_Banner(self):
        return self.base_find_elements(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/image_indicator')]")

    #系统公告
    @property
    def el_system_notice(self):
        return self.base_find_element(By.XPATH,
                                       "//*[@resource-id='com.quarkfinance.ufo:id/tv_verticalScrollTV']/android.widget.TextView[1]")

    #"我的"按钮 元素
    @property
    def el_my_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'我的')]")

    #"产品列表"按钮 元素
    @property
    def el_product_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'产品列表')]")

    #首页
    @property
    def el_home_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'首页')]")

    #消息中心
    @property
    def el_news_img(self):
        return self.base_find_elements(By.XPATH, "//android.widget.RelativeLayout[contains(@resource-id,'com.quarkfinance.ufo:id/rl_message_layout')]")

    #投资记录
    @property
    def el_invest_img(self):
       # return self.base_find_element(By.XPATH,"//android.widget.ImageView[contains(@resource-id,'com.quarkfinance.ufo:id/return_money_btn')]")
        return  self.base_find_element(By.ID,"com.quarkfinance.ufo:id/return_money_btn")



    # 新手体验计划投资记录
    @property
    def el_invest_newpeo_img(self):
        return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/tv_invest")

    #立即投资
    @property
    def el_immediate_investment_btn(self):
        return self.base_find_element(By.XPATH,
                                       "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tv_invest')]")


    # 理财产品名称
    @property
    def el_product_title_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_product_title")



    #点击【我的】跳转至my_page,刚注册成功点击该按钮
    def click_el_my_btn(self):
        # self.press_TouchAction()
        self.el_my_btn.click()
        time.sleep(0.5)
        self.el_my_btn.click()
        return MyPage(self.driver)

    #点击【我的】跳转至my_page,刚购买完理财点击该按钮
    def logic_buy_my_btn(self):
        self.el_my_btn.click()
        return MyPage(self.driver)


    #未登录态 点击【我的】跳转至LoginPage
    def logic_link_login_page(self):
        from pages.login_page import LoginPage
        self.el_my_btn.click()
        return LoginPage(self.driver)


    #点击【消息中心】，跳转至newsw_page
    def logic_click_el_news_img(self):
        time.sleep(1)
        self.press_TouchAction()
        self.el_news_img[0].click()
        return NewsPage(self.driver)

    #点击【投资记录】，跳转至 my_invset_record_page
    def logic_click_el_invest_img(self):
        self.press_TouchAction()
        self.el_invest_img.click()
        return MyInvsetRecorePage(self.driver)

    #点击【立即投资】

    def el_immediate_investment_btn_click(self):
        self.press_TouchAction()
        self.el_immediate_investment_btn.click()



    #点击【产品列表】按钮 跳转产品列表page
    def logic_link_product(self):
        self.el_product_btn.click()
        return ProductListPage(self.driver)

    #登录状态 点击产品列表
    def logic_link_login_product(self):
        #time.sleep(0.5)
       #self.press_TouchAction()
        self.el_product_btn.click()
        self.el_product_btn.click()
        return ProductListPage(self.driver)


    def checga_element(self):
        return  self.proving_element('com.quarkfinance.ufo:id/tv_invest')

    #首页理财产品名称
    def get_product_title_text(self):
        text=self.el_product_title_btn.text
        return text


    def logic_el_invest_newpeo_click(self):
         self.el_invest_newpeo_img.click()
         return  ProductBeautiPage(self.driver)




    # 根据传入的ID 点击对应的Banner index
    def banner_click(self,id):
       # print  id
        if id==1:
           # print  "进来了"
            self.el_Banner[id].click()
        else:
            time.sleep(3*(id-1))
            self.el_Banner[id].click()
        time.sleep(0.5)
            #self.saveScreenshot('banner_click')
        return BannerPages(self.driver)
        self.logger.info('HomePage | Exception  is %s %s'%e %(sys._getframe().f_back.f_lineno))
        #self.saveScreenshot('banner_click')
            
    
if __name__ == '__main__':
    Init()
    driver = appium_init.inital.get_driver()
    from pages.login_page import LoginPage
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    a.click_el_news_img()

