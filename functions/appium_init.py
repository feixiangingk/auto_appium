# coding:utf-8
import os,sys,time
sys.path.append('..')
from appium import webdriver
from configParser import Config
from functions.appium_logging import AppLog
from functions.adbConnon import AndroidDebugBridge
import appium_init

inital=None

class Initialization():
    """
    只在程序启动时，实例化一次Init()；后面在调用时就用实例化好的对象
    口操作都封装在全局对象appium_init.inital中
    """


    def __init__(self):

        self.config=Config()

        #唯一需要配置路径的地方，路径为配置文件绝对路径
        self.config_path="D:\\quarkscript\\UFO_appium\\config\\appium_config.ini"

        #读取配置文件中desired_caps信息，作为initial的属性保存
        self.desired_caps=self.config.get_config(
            'desired_caps', self.config_path)

        #读取配置文件中project_path信息，作为initial的属性保存
        self.project_path=self.desired_caps['project_path']

        #将常用配置信息，日志类、ADB调用类、手机系统监控类（待扩展）的实例作为属性绑定在inital中，这些常用类避免反复实例化浪费内存影响效率
        appLog = AppLog(self.project_path)
        self.logger = appLog.logger
        self.adbCall = AndroidDebugBridge()
        self.logger.info('Initialization | config_path is %s init is complate!' %
                         self.config_path)


    def get_cases_info(self, case_ini):

        cases_info = self.config.get_config(case_ini, self.config_path)
        if cases_info != []:
            return cases_info
        else:
            self.logger.info(
                "Initialization | config is Null! plz check information!")

    def get_driver(self):
        """

        :return: driver
        """
        # 通过adb判断设备是否启动
        if self.adbCall.attached_devices():
            # desired_caps_config = self.get_desired_caps()
            desired_caps = {}
            desired_caps['platformName'] = self.desired_caps['platformname']
            desired_caps['platformVersion'] = self.desired_caps[
                'platformversion']
            desired_caps['deviceName'] = self.desired_caps['devicename']
            desired_caps['appPackage'] = self.desired_caps['apppackage']
            desired_caps['appActivity'] = self.desired_caps['appactivity']

            time.sleep(1)
            # driver 实例化前，调用adb命令卸载和重新安装应用,保证每次测试用例执行的环境都是干净的
            self.adbCall.call_adb('uninstall ' + desired_caps['appPackage'])
            time.sleep(1)
            self.adbCall.call_adb(
                'install ' + self.project_path + "\\app\\" + self.desired_caps['app_name'])
            time.sleep(1)
            # print desired_caps.items()
            driver = webdriver.Remote(
                'http://localhost:4723/wd/hub', desired_caps)

            return driver

        else:
            self.logger.info('Initialization | 设备不存在 ')


#初始化类，执行以后inital成为Initialization的实例，供框架各处调用
class Init():
    def __init__(self):
        appium_init.inital=Initialization()


if __name__ == '__main__':
    if isinstance(appium_init.inital,Initialization)!=True:
        Init()
    print appium_init.inital.desired_caps


