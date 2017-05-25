#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.login_page import LoginPage as login
from pages.banner_pages import BannerPages
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver

class NewsMesg(InterfaceCase):
    """消息中心模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger



    def test_newspage_contract(self):
        """消息中心-合同消息-本金确认书验证"""


        #客户登录并进入消息中心列表
        newspage = self.logon()
        #点击合同列表页面
        contractspage=newspage.click_el_contract_message_btn()
        #点击合同详情页
        contractdetailspage=contractspage.click_el_check_pact_btn()
        #点击出借本金确认书 el_capital_btn
        contractdetailspage.clcik_el_capital_btn()

        bool1 = contractdetailspage.get_screenshot_by_element(contractdetailspage, 'el_capital_img',isexist=False)  #第一次截图时
        #进行截图对比
        time.sleep(5)
        bool1= contractdetailspage.get_screenshot_by_element(contractdetailspage,'el_capital_img',isexist=True).same_as(percent=30)
        print bool1

        #断言判断
        title=contractdetailspage.el_capitalt_title.text
        self.assertTrue(bool1)
        self.assertEqual(title,'出借本金确认书')


    def test_contract_list(self):
        """消息中心-合同消息-展示本金确认书合同列表"""

        # 客户登录并进入消息中心列表
        newspage = self.logon()
        # 点击合同列表页面
        contractspage = newspage.click_el_contract_message_btn()

        time.sleep(2)
        #获取列表中第 index 个的详情数据,默认最新的一条数据
        con_list=contractspage.get_Contracts_list_text(index=0)
       # print "con_list is %s" %con_list[0]
        #从DB中查询购买的最新的理财产品信息
        #sql=Exce_SQLserver()
       # results = sql.execSql_getList(
           # "SELECT top 1  new_product_name,new_investdate,new_name,new_financeterm from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' order BY  new_investdate DESC")
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList("SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' order BY  CreatedOn DESC")
        #print "product_name is %s" %product_name
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT top 1  new_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' order BY  CreatedOn DESC")
        #print "contract_number is %s" % contract_number

        #print con_list[2]
        #print  contract_number[0][0]

        #断言处理
        self.assertIn(con_list[0],product_name[0][0])
        self.assertEqual(con_list[2],contract_number[0][0])

        """
        [u'\u5938\u5ba2\u5c0a\u4eab', u'2017-05-22', u'UF201500009497', u'90\u5929']
        [(u'\u5938\u5ba2\u5c0a\u4eab*90\u5929', datetime.datetime(2017, 5, 22, 10, 39, 4), u'UF201500009497', 90)]
        """



    def test_consultation_mes(self):
        """消息中心-咨询消息-展示咨询消息列表"""

        # 客户登录并进入消息中心列表
        newspage = self.logon()

        # 点击合同列表页面
        newsconsultspage = newspage.click_el_consult_message_btn()

        newsconsultspage_title=newsconsultspage.el_service_agreement_title.text

        self.assertEqual(newsconsultspage_title,'咨询消息')

    def logon(self):
        startupPage = StartupPage(self.driver)
        homepage = startupPage.page_swipe()
        loginPage = homepage.logic_link_login_page()
        homepage = loginPage.logic_login()
        time.sleep(1)
        newspage = homepage.logic_click_el_news_img()
        return  newspage

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    Init()
    unittest.main()



