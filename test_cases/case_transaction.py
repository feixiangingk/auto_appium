#coding=utf-8

import unittest,sys
sys.path.append('..')
import time
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.appium_init import *
from pages.entry_page import Entry_page

class Transaction(InterfaceCase):
    """交易记录模块验证"""

    def setUp(self):
        self.driver = self.inital.get_driver()
        self.logger = self.inital.logger


    def test_transaction_list(self):
        """交易记录-交易列表数据验证"""
        #mytraderecordpage=self.into_transaction()

        entry_page = Entry_page(self.driver)
        mytradeRecordPage = entry_page.open_my_tradeRecord_page()

       # time.sleep(2)
        trade_list = mytradeRecordPage.logic_trade_list()
        # 查询DB 获得理财中第一个理财的合同编号
        sql = Exce_SQLserver()
        txtinvestapply = sql.execSql_getList("SELECT  top 1 new_txtinvestapply from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
       # print  txtinvestapply[0][0]
        #print  trade_list[0]
        sql = Exce_SQLserver()
        paymentno = sql.execSql_getList("SELECT top 1  new_paymentno from new_tradedetailBase WHERE new_account = '24004F6C-7C08-E711-80C9-00155D01F903'  ORDER BY new_paydate DESC")
        #print  paymentno[0][0]
        #print trade_list[1]

        entry_page.saveScreenshot('transaction_list')
        self.assertEquals(trade_list[0],txtinvestapply[0][0])
        self.assertEquals(trade_list[1], paymentno[0][0])


    def test_transaction_consultation(self):
        """交易记录-咨询消息验证"""
        "14114444144"

        entry_page=Entry_page(self.driver)
        mytradeRecordPage=entry_page.open_my_tradeRecord_page()
        mytradeRecordPage.el_trade_Consultation_btn.click()
        mytradeRecordPage.el_trade_Consultation_list[0].click()
        #time.sleep(2)
        title=mytradeRecordPage.logic_get_inquiry_no_test()

        entry_page.saveScreenshot('transaction_consultation')
        #断言
        self.assertIsNotNone(title)


    def test_payment_record(self):
        """交易记录-回款记录验证"""

        entry_page = Entry_page(self.driver,phone="14454839876",pwd="qwe123")
        mytradeRecordPage = entry_page.open_my_tradeRecord_page()

        mytradeRecordPage.el_trade_list_image.click()
        trade_list_dict=mytradeRecordPage.logic_get_trade_list()

        sql = Exce_SQLserver()
        data_trade_list = sql.execSql_getList("SELECT top 1 new_product_name,new_payamount,new_paydate,new_paymentstatus,new_paymentno,new_txtinvestapply FROM new_tradedetailBase  WHERE new_account ='6B5A5084-9C49-E711-80D3-00155D02B414'")

        entry_page.saveScreenshot("payment_record")

        #断言理财名称
        self.assertIn(trade_list_dict['name'],data_trade_list[0][0])
        #断言金额
        self.assertIn(str(data_trade_list[0][1])[:-6]+","+str(data_trade_list[0][1])[-6:],trade_list_dict['amount'])
        #断言时间
        self.assertIn((data_trade_list[0][2].date().strftime("%Y-%m-%d")),trade_list_dict['data'])
        #断言交易流水
        self.assertEquals(trade_list_dict['flowing'],data_trade_list[0][4])
        #断言理财状态
        self.assertEquals(data_trade_list[0][3],100000003)
        #断言合同编号
        self.assertEquals(trade_list_dict['contract_no'],data_trade_list[0][5])

    def test_Continued_investment(self):
        """交易记录-续投记录验证"""

        entry_page = Entry_page(self.driver, phone="14404414441", pwd="qwe123")
        mytradeRecordPage = entry_page.open_my_tradeRecord_page()

        mytradeRecordPage.el_trade_list_image.click()
        trade_list_dict = mytradeRecordPage.logic_get_reinvest_way()


        sql = Exce_SQLserver()
        data_trade_list = sql.execSql_getList("SELECT top 10 new_renewmethod,new_expectprofit,new_newcontractno FROM new_renewapplyBase WHERE new_customer ='47A24DAD-E65A-E711-80C9-00155D01F903'")

        entry_page.saveScreenshot("Continued_investment")

        #断言续投方式
        self.assertEquals(data_trade_list[0][0],100000001)
        self.assertEquals(trade_list_dict['reinvest_way'],"本金续投")
        #断言预期收益
        self.assertIn(str(data_trade_list[0][1])[:5],trade_list_dict['expect_incomeself'])
        #断言续投编号
        self.assertEquals(trade_list_dict['el_reinvest_contract_no'],data_trade_list[0][2])





    def tearDown(self):
        self.driver.quit()

        "14454839876 qwe123  回款成功"
        "14454635718 qwe123  回款成功"
        "14404414441 qwe123 续投记录"
        "SELECT top 1 * FROM AccountBase WHERE  new_telephone1=14454839876"

if __name__ == '__main__':
    Init()
    unittest.main(verbosity=2)
