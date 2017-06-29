#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from functions.BasePage import BasePage

class ProductBuyQuarkZX(InterfaceCase):
    '''购买夸客尊享理财产品测试用例集'''

    def setUp(self):
        self.drvier=self.inital.get_driver()
        self.logger=self.inital.logger

    @unittest.skip('skip')
    def test_buy_quarkZX90(self):
        '''购买夸客尊享90天测试用例'''
        user_phone=self.inital.excel_info['quarkZX90']['phone']
        pwd=self.inital.excel_info['quarkZX90']['pwd']
        amount=self.inital.excel_info['quarkZX90']['amount']

        startupPage=StartupPage(self.drvier)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,pwd)
        #点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(3)
        buyInsertMoneyPage=productQuarkzxPage.logic_link_buy()

        buyConfirmPage=buyInsertMoneyPage.logic_buy_product(amount)
        buyTradeResultPage=buyConfirmPage.logic_confirm_info(pwd)
        time.sleep(20)
        homePage=buyTradeResultPage.logic_link_buy()
        myPage=homePage.logic_buy_my_btn()

        #数据库断言，查询投资记录最新的记录根据金额判断
        SQL="select top(1) m.new_managemoney,m.new_product_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" %(user_phone)
        sql_conn=Exce_SQLserver()

        sql_result = sql_conn.execSql_getOne(SQL)
        sql_amount = int(sql_result[0])
        sql_product_name = str(sql_result[1])

        self.basepage = BasePage(self.drvier)
        self.basepage.saveScreenshot('buy_quarkZX90')
        self.assertEqual(int(amount),sql_amount)
        self.assertEqual("夸客尊享*90天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX90")


    @unittest.skip('skip')
    def test_buy_quarkZX30(self):
        '''购买夸客尊享30天测试用例'''
        user_phone=self.inital.excel_info['quarkZX30']['phone']
        pwd=self.inital.excel_info['quarkZX30']['pwd']
        amount=self.inital.excel_info['quarkZX30']['amount']

        startupPage=StartupPage(self.drvier)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,pwd)
        #点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(1)

        buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

        buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
        buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
        time.sleep(20)
        homePage = buyTradeResultPage.logic_link_buy()
        myPage = homePage.logic_buy_my_btn()

        # 数据库断言，查询投资记录最新的记录根据金额判断
        SQL = "select top(1) m.new_managemoney,m.new_product_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
        user_phone)
        sql_conn = Exce_SQLserver()

        sql_result = sql_conn.execSql_getOne(SQL)
        sql_amount = int(sql_result[0])
        sql_product_name = str(sql_result[1])

        buyTradeResultPage.saveScreenshot('buy_quarkZX30')
        self.assertEqual(int(amount),sql_amount)
        self.assertEqual("夸客尊享*30天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX30")

    @unittest.skip('skip')
    def test_buy_quarkZX60(self):
        '''购买夸客尊享60天测试用例'''
        user_phone = self.inital.excel_info['quarkZX60']['phone']
        pwd = self.inital.excel_info['quarkZX60']['pwd']
        amount = self.inital.excel_info['quarkZX60']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productQuarkzxPage = productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(2)

        buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

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

        buyTradeResultPage.saveScreenshot('buy_quarkZX60')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("夸客尊享*60天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX60")

    @unittest.skip('skip')
    def test_buy_quarkZX180(self):
        '''购买夸客尊享180天测试用例'''
        user_phone = self.inital.excel_info['quarkZX180']['phone']
        pwd = self.inital.excel_info['quarkZX180']['pwd']
        amount = self.inital.excel_info['quarkZX180']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productQuarkzxPage = productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(4)

        buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

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

        buyTradeResultPage.saveScreenshot('buy_quarkZX180')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("夸客尊享*180天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX180")

    @unittest.skip('skip')
    def test_buy_quarkZX360(self):
        '''购买夸客尊享360天测试用例'''
        user_phone = self.inital.excel_info['quarkZX360']['phone']
        pwd = self.inital.excel_info['quarkZX360']['pwd']
        amount = self.inital.excel_info['quarkZX360']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productQuarkzxPage = productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(5)

        buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

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

        buyTradeResultPage.saveScreenshot('buy_quarkZX360')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("夸客尊享*360天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX360")

    # @unittest.skip('skip')
    def test_buy_quarkZX720(self):
        '''购买夸客尊享720天测试用例'''
        user_phone = self.inital.excel_info['quarkZX720']['phone']
        pwd = self.inital.excel_info['quarkZX720']['pwd']
        amount = self.inital.excel_info['quarkZX720']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        productQuarkzxPage = productListPage.logic_link_quarkZX()
        productQuarkzxPage.logic_choose_product_type(6)

        buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

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

        buyTradeResultPage.saveScreenshot('buy_quarkZX720')
        self.assertEqual(int(amount), sql_amount)
        self.assertEqual("夸客尊享*720天",sql_product_name)
        self.logger.info("run case:test_buy_quarkZX720")



    def tearDown(self):
        self.drvier.quit()

if __name__=="__main__":
    Init()
    unittest.main()