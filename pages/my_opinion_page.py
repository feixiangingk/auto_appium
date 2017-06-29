
#coding:utf-8
import sys
sys.path.append('..')
from functions.BasePage import BasePage
from selenium.webdriver.common.by import By
from functions.appium_init import *


class Opinionpage(BasePage):
        """意见反馈页面"""


        #意见反馈输入框
        @property
        def el_opinionp_Input_box(self):
            return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/et_feedback")

        #意见反馈提交按钮
        @property
        def el_opinionp_Submit_bt(self):
            return self.base_find_element(By.ID, "com.quarkfinance.ufo:id/bt_confirm")

        # 权限弹层
        @property
        def el_opinionp_jurisdiction_bt(self):
            #return self.base_find_elements(By.XPATH,"//android.widget.Button[contains(@text,'允许')]")
            return  self.base_find_element(By.ID,"com.android.packageinstaller:id/permission_allow_button")




        #输入数据
        def logic_input_data(self,strmeg):
            self.el_opinionp_Input_box.send_keys(strmeg)

        #提交数据
        def logic_Submit_meg_click(self):
            self.el_opinionp_Submit_bt.click()

        #权限弹层处理
        def logic_jurisdiction_click(self):
            self.el_opinionp_jurisdiction_bt.click()










