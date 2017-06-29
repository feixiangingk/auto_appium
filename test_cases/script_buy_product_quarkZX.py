#coding:utf-8
import sys,unittest,time
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.converged_page import ConvergedPage
from functions.sqlServerJDBC import Exce_SQLserver


class BuyProductScriptQuarkZX(InterfaceCase):

    def setUp(self):
        self.logger=self.inital.logger

    # @unittest.skip('skip')
    def test_buy_quarkZX30(self):
        '''购买夸客尊享30天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX30']['phone']
        pwd = self.inital.buyProduct_info['quarkZX30']['pwd']
        amount = self.inital.buyProduct_info['quarkZX30']['amount']
        times = self.inital.buyProduct_info['quarkZX30']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX30']['exec']
        load_create = self.inital.buyProduct_info['quarkZX30']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX30: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX30: do not buy product quarkZX30!')
            return "do not buy product quarkZX30!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX30: user_phone pwd value can not be null!")
            return  "BuyProductScript.test_buy_quarkZX30: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
                homePage = startupPage.page_swipe()
                loginPage = homePage.logic_link_login_page()
                homePage = loginPage.logic_login(user_phone, pwd)
                # 点击一次理财产品元素，过滤蒙层
                homePage.el_product_btn.click()
                time.sleep(0.5)
                productListPage = homePage.logic_link_product()
                productQuarkzxPage = productListPage.logic_link_quarkZX()
                productQuarkzxPage.logic_choose_product_type(1)

                buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

                buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
                buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
                time.sleep(20)
                homePage = buyTradeResultPage.logic_link_buy()
                myPage = homePage.logic_buy_my_btn()
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])

                self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX30:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX30 failed!"+str(e))
            finally:
                self.driver.quit()

    # @unittest.skip('skip')
    def test_buy_quarkZX60(self):
        '''购买夸客尊享60天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX60']['phone']
        pwd = self.inital.buyProduct_info['quarkZX60']['pwd']
        amount = self.inital.buyProduct_info['quarkZX60']['amount']
        times = self.inital.buyProduct_info['quarkZX60']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX60']['exec']
        load_create = self.inital.buyProduct_info['quarkZX60']['load_create']

        if amount == "" or times == "" or exec_flag == "" or load_create == "":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX60: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag == 'N' or times == '0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX60: do not buy product quarkZX60!')
            return "do not buy product quarkZX60!"

        if load_create == 'N':
            self.driver = self.inital.get_driver()
            convergedPage = ConvergedPage(self.driver)
            user_phone, pwd = convergedPage.register_customer()

        elif load_create == "Y" and (user_phone == "" or pwd == ""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX60: user_phone pwd value can not be null!")
            return "BuyProductScriptQuarkZX.test_buy_quarkZX60: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
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
                SQL = "select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])
                self.assertIsNot(sql_productNo, "", None)
                self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX60:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i + 1), two=user_phone, three=pwd,
                                                           four=sql_productNo, five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX60 failed!" + str(e))
            finally:
                self.driver.quit()


    # @unittest.skip('skip')
    def test_buy_quarkZX90(self):
        '''购买夸客尊享90天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX90']['phone']
        pwd = self.inital.buyProduct_info['quarkZX90']['pwd']
        amount = self.inital.buyProduct_info['quarkZX90']['amount']
        times = self.inital.buyProduct_info['quarkZX90']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX90']['exec']
        load_create = self.inital.buyProduct_info['quarkZX90']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX90: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX90: do not buy product quarkZX90!')
            return "do not buy product quarkZX90!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX90: user_phone pwd value can not be null!")
            return  "BuyProductScriptQuarkZX.test_buy_quarkZX90: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
                homePage = startupPage.page_swipe()
                loginPage = homePage.logic_link_login_page()
                homePage = loginPage.logic_login(user_phone, pwd)
                # 点击一次理财产品元素，过滤蒙层
                homePage.el_product_btn.click()
                time.sleep(0.5)
                productListPage = homePage.logic_link_product()
                productQuarkzxPage = productListPage.logic_link_quarkZX()
                productQuarkzxPage.logic_choose_product_type(3)

                buyInsertMoneyPage = productQuarkzxPage.logic_link_buy()

                buyConfirmPage = buyInsertMoneyPage.logic_buy_product(amount)
                buyTradeResultPage = buyConfirmPage.logic_confirm_info(pwd)
                time.sleep(20)
                homePage = buyTradeResultPage.logic_link_buy()
                myPage = homePage.logic_buy_my_btn()
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])
                self.assertIsNot(sql_productNo, "", None)
                self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX90:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX90 failed!" + str(e))
            finally:
                self.driver.quit()

    # @unittest.skip('skip')
    def test_buy_quarkZX180(self):
        '''购买夸客尊享180天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX180']['phone']
        pwd = self.inital.buyProduct_info['quarkZX180']['pwd']
        amount = self.inital.buyProduct_info['quarkZX180']['amount']
        times = self.inital.buyProduct_info['quarkZX180']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX180']['exec']
        load_create = self.inital.buyProduct_info['quarkZX180']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX180: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX180: do not buy product quarkZX180!')
            return "do not buy product quarkZX180!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX180: user_phone pwd value can not be null!")
            return  "BuyProductScriptQuarkZX.test_buy_quarkZX180: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
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
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])
                self.assertIsNot(sql_productNo, "", None)
                self.logger.info("BuyProductScript.test_buy_quarkZX180:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX180 failed!" + str(e))
            finally:
                self.driver.quit()

    # @unittest.skip('skip')
    def test_buy_quarkZX360(self):
        '''购买夸客尊享360天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX360']['phone']
        pwd = self.inital.buyProduct_info['quarkZX360']['pwd']
        amount = self.inital.buyProduct_info['quarkZX360']['amount']
        times = self.inital.buyProduct_info['quarkZX360']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX360']['exec']
        load_create = self.inital.buyProduct_info['quarkZX360']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX360: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX360: do not buy product quarkZX360!')
            return "do not buy product quarkZX360!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX360: user_phone pwd value can not be null!")
            return  "BuyProductScriptQuarkZX.test_buy_quarkZX360: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
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
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])
                self.assertIsNot(sql_productNo, "", None)
                self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX360:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX360 failed!" + str(e))
            finally:
                self.driver.quit()

    # @unittest.skip('skip')
    def test_buy_quarkZX720(self):
        '''购买夸客尊享720天脚本，和buy_prodouct_info.xls数据源对应'''

        user_phone = self.inital.buyProduct_info['quarkZX720']['phone']
        pwd = self.inital.buyProduct_info['quarkZX720']['pwd']
        amount = self.inital.buyProduct_info['quarkZX720']['amount']
        times = self.inital.buyProduct_info['quarkZX720']['times']
        exec_flag = self.inital.buyProduct_info['quarkZX720']['exec']
        load_create = self.inital.buyProduct_info['quarkZX720']['load_create']

        if amount=="" or times=="" or exec_flag=="" or load_create=="":
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX720: buy_info excel parms is wrong!")
            return "buy_info excel parms is wrong!"


        elif exec_flag=='N' or times=='0':
            self.logger.info('BuyProductScriptQuarkZX.test_buy_quarkZX720: do not buy product quarkZX720!')
            return "do not buy product quarkZX720!"

        if load_create=='N':
            self.driver = self.inital.get_driver()
            convergedPage=ConvergedPage(self.driver)
            user_phone,pwd=convergedPage.register_customer()

        elif load_create=="Y" and (user_phone=="" or pwd==""):
            self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX720: user_phone pwd value can not be null!")
            return  "BuyProductScriptQuarkZX.test_buy_quarkZX720: user_phone pwd value can not be null!"

        for i in xrange(int(times)):
            try:
                self.driver = self.inital.get_driver()
                startupPage = StartupPage(self.driver)
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
                SQL="select top(1) m.new_managemoney,m.new_name from dbo.Account t,dbo.new_investdetail m where t.name=m.new_accountnameName and t.new_telephone1=%s ORDER BY m.CreatedOn DESC" % (
                    user_phone)
                sql_conn = Exce_SQLserver()

                sql_result = sql_conn.execSql_getOne(SQL)
                sql_amount = int(sql_result[0])
                sql_productNo = str(sql_result[1])
                self.assertIsNot(sql_productNo, "", None)
                self.logger.info("BuyProductScriptQuarkZX.test_buy_quarkZX720:run {one} time;"
                                 "phone is {two};"
                                 "pwd is {three};"
                                 "product is {four};"
                                 "amount is {five}".format(one=(i+1),two=user_phone,three=pwd,four=sql_productNo,five=sql_amount))
            except Exception as e:
                self.logger.info("buy_quarkZX720 failed!" + str(e))
            finally:
                self.driver.quit()



if __name__=="__main__":
    print range(4)