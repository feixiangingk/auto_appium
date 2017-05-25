#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from functions.appium_init import *
from pages.startup_page import StartupPage
from functions.sqlServerJDBC import Exce_SQLserver

class ProductBuyTest(InterfaceCase):
    '''购买理财产品测试用例集'''

    def setUp(self):
        self.drvier=self.inital.get_driver()
        self.logger=self.inital.logger

    def test_buy_quarkZX(self):
        '''购买夸客尊享测试用例'''
        user_phone='14488888098'
        pwd='qwe123'
        amount=51000
        startupPage=StartupPage(self.drvier)
        homePage=startupPage.page_swipe()
        loginPage=homePage.logic_link_login_page()
        homePage=loginPage.logic_login(user_phone,pwd)
        #点击一次理财产品元素，过滤蒙层
        homePage.el_product_btn.click()
        time.sleep(0.5)
        productListPage=homePage.logic_link_product()
        productQuarkzxPage=productListPage.logic_link_quarkZX()
        buyInsertMoneyPage=productQuarkzxPage.logic_link_buy()

        buyConfirmPage=buyInsertMoneyPage.logic_buy_product(amount)
        buyTradeResultPage=buyConfirmPage.logic_confirm_info(pwd)
        time.sleep(10)
        homePage=buyTradeResultPage.logic_link_buy()
        myPage=homePage.logic_buy_my_btn()

        #数据库断言，查询投资记录最新的记录根据金额判断
        SQL="select top(1) m.new_managemoney from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1='14488888098' ORDER BY m.CreatedOn DESC"
        sql_conn=Exce_SQLserver()
        sql_amount=int(sql_conn.execSql_getOne(SQL)[0])

        self.assertEqual(int(amount),sql_amount)


        #点击浮层“我知道了”按钮
        # myPage.el_tv_know.click()
        # myTradeRecordPage=myPage.logic_my_transactionRecord_btn_click()
        #
        # myTradeRecordPage.el_tv_know.click()

    def tearDown(self):
        self.drvier.quit()

if __name__=="__main__":
    Init()
    unittest.main()