公共方法调用规范
1.只在程序启动时，实例化一次Init()；后面在调用时就用实例化好的对象，例子：
from functions.appium_init import *
if isinstance(appium_init.inital,Initialization)!=True:
    Init()

入口操作都封装在全局对象appium_init.inital中。
appium_init.inital包含的方法：
get_project_path(self)
get_desired_caps(self)
get_cases_info(self, case_ini)
get_driver(self)