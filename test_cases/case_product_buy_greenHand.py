#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver
from pages.converged_page import ConvergedPage

class ProductBuyGreenHand(InterfaceCase):
    '''购买新手体验测试用例集'''

    def setUp(self):
        self.drvier=self.inital.get_driver()
        self.logger=self.inital.logger



    # @unittest.skip('skip')
    def test_buy_GreenHand_fristtime(self):
        '''购买新手体验计划测试用例'''
        convergedPage=ConvergedPage(self.drvier)
        (user_phone,pwd)=convergedPage.register_customer()

        amount='100000'

        self.drvier=appium_init.inital.get_driver()
        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()

        productGreenHandPage = productListPage.logic_link_greenHand()
        buyInsertMoneyPage=productGreenHandPage.logic_link_buy()


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

        buyTradeResultPage.saveScreenshot('test_buy_GreenHand_fristtime')
        self.assertEqual(int(amount), sql_amount)

        self.logger.info("run case:test_buy_GreenHand_fristtime user_phone is %s,product_name is %s" %(user_phone,sql_product_name))
        self.assertEqual("新手体验计划*12天", sql_product_name)

    def test_buy_greenHand_secondtime(self):
        '''已经有理财记录的账号，再次购买新手标测试用例'''
        user_phone=self.inital.excel_info['quarkZX90']['phone']
        pwd=self.inital.excel_info['quarkZX90']['pwd']
        amount='100000'

        startupPage = StartupPage(self.drvier)
        homePage = startupPage.page_swipe()
        loginPage = homePage.logic_link_login_page()
        homePage = loginPage.logic_login(user_phone, pwd)
        # 点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage = homePage.logic_link_product()
        time.sleep(3)
        productListPage.swipe_to_up()
        productGreenHandPage = productListPage.logic_link_greenHand()
        # productGreenHandPage.get_screenshot_by_element(productGreenHandPage,'el_buy_btn',False)
        result=productGreenHandPage.get_screenshot_by_element(productGreenHandPage,'el_buy_btn').same_as(30)
        productGreenHandPage.saveScreenshot('test_buy_greenHand_secondtime')
        self.logger.info(
            "run case:test_buy_greenHand_secondtime user_phone is %s" %user_phone)
        self.assertEqual(result,True)


    def tearDown(self):
        self.drvier.quit()

if __name__=="__main__":
    Init()
    unittest.main()