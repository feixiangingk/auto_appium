#coding:utf-8
from appium import webdriver
import time,unittest,sys
sys.path.append('..')
from functions.interface_case import InterfaceCase
from pages.startup_page import StartupPage
from pages.home_page import HomePage
from pages.my_page import MyPage




class A_login(InterfaceCase):
	"""docstring for A_login"""

	#类级别的setUpClass
	# @classmethod

	def setUp(self):
		# info=Initialization()
		self.logger=self.inital.logger
		self.driver=self.inital.get_driver()
		startup_page = StartupPage(self.driver)
		startup_page.swipLeft()


	def test_goto_mypage(self):

		try:
			home_page=HomePage(self.driver)
			my_page=home_page.my_page()
			self.logger.info('A_login | goto my_page !')


		except Exception, e:
			self.driver.quit()
			self.logger.info('A_login | Exception is %s' %e)


	# @unittest.skip('skip')
	def test_goto_product(self):
		try:
			self.driver.implicitly_wait(5)
			home_page = HomePage(self.driver)
			home_page.product_page()
			self.logger.info('A_login | goto product_page !')
		except Exception, e:
			self.driver.quit()
			self.logger.info('A_login | Exception is %s' %e)



	# @classmethod
	def tearDown(self):
		self.driver.quit()


if __name__ == '__main__':
	unittest.main()
	# testSuite=unittest.TestSuite()
	# loader=unittest.defaultTestLoader
    #
	# test1=loader.loadTestsFromTestCase(A_login)
	# testSuite.addTests(test1)
    #
	# runner=unittest.TextTestRunner()
	# runner.run(testSuite)