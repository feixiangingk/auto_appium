#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.BasePage import BasePage

class ProductBuyMonthlyInterest(InterfaceCase):
    '''购买月月付息测试用例集'''

    def setUp(self):
        self.drvier=self.inital.get_driver()
        self.logger=self.inital.logger



    # @unittest.skip('skip')
    def test_buy_monthly_interest180(self):
        '''购买月月付息180天测试用例'''
        user_phone = self.inital.excel_info['monthly_interest180']['phone']
        pwd = self.inital.excel_info['monthly_interest180']['pwd']
        amount = self.inital.excel_info['monthly_interest180']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productMonthlyInterestPage = productListPage.logic_link_monthly_interest()
        productMonthlyInterestPage.logic_choose_product_type(3)

        buyInsertMoneyPage = productMonthlyInterestPage.logic_link_buy()

        buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
        buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
        time.sleep(20)
        homePage = buyTradeResultPage.logic_link_buy()
        myPage = homePage.logic_buy_my_btn()

        # 数据库断言，查询投资记录最新的记录根据金额判断
        SQL = "select top(1) m.new_managemoney,m.new_product_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
            user_phone)
        sql_conn = Exce_SQLserver()

        sql_result=sql_conn.execSql_getOne(SQL)
        sql_amount = int(sql_result[0])
        sql_product_name=str(sql_result[1])

        buyTradeResultPage.saveScreenshot('test_buy_monthly_interest180')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("月月付息*180天",sql_product_name)
        self.logger.info("run case:ProductBuyMonthlyInterest.test_buy_monthly_interest180")



    # @unittest.skip('skip')
    def test_buy_monthly_interest360(self):
        '''购买月月付息360天测试用例'''
        user_phone = self.inital.excel_info['monthly_interest360']['phone']
        pwd = self.inital.excel_info['monthly_interest360']['pwd']
        amount = self.inital.excel_info['monthly_interest360']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productMonthlyInterestPage = productListPage.logic_link_monthly_interest()
        productMonthlyInterestPage.logic_choose_product_type(4)

        buyInsertMoneyPage = productMonthlyInterestPage.logic_link_buy()

        buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
        buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
        time.sleep(20)
        homePage = buyTradeResultPage.logic_link_buy()
        myPage = homePage.logic_buy_my_btn()

        # 数据库断言，查询投资记录最新的记录根据金额判断
        SQL = "select top(1) m.new_managemoney,m.new_product_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
            user_phone)
        sql_conn = Exce_SQLserver()

        sql_result=sql_conn.execSql_getOne(SQL)
        sql_amount = int(sql_result[0])
        sql_product_name=str(sql_result[1])


        buyTradeResultPage.saveScreenshot('test_buy_monthly_interest360')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("月月付息*360天",sql_product_name)
        self.logger.info("run case:ProductBuyMonthlyInterest.test_buy_monthly_interest360")


    def tearDown(self):
        self.drvier.quit()

if __name__=="__main__":
    Init()
    unittest.main()