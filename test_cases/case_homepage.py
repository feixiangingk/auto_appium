#coding=utf-8

import unittest,sys
reload(sys)
sys.setdefaultencoding('utf-8')

sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.startup_page import StartupPage
from pages.home_page import HomePage
from functions.BasePage import BasePage
from pages.entry_page import Entry_page



class hometest(InterfaceCase):
    u"""首页模块验证"""


    """
    setup():每个测试case运行前运行
    teardown():每个测试case运行完后执行
    setUpClass():必须使用@classmethod 装饰器,所有case运行前只运行一次
    tearDownClass():必须使用@classmethod装饰器,所有case运行完后只运行一次
    """

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger=self.inital.logger


    #id:输入需要验证的banner 索引ID
    #assertEqual 输入预期的banner详情的title


    def test_click_banner1(self):
        u"""验证banner[1]"""

        startUp=StartupPage(self.driver)
        homepage=startUp.page_swipe()
        b=homepage.banner_click(id=1)
        time.sleep(3)
        self.logger.info(b.el_title.text)
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('click_banner1')
        self.logger.info(self.assertEqual(b.el_title.text, u"系统维护"))
        #self.assertEqual(b.el_title.text, u"系统维护")


    def test_click_banner3(self):
            u"""验证banner[3]"""

            # id:输入需要验证的banner 索引ID
            # assertEqual 输入预期的banner详情的title

            startUp=StartupPage(self.driver)
            homepage=startUp.page_swipe()
            b=homepage.banner_click(id=3)
            time.sleep(1)
            self.logger.info(b.el_title.text)
            self.basepage = BasePage(self.driver)
            self.basepage.saveScreenshot('click_banner3')
           # self.assertEqual(b.el_title.text, u"夸客美丽增值计划")


    def test_click_banner5(self):
            u"""验证banner[5]"""
            # id:输入需要验证的banner 索引ID
            # assertEqual 输入预期的banner详情的title

            startUp = StartupPage(self.driver)
            homepage = startUp.page_swipe()
            b = homepage.banner_click(id=5)
            time.sleep(3)
            self.logger.info(b.el_title.text)
            self.basepage = BasePage(self.driver)
            self.basepage.saveScreenshot('click_banner5')
           # self.assertEqual(b.el_title.text, u"新春心意")


    def test_newuser_product_buy(self):
        """新用户首页理财产品验证"""
        "14414441414 ，qwe123"

        entry_page=Entry_page(self.driver,phone='14414441414')
        homepage=entry_page.open_login_home_page()
        title_text=homepage.get_product_title_text()
        entry_page.saveScreenshot('newuser_product_buy')

        self.assertEquals(title_text,"新手体验计划")



    def test_system_notice(self):
        """首页-未登录点击系统广告"""
        entry_page = Entry_page(self.driver)
        homepage = entry_page.open_start_home_page()
        homepage.el_system_notice.click()
        time.sleep(2)
        entry_page.saveScreenshot('system_notice')


    def test_home_product(self):
        """首页-未登录点击推荐产品"""
        entry_page = Entry_page(self.driver)
        homepage = entry_page.open_start_home_page()
        productBeautiPage=homepage.logic_el_invest_newpeo_click()
        title=productBeautiPage.logic_get_title_text()
        entry_page.saveScreenshot('home_product')
        self.assertEquals(title,"新手体验计划")


    def test_product_notlogin(self):
        """首页-未登录购买理财产品"""
        entry_page = Entry_page(self.driver)
        homepage = entry_page.open_start_home_page()
        productBeautiPage = homepage.logic_el_invest_newpeo_click()
        #productListPage=homepage.logic_link_product()
       # productBeautiPage=productListPage.logic_notlogin_prodict()
        loginPage=productBeautiPage.logic_noLogin_state_buy()
        title=loginPage.el_title.text

        entry_page.saveScreenshot('product_notlogin')
        self.assertEquals(title,"登录")



    def tearDown(self):
         self.driver.quit()



if __name__ == '__main__':
    Init()
    unittest.main()