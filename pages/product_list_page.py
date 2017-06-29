#coding:utf-8
from functions.BasePage import BasePage
from functions.appium_init import *
from selenium.webdriver.common.by import By
from pages.product_quarkzx_page import ProductQuarkzxPage
from pages.product_van_Gogh_page import ProductVanGoghPage
from pages.my_invset_record_page import MyInvsetRecorePage
from pages.product_beauti_page import ProductBeautiPage
from pages.product_greenHand_page import ProductGreenHandPage
from pages.product_monthly_interest_page import ProductMonthlyInterestPage
from pages.product_riseBystep_page import ProductRiseByStepPage
from pages.product_annualInterestRise_page import ProductAnnualInterestRisePage

class ProductListPage(BasePage):

    context='product list page'

    #夸客尊享按钮 元素
    @property
    def el_quarkZX_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'夸客尊享')]")

    #私募基金按钮 元素
    @property
    def el_fund_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'私募基金')]")

    #续投产品按钮 元素
    @property
    def el_reinvestment_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'续投产品')]")


    #梵高计划按钮  元素
    @property
    def el_van_Gogh_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'梵高计划')]")

    #新手体验计划
    @property
    def el_Novice_experience_btn(self):
        return self.base_find_element(By.XPATH, "//android.widget.TextView[contains(@text,'新手体验计划')]")

    #夸客美丽按钮
    @property
    def el_beauti_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'夸客美丽')]")

    #月月付息按钮 元素
    @property
    def el_monthly_interest_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'月月付息')]")


    #新手体验计划
    @property
    def el_greenHand_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'新手体验计划')]")

    #步步高按钮 元素
    @property
    def el_risebystep_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'步步高')]")

    #年年生利 按钮 元素
    @property
    def el_annualinterestrise_btn(self):
        return self.base_find_element(By.XPATH,"//android.widget.TextView[contains(@text,'年年生利')]")

    #投资记录悬浮层
    @property
    def el_financia_img(self):
        return self.base_find_element(By.ID,"com.quarkfinance.ufo:id/return_money_btn")

    #点击月月付息链接，跳转至月月付息产品详情page
    def logic_link_monthly_interest(self):
        self.el_monthly_interest_btn.click()
        return ProductMonthlyInterestPage(self.driver)

    #点击步步高按钮，跳转至步步高产品详情page
    def logic_link_rise_by_step(self):
        self.el_risebystep_btn.click()
        return ProductRiseByStepPage(self.driver)

    def logic_link_annualInterestRise(self):
        self.el_annualinterestrise_btn.click()
        return  ProductAnnualInterestRisePage(self.driver)


    #点击夸客尊享链接，跳转至夸客尊享产品详情page
    def logic_link_quarkZX(self):
        self.el_quarkZX_btn.click()
        return ProductQuarkzxPage(self.driver)

    #点击新手体验计划，跳转至新手体验计划详情page
    def logic_link_greenHand(self):
        self.el_greenHand_btn.click()
        return ProductGreenHandPage(self.driver)


    #点击梵高计划链接，跳转至梵高计划产品详情page
    def logic_link_van_Gogh(self):
        self.el_van_Gogh_btn.click()
        return ProductVanGoghPage(self.driver)

    def logic_link_beauti(self):
        self.el_beauti_btn.click()
        return ProductBeautiPage(self.driver)

    #非登录状态，点击私募基金链接，跳转至首页
    def logic_nologin_state_fund(self):
        from pages.login_page import LoginPage
        self.el_fund_btn.click()
        return LoginPage(self.driver)

    # 登录状态，点击私募基金链接，跳转至私募列表页
    def logic_login_private_fund(self):
        from pages.private_offering_fund_page import Private_Offering_Fund_Page
        self.el_fund_btn.click()
        return Private_Offering_Fund_Page(self.driver)

    #非登录状态，点击续投产品链接，跳转至首页
    def logic_nologin_state_reinvestment(self):
        from pages.login_page import LoginPage
        self.el_reinvestment_btn.click()
        return LoginPage(self.driver)

    # 跳转投资记录page
    def logic_financia_img_click(self):
        self.el_financia_img.click()
        return  MyInvsetRecorePage(self.driver)

    #非登录状态点击新手体验计划
    def logic_notlogin_prodict(self):
        self.el_Novice_experience_btn.click()
        return ProductBeautiPage(self.driver)

