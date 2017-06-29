#coding:utf-8
import sys,unittest
sys.path.append("..")
from functions.interface_case import InterfaceCase
from pages.converged_page import ConvergedPage

class RegisterBankCard(InterfaceCase):
    '''绑卡相关测试集'''

    def setUp(self):
        self.logger=self.inital.logger
        self.driver=self.inital.get_driver()

    @unittest.skip('skip')
    def test_register_JS(self):
        '''绑定建行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('JS')
        self.logger.info('run case:RegisterBankCard.test_register_JS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国建设银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_JS')


    @unittest.skip('skip')
    def test_register_GF(self):
        '''绑定广发卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('GF')
        self.logger.info('run case:RegisterBankCard.test_register_GF user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"广发银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_GF')

    @unittest.skip('skip')
    def test_register_JT(self):
        '''绑定交通卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('JT')
        self.logger.info('run case:RegisterBankCard.test_register_JT user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"交通银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_JT')

    @unittest.skip('skip')
    def test_register_PA(self):
        '''绑定平安银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('PA')
        self.logger.info('run case:RegisterBankCard.test_register_PA user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"平安银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_PA')

    @unittest.skip('skip')
    def test_register_ZS(self):
        '''绑定招商银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZS')
        self.logger.info('run case:RegisterBankCard.test_register_ZS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"招商银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZS')

    @unittest.skip('skip')
    def test_register_ZX(self):
        '''绑定中信银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZX')
        self.logger.info('run case:RegisterBankCard.test_register_ZX user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中信银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZX')

    @unittest.skip('skip')
    def test_register_ZG(self):
        '''绑定中国银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('ZG')
        self.logger.info('run case:RegisterBankCard.test_register_ZG user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_ZG')

    @unittest.skip('skip')
    def test_register_NY(self):
        '''绑定中国农业银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('NY')
        self.logger.info('run case:RegisterBankCard.test_register_NY user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国农业银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_NY')

    def test_register_MS(self):
        '''绑定中国民生银行卡测试用例'''
        convergedPage=ConvergedPage(self.driver)
        myBankCardPage,user_card=convergedPage.register_bankcard('MS')
        self.logger.info('run case:RegisterBankCard.test_register_MS user_card is %s'%user_card)
        self.assertEqual(myBankCardPage.el_bankName_listOne.text,"中国民生银行")
        self.assertEqual(myBankCardPage.el_bankWeihao_listOne.text[-5:-1],user_card[-4:])
        myBankCardPage.saveScreenshot('test_register_MS')

    def tearDown(self):
        self.driver.quit()