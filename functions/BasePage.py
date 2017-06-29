#coding=utf-8
import time,os
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webelement import WebElement
from functions.appium_init import *
import sys,re,math,operator
from PIL import Image

class BasePage(object):
	"""
	封装关于Appium中操作元素对象的方法
	"""

	def __init__(self, driver,phone="14488888098",pwd="qwe123"):
		self.driver = driver
		self.logger=appium_init.inital.logger
		self.phone=phone
		self.pwd=pwd




	#根据何乐获取的方法名、方法行数对日志异常修改完善
	def base_find_element(self,locator,value):
		try:
			WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(locator,value).is_displayed())
			return self.driver.find_element(locator,value)
		except TimeoutException,e:
			self.logger.info('BasePage | TimeoutException error occur at {one};function name is {two};locator is {three} {four} Exception:{five};'.format(one=sys._getframe().f_back.f_lineno,																																				 two=sys._getframe().f_back.f_code.co_name,
																																				three=locator,four=value,five=e))
			self.saveScreenshot(sys._getframe().f_back.f_code.co_name)


	def base_find_elements(self,locator,value):

		if len(self.driver.find_elements(locator, value)):
			return self.driver.find_elements(locator, value)
		else:
			for i in xrange(15):
				time.sleep(1)
				if len(self.driver.find_elements(locator,value)):
					return self.driver.find_elements(locator,value)
			self.logger.info('BasePage | NoSuchElementException error occur at {one};function name is {two};locator is {three} {four};'.format(one=sys._getframe().f_back.f_lineno,
																																			   two=sys._getframe().f_back.f_code.co_name,
																																		   three=locator,four=value))
			self.saveScreenshot(sys._getframe().f_back.f_code.co_name)

	def get_size(self):
		"""
		获取当前屏幕的分辨率
		:return: int, x*y
		"""
		size = self.driver.get_window_size()
		return size

	def swipe_to_up(self):
		"""
		从下往上滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

	def swipe_to_down(self):
		"""
		从上往下滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

	def swipe_to_left(self):
		"""
		从右往左滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width / 8, height / 2, width * 7 / 8, height / 2, 500)

	def swipe_to_right(self):
		"""
		从左往右滑动
		:return: None
		"""
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		self.driver.swipe(width * 7 / 8, height / 2, width / 8, height / 2, 500)

	def reLoadApp(self):
		"""
		重启app
		:return:None
		"""
		self.driver.close_app()
		self.driver.launch_app()

	def longPress(self, x, y, peroid):
		"""
		长按点击操作
		:Args:
		 - x,y： 长按点的坐标
		 - peroid: 多长时间内完成该操作,单位是毫秒

		:Usage:
		 self.longPress(50, 50, 500)
		"""
		self.driver.tap([(x, y)], peroid)



	def pressBackKey(self):
		"""
		按返回键
		"""
		# code码参考Android的官网的keycode
		self.driver.keyevent(4)

	def hideKeyboard(self):
		"""
		收起键盘
		"""
		self.driver.hide_keyboard()


	def press_TouchAction(self):
		window_size = self.get_size()
		width = window_size.get("width")
		height = window_size.get("height")
		TouchAction(self.driver).press(x=int(width * 0.5), y=int(height*0.9)).release().perform()



	def waitActivity(self, activity, timeout=5):
		"""
		等待指定的Activity,5秒超时
		:param activity: 等待的Activity
		:param timeout: 超时时间
		:return:True or False
		"""
		result = self.driver.wait_activity(activity, timeout)
		return result


	# savePngName:生成图片的名称
	def savePngName(self, name):
			"""
			name：自定义图片的名称
			"""
			# 每次实例化Initalization太浪费内存，已经定义好的全局变量就是为了减少初始化类反复实例化

			tm = self.saveTime()
			day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
			type = ".png"
			fp = ".\\result\\" + day + "\\image"
			if os.path.exists(fp):
				filename = str(fp) + "\\" + str(tm) + str("_") + str(name) + str(type)
				print filename
				return filename
			else:
				os.makedirs(fp)
				filename = str(fp) + "\\" + str(tm) + str("_") + str(name) + str(type)
				print filename
				return filename

			'''
			if isinstance(appium_init.inital,Initialization)!=True:
				Init()
			inital=appium_init.inital
			day = time.strftime('%Y-%m-%d', time.localtime(time.time()))

			fp = inital.project_path+"\\result\\" + day + "\\image\\" + day

			tm = self.saveTime()
			type = ".png"
			if os.path.exists(fp):
				filename = fp + "\\" + tm + "_" + name + type
				# print filename
				# print "True"
				return filename
			else:
				os.makedirs(fp)
				filename = fp + "\\" + tm + "_" + name + type
				# print filename
				# print "False"
				return filename '''

	# 获取系统当前时间
	def saveTime(self):
			"""
			返回当前系统时间以括号中（2014-08-29-15_21_55）展示
			"""
			return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))

	# saveScreenshot:通过图片名称，进行截图保存
	def saveScreenshot(self, name):
			"""
			快照截图
			name:图片名称
			"""
			# 获取当前路径
			# print os.getcwd()
			image = self.driver.save_screenshot(self.savePngName(name))
			return image



	def get_screenshot_by_element(self, instance, function_name, isexist=True):

		'''
		
		:param instance: Page类的实例，比如  a=HomePage()传入的就是a
		:param function_name:  Page类的元素方法名，注意是字符串。eg:'el_my_btn'
		:param isexist:  截图对比图片是否存在，即断言对比的图片是否存在，默认存在，就能调用对比，如果不存在就填False，保持该元素图片，以供下次对比
		:return:  返回self  ，方便same_as()方法连续调用
		'''

		r = r".([a-z0-9A-Z]*)'>"
		class_name = re.findall(r, str(type(instance)))[0]
		if isexist == False:
			self.img_file = appium_init.inital.project_path+ "\\img\\" + class_name + "_" + function_name + ".png"
		elif isexist == True:
			self.img_file = appium_init.inital.project_path+ "\\img\\" + "temp_" + class_name + "_" + function_name + ".png"
		else:
			appium_init.inital.logger.info("Pictrue | get_screenshot_by_element : isexist value is error %s" % isexist)
			return False
		f = getattr(instance, function_name)
		element = f
		time.sleep(5)
		self.driver.get_screenshot_as_file(self.img_file)

		if isinstance(element,WebElement):
			# 获取元素bounds
			location = element.location
			size = element.size
			box = (location["x"], location["y"], location["x"] + size["width"], location["y"] + size["height"])
		else:
			appium_init.inital.logger.info("Pictrue | get_screenshot_by_element :  element is not found! locator is %s" %function_name)
			return False
		# 截取图片
		image = Image.open(self.img_file)
		newImage = image.crop(box)
		newImage.save(self.img_file)
		appium_init.inital.logger.info("Pictrue | get_screenshot_by_element:pic %s save complate!" % self.img_file)
		return self


	def same_as(self, percent=30):
		'''
		
		:param percent: 相似的百分百，0为100%相似，数值越高，对比容忍度越高，默认值为30
		:return:  返回True/False   True对比通过，False对比不通过
		'''
		try:
			image1 = Image.open(self.img_file)
			image2 = Image.open(self.img_file.replace("temp_", ""))
		except IOError,e:
			print(e)
			appium_init.inital.logger.info("Pictrue | same_as: %s" %e)
			return False

		histogram1 = image1.histogram()
		histogram2 = image2.histogram()

		differ = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2,
														 histogram1, histogram2))) / len(histogram1))
		if differ <= percent:
			return True
		else:
			return False


		#判断元素是否存在于当前页面
	def proving_element(self,el):
		"""
		:param el: 元素 
		:return: True  False
		"""
		source = self.driver.page_source
		#print  source
		if el in source:
			return True
		else:
			return False

	def element_is_exsit(self,el):
		return isinstance(el,WebElement)



class WebUI(BasePage):
	def __str__(self):
		return 'WEB UI'


class AppUI(BasePage):
	def __str__(self):
		return 'App UI'


if __name__ == '__main__':
	a=Initialization()
	d=a.get_driver()
	c=BasePage(d)
	c.saveScreenshot("test")