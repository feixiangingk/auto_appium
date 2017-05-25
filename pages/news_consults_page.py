#coding:utf-8
import time,sys
reload(sys)
sys.setdefaultencoding('utf-8')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *

class NewsConsultsPage(BasePage):
    """
    describe：消息中心咨询页面
    """

    # 元素【出借咨询与服务协议】
    @property
    def el_service_agreement_txt(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'夸客优富私募基金6号')]")

    @property
    def el_service_agreement_title(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'咨询消息')]")





    def Verification_NewsConsults_el(self):
        return self.proving_element('夸客优富私募基金6号')


