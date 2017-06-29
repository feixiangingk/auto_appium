#coding:utf-8
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.sms_verification import Message
import time

class RegisterAddCardPage(BasePage):

    context='register add card page'

    #持卡人姓名文本输入框
    @property
    def el_username_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_user_pass")

    #银行卡下拉列表
    @property
    def el_bankcard_list(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_bankname")

    #银行卡号文本输入框
    @property
    def el_cardNo_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_cradnum")

    #预留手机号文本输入框
    @property
    def el_phone_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_phone_num")

    #获取验证码按钮  元素
    @property
    def el_getsms_btn(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/tv_getverify")

    #验证码文本输入框
    @property
    def el_sms_textfield(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/edit_yanzheng")

    #下拉列表中 建设银行 option
    @property
    def el_bank_optionJS(self):
        return self.base_find_element(By.NAME,"中国建设银行")

    #下拉列表中 广发银行 option
    @property
    def el_bank_optionGF(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'广发银行')]")

    #下拉列表中 交通银行 option
    @property
    def el_bank_optionJT(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'交通银行')]")

    #下拉列表中 平安银行 option
    @property
    def el_bank_optionPA(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'平安银行')]")


    #下拉列表中 招商银行 option
    @property
    def el_bank_optionZS(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'招商银行')]")

    #下拉列表中 中信银行 option
    @property
    def el_bank_optionZX(self):
        self.swipe_to_up()
        time.sleep(1)
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中信银行')]")

    # 下拉列表中 中国银行 option
    @property
    def el_bank_optionZG(self):
        self.swipe_to_up()
        time.sleep(1)
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国银行')]")

    # 下拉列表中 农业银行 option
    @property
    def el_bank_optionNY(self):
        self.swipe_to_up()
        time.sleep(1)
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国农业银行')]")

    #下拉列表中 明生银行 option
    @property
    def el_bank_optionMS(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'中国民生银行')]")

    #确认按钮 元素
    @property
    def el_confirm_btn(self):
        return self.base_find_element(By.XPATH,"//*[contains(@resource-id,'com.quarkfinance.ufo:id/tv_nextstep')]")

    #点击获取验证码按钮，获取短信验证码
    def logic_getSMS(self):
        self.el_getsms_btn.click()





    #点击银行卡下拉列表，选择银行
    def logic_choose_bankcard(self,bankType):
        self.el_bankcard_list.click()
        method_name="el_bank_option"+str(bankType)
        time.sleep(1)
        exec "self.%s.click()" %method_name

    #反射机制实现选择银行  暂时有问题
    def logic_choose_bankcard_getattr(self,bankType):
        self.el_bankcard_list.click()
        method_name="el_bank_option"+str(bankType)
        el_option=getattr(self,method_name)
        time.sleep(1)
        el_option.click()



    #最后一个参数bankType为银行简称，输入哪个简称就绑定哪家银行卡
    def logic_insert_bankCard_INFO(self,username,phone,cardNO,bankType='JS'):
        from pages.my_bankcard_page import MyBankCardPage
        self.el_username_textfield.send_keys(username)
        self.logic_choose_bankcard(bankType)
        self.el_cardNo_textfield.send_keys(cardNO)
        self.el_phone_textfield.send_keys(phone)

        self.el_getsms_btn.click()
        sms=Message()
        self.el_sms_textfield.send_keys(sms.get_sms(phone))
        self.el_confirm_btn.click()
        time.sleep(15)

        return MyBankCardPage(self.driver)








