#coding:utf-8
import unittest,sys
sys.path.append('..')
from appium_init import *


class LoadCase():

	@staticmethod
	def get_cases(case_ini='testcase'):
		testSuite=unittest.TestSuite()
		loader=unittest.defaultTestLoader
		# info=Initialization()
		inital=appium_init.inital

		cases_info=inital.get_cases_info(case_ini)
		# print cases_info.get('case_discover')
		if cases_info=={}:
			inital.logger.info('get_cases | plz check appium_config.ini')
			return None

		#全选按钮打开，获取所有用例
		elif cases_info.get('load_all') in ['Y','y','*']:
			cases_list=loader.discover(cases_info.get('cases_path'),pattern='*.py')
			for module in cases_list:
				testSuite.addTests(module)

			inital.logger.info("get_cases | load all cases!")
			return  testSuite


		elif cases_info.get('case_module')==None and cases_info.get('case_discover')==None:
			print('cases_list is null,plz input cases in appium_config.ini')
			return None

		elif cases_info.get('case_module')!=None:
			modules=cases_info.get('case_module').split(',')
			for module in modules:
				if module.startswith('#')==False:
					module='test_cases.'+module
					cases_list=loader.loadTestsFromModule(__import__(module,fromlist=True))

					testSuite.addTests(cases_list)

		if cases_info.get('case_discover')!=None:
			if  ',' not in cases_info.get('case_discover'):
				discover_list=[]
				discover_list.append(cases_info.get('case_discover'))
			else:
				discover_list=cases_info.get('case_discover').split(',')
			for discover in discover_list:
				if discover.startswith('#')==False:
					cases_list = loader.discover(cases_info.get('cases_path'), pattern=discover)
					for module in cases_list:
						testSuite.addTests(module)

		cases=testSuite.countTestCases()
		inital.logger.info('get_cases | load case number is %d' %cases)
		return testSuite


if __name__ == '__main__':
	Init()
	testSuite= LoadCase.get_cases()
	if testSuite!=None:
		runner=unittest.TextTestRunner()
		runner.run(testSuite)



