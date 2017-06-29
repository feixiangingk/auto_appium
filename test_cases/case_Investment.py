#coding=utf-8

import unittest,sys,datetime
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from functions.BasePage import BasePage
from pages.entry_page import Entry_page


class InvestRecord(InterfaceCase):

    """投资记录模块验证"""


    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_home_financial(self):
        "登录状态-首页进入资产详情"
        entry_page=Entry_page(self.driver)
        homepage=entry_page.open_login_home_page()
        time.sleep(2)
        myInvsetRecorePage=homepage.logic_click_el_invest_img()
        myInvsetRecorePage.el_tv_know.click()
        title_text=myInvsetRecorePage.logic_get_invest_title()

        #截图
        entry_page.saveScreenshot('home_financial')

        #断言
        self.assertEquals(title_text,u"投资记录")


    def test_product_financial(self):
        "登录状态—产品列表进入资产详情"
        entry_page = Entry_page(self.driver)
        productListPage = entry_page.open_login_productList_page()
        myInvsetRecorePage=productListPage.logic_financia_img_click()
        myInvsetRecorePage.el_tv_know.click()
        title_text=myInvsetRecorePage.logic_get_invest_title()

        # 截图
        self.assertEquals(title_text, u"投资记录")

        # 断言
        entry_page.saveScreenshot('product_financial')


    def test_my_financial(self):
        "登录状态-我的列表进入资产详情"
        entry_page = Entry_page(self.driver)
        mypage=entry_page.open_login_my_page()

        myInvsetRecorePage=mypage.logic_financial_img_click()
        myInvsetRecorePage.el_tv_know.click()

        title_text = myInvsetRecorePage.logic_get_invest_title()
        # 断言
        self.assertEquals(title_text, u"投资记录")
        # 截图
        entry_page.saveScreenshot('my_financial')


    def test_financial_list(self):
        "投资记录-理财中列表数据验证"

        entry_page = Entry_page(self.driver)
        myinvsetrecorepage=entry_page.open_my_invset_recore_Page()
        invest_list_value=myinvsetrecorepage.logic_get_invest_value()
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_product_name,new_name,new_instreststartdate,new_quitdate,new_planmoney,new_planmoney_Base from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")

        entry_page.saveScreenshot('financial_data')
        #断言验证

        #断言理财名称
        self.assertIn(invest_list_value["invest_text_name"],contract_number[0][0])
        #断言合同编号
        self.assertIn(contract_number[0][1],invest_list_value["invest_product_no"])
        #断言起息日
        self.assertEquals(invest_list_value["start_income_day"], (contract_number[0][2].date()+datetime.timedelta(days = 1)).strftime("%Y-%m-%d"))

        #断言结息日
        if  '年年生利' in invest_list_value["invest_text_name"]:
            self.assertIn("随时申请退出",invest_list_value["end_income_day"])
        else:
            self.assertEquals(invest_list_value["end_income_day"],(contract_number[0][3].date().strftime("%Y-%m-%d")))

        #断言 实际投资金额
        self.assertIn(str(contract_number[0][4])[:-6]+ ","+ str(contract_number[0][4])[-6:],invest_list_value["reality_invest"])

        #断言 意向投资金额
        self.assertIn(str(contract_number[0][5])[:-6]+ ","+ str(contract_number[0][5])[-6:],invest_list_value["expected_invest"])


    def test_quiting_list(self):
        "投资记录-退出中列表数据验证"

        entry_page = Entry_page(self.driver)
        myinvsetrecorepage = entry_page.open_my_invset_recore_Page()
        time.sleep(0.2)
        myinvsetrecorepage.el_drop_out_btn.click()

        invest_list_value = myinvsetrecorepage.logic_get_invest_value()
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList(
            "SELECT  top 1 new_product_name,new_name,new_instreststartdate,new_quitdate,new_planmoney,new_planmoney_Base from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000003 order BY  new_paidon desc")

        entry_page.saveScreenshot('test_quiting_list')
        # 断言验证

        # 断言理财名称
        self.assertIn(invest_list_value["invest_text_name"], contract_number[0][0])

        # 断言合同编号
        self.assertIn(contract_number[0][1], invest_list_value["invest_product_no"])

        # 断言起息日
        self.assertEquals(invest_list_value["start_income_day"],
                          (contract_number[0][2].date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

        # 断言结息日
        if '年年生利' in invest_list_value["invest_text_name"]:
            self.assertIn("随时申请退出", invest_list_value["end_income_day"])
        else:
            self.assertEquals(invest_list_value["end_income_day"], (contract_number[0][3].date().strftime("%Y-%m-%d")))

        # 断言 实际投资金额
        self.assertIn(str(contract_number[0][4])[:-6] + "," + str(contract_number[0][4])[-6:],
                      invest_list_value["reality_invest"])

        # 断言 意向投资金额
        self.assertIn(str(contract_number[0][5])[:-6] + "," + str(contract_number[0][5])[-6:],
                      invest_list_value["expected_invest"])


    def test_invest_contract_no1(self):
        """资产详情-电子合同《出借咨询与服务协议》验证"""
        entry_page = Entry_page(self.driver)
        electronic_contract_page=entry_page.open_Electronic_contract_page()
        time.sleep(1)
        electronic_contract_page.logic_contract_no1_click(index=0)
        title=electronic_contract_page.logic_get_contract_details_title()
        entry_page.saveScreenshot('invest_contract_no1')
        self.assertEquals(title,"出借咨询与服务协议")


    def test_invest_contract_no2(self):
        """资产详情-电子合同《授权委托书-出借确认和债权转让》验证"""
        entry_page = Entry_page(self.driver)
        electronic_contract_page = entry_page.open_Electronic_contract_page()
        time.sleep(1)
        electronic_contract_page.logic_contract_no1_click(index=1)
        title = electronic_contract_page.logic_get_contract_details_title()
        entry_page.saveScreenshot('invest_contract_no2')
        self.assertEquals(title, "授权委托书-出借确认和债权转让")


    def test_invest_contract_no3(self):
        """资产详情-电子合同《授权委托书-催收及诉讼》验证"""
        entry_page = Entry_page(self.driver)
        electronic_contract_page = entry_page.open_Electronic_contract_page()
        time.sleep(1)
        electronic_contract_page.logic_contract_no1_click(index=2)
        title = electronic_contract_page.logic_get_contract_details_title()
        entry_page.saveScreenshot('invest_contract_no3')
        self.assertEquals(title, "授权委托书-催收及诉讼")


    def test_invest_contract_no4(self):
        """资产详情-电子合同《出借本金确认书》验证"""
        entry_page = Entry_page(self.driver)
        electronic_contract_page = entry_page.open_Electronic_contract_page()
        time.sleep(1)
        electronic_contract_page.logic_contract_no1_click(index=3)
        title = electronic_contract_page.logic_get_contract_details_title()
        entry_page.saveScreenshot('invest_contract_no4')
        self.assertEquals(title, "出借本金确认书")


    def test_invest_profit_detailed(self):
        """投资记录-资产详情-月月付息收益详情"""

        "账户 15948444448  qwe123"

        entry_page = Entry_page(self.driver, phone="15948444448",pwd='qwe123')
        myAssetDetailsPage=entry_page.open_my_assetDetails_quiting_page()
        My_Invest_Profit_Detailed_page=myAssetDetailsPage.logic_Profit_btn_click()
        time.sleep(1)
        entry_page.saveScreenshot('invest_profit_detailed')
        money=My_Invest_Profit_Detailed_page.logic_get_sum_money()

        #对金额进行断言
        self.assertNotEqual(money,0)


    def test_Exited_list(self):
        "投资记录-已退出列表数据验证"
        entry_page = Entry_page(self.driver,phone='17712345606',pwd='qwe123')
        myinvsetrecorepage = entry_page.open_my_invset_recore_Page()
        time.sleep(0.2)
        myinvsetrecorepage.el_exited_btn.click()
        invest_list_value = myinvsetrecorepage.logic_get_invest_value()
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList(
            "SELECT  top 1 new_product_name,new_name,new_instreststartdate,new_quitdate,new_planmoney,new_planmoney_Base from new_investdetailBase WHERE new_accountname = 'F86EEE35-2940-E711-80D3-00155D02B414' AND  new_status=100000002 order BY  new_paidon desc")

        entry_page.saveScreenshot('test_Exited_list')
        # 断言验证

        # 断言理财名称
        self.assertIn(invest_list_value["invest_text_name"], contract_number[0][0])

        # 断言合同编号
        self.assertIn(contract_number[0][1], invest_list_value["invest_product_no"])

        # 断言起息日
        self.assertEquals(invest_list_value["start_income_day"],
                          (contract_number[0][2].date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

        # 断言结息日
        self.assertEquals(invest_list_value["end_income_day"], (contract_number[0][3].date() + datetime.timedelta(days=1)).strftime("%Y-%m-%d"))

        # 断言 实际投资金额
        self.assertIn(str(contract_number[0][4])[:-6] + "," + str(contract_number[0][4])[-6:],
                      invest_list_value["reality_invest"])

        # 断言 意向投资金额
        self.assertIn(str(contract_number[0][5])[:-6] + "," + str(contract_number[0][5])[-6:],
                      invest_list_value["expected_invest"])

    def test_financial_data(self):
        """投资记录-理财中资产详情数据验证"""

        entry_page = Entry_page(self.driver)
        MyAssetDetailsPage = entry_page.open_my_assetDetails_page()
        time.sleep(1.5)

        #获得资产详情页列表数据，默认获得第index=0 个
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text

        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = '24004F6C-7C08-E711-80C9-00155D01F903' AND  new_status=100000000 order BY  new_paidon desc")

        #断言
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('financial_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')

    def test_quiting_data(self):
        """投资记录-退出中资产详情数据验证"""

        entry_page = Entry_page(self.driver,phone='14477650717',pwd='qwe123')
        MyAssetDetailsPage = entry_page.open_my_assetDetails_quiting_page()


        #获得资产详情页列表数据，默认获得第index=0 个
        time.sleep(1.5)
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()
        time.sleep(2)

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text
        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = '331C4E9C-D93A-E711-80D3-00155D02B414' AND  new_status=100000003 order BY  new_instreststartdate desc")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = '331C4E9C-D93A-E711-80D3-00155D02B414' AND  new_status=100000003 order BY  new_instreststartdate desc")

        #断言

        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('quiting_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')


    def test_Exited_data(self):
        """投资记录-已退出资产详情数据验证"""

        entry_page = Entry_page(self.driver, phone='17712345606',pwd='qwe123')
        MyAssetDetailsPage = entry_page.open_my_assetDetails_Exited_page()
        time.sleep(1.5)
        assetdetails_list=MyAssetDetailsPage.get_assetdetails_list()

        pact_title=MyAssetDetailsPage.el_pact_title_btn.text

        #查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        contract_number = sql.execSql_getList("SELECT  top 1 new_name from new_investdetailBase WHERE new_accountname = 'F86EEE35-2940-E711-80D3-00155D02B414' AND  new_status=100000002 order BY  new_instreststartdate desc ")

        #查询DB 获得理财产品名称
        sql = Exce_SQLserver()
        product_name = sql.execSql_getList(
            "SELECT top 1  new_product_name from new_investdetailBase WHERE new_accountname = 'F86EEE35-2940-E711-80D3-00155D02B414' AND  new_status=100000002 order BY  new_instreststartdate desc")

        #断言
        self.basepage = BasePage(self.driver)
        self.basepage.saveScreenshot('Exited_data')
        self.assertIn(assetdetails_list[0],product_name[0][0])
        self.assertIn(contract_number[0][0],assetdetails_list[1])
        self.assertEqual(pact_title,'资产详情')


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    "月月付息 17712345602 qwe123"
