#coding:utf-8
from appium import  webdriver

class BasePage():

    def __init__(self,driver):
        self.driver=driver

    def title(self):
        return self.driver.title

    def url(self):
        return self.driver.current_url

    def by_name(self,name):
        return self.driver.find_element_by_name(name)

    def by_id(self,id):
        return self.driver.find_element_by_name(id)


