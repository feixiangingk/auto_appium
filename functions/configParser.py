#coding:utf-8
import configparser,codecs

class Config():
	"""
	读取配置文件类，主要使用get_config方法
	"""

	def __init__(self):
		self.config=configparser.ConfigParser()

#根据section，path读取配置文件信息，以字典的格式返回
	def get_config(self,section,path):
		self.config.readfp(codecs.open(path,'r','utf-8-sig'))
		values=self.config.options(section)
		parameter_dict={}
		for i in values:
			parameter_dict[i]=self.config.get(section, i)
		return parameter_dict


if __name__ == '__main__':
	config=Config()
	path="D:\\quarkscript\\auto_appium\\config\\appium_config.ini"
	parameter_dict=config.get_config('desired_caps', path)
	print parameter_dict