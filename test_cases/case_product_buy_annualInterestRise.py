#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from pages.converged_page import ConvergedPage

class ProductBuyAnnualInterestRise(InterfaceCase):
    '''购买年年生利测试用例集'''

    def setUp(self):
        self.drvier=self.inital.get_driver()
        self.logger=self.inital.logger



    # @unittest.skip('skip')
    def test_buy_annualInterestRise(self):
        '''购买年年生利用例'''
        user_phone=self.inital.excel_info['annualInterestRise']['phone']
        pwd=self.inital.excel_info['annualInterestRise']['pwd']
        amount=self.inital.excel_info['annualInterestRise']['amount']

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        time.sleep(1)
        productListPage.swipe_to_up()
        productAnnualInterestRisePage = productListPage.logic_link_annualInterestRise()
        buyInsertMoneyPage=productAnnualInterestRisePage.logic_link_buy()


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

        buyTradeResultPage.saveScreenshot('test_buy_annualInterestRise')
        self.assertEqual(int(amount), sql_amount)
        self.logger.info("run case:ProductBuyAnnualInterestRise.test_buy_annualInterestRise user_phone is %s,product_name is %s" %(user_phone,sql_product_name))
        self.assertEqual("年年生利*360天", sql_product_name)



    def tearDown(self):
        self.drvier.quit()

if __name__=="__main__":
    Init()
    unittest.main()