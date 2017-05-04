#coding:utf-8
from pages.base_page import BasePage
from pages.home_page import HomePage
from appium.webdriver.common.touch_action import TouchAction
import  time

class StartupPage(BasePage):

    def swipLeft(self):
        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        start_x=int(x*0.8)
        end_x=int(x*0.2)
        start_y=int(y*0.5)
        end_y=int(y*0.5)
        for i in xrange(3):
            self.driver.swipe(start_x,start_y,end_x,end_y)
            time.sleep(1)
        TouchAction(self.driver).press(x=377,y=1048).wait(100).release().perform()
        time.sleep(1)
        return HomePage(self.driver)


