#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *
from pages.news_contracts_page import NewsContractsPage
from pages.news_consults_page import NewsConsultsPage


class NewsPage(BasePage):
    """
    describe：消息中心
    """

    #合同消息
    @property
    def el_contract_message_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'合同消息')]")

    #咨询消息
    @property
    def el_consult_message_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'咨询消息')]")

    #未读消息数
    @property
    def el_unread_message_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tv_message_number')]")

    @property
    def el_newspage_title_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@resource-id,'com.quarkfinance.ufo:id/tb_title')]")




    def click_el_contract_message_btn(self):
        """
        :return:  NewsContractsPage  消息中心合同消息
        """
        self.el_contract_message_btn.click()

        return NewsContractsPage(self.driver)

    def click_el_consult_message_btn(self):
        """
        :return:  NewsConsultsPage   消息中心咨询页面
        """
        self.el_consult_message_btn.click()
        return NewsConsultsPage(self.driver)

    def Verification_newspage_el(self):
        return  self.proving_element('合同消息')




    def get_el_consult_message_btn(self):
        """
        :return: message_number
        """
        return  self.el_unread_message_btn.text

    def get_el_newspage_title(self):
        """
        :return:  newspage title
        """
        try:
            return  self.el_newspage_title_btn.text
        except  AttributeError,e:
            self.logger.debug('LoginTest | exception is %s' % e)
            #self.driver.quit()




if __name__ == '__main__':
    from login_page import LoginPage
    Init()
    driver = appium_init.inital.get_driver()
    login = LoginPage(driver)
    a = login.logic_login('14488888098', 'qwe123')
    time.sleep(1.5)
    b=a.el_news_img_click()
    print b.el_consult_message_btn_get
