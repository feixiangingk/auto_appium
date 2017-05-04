# coding:utf-8
import requests, json, re
from appium_init import *


# from selenium import webdriver
class Message():
    """docstring for ClassName"""

    def __init__(self):
        self.s = requests.session()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                        'Accept-Encoding': 'gzip, deflate',
                        'Connection': 'keep-alive',
                        'Content-Type': 'application/x-www-form-urlencoded'}

    def get_message(self, phone, sms_login_url, sms_serach_url):
        login_data = {'username': 'sms_test', 'password': 'sms_test'}
        response = self.s.post(sms_login_url, headers=self.headers, params=login_data)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
                   'Accept': 'application/json, text/javascript, */*; q=0.01',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Accept-Encoding': 'gzip, deflate',
                   'Connection': 'keep-alive',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}

        search_data = "phoneNumber=" + str(
            phone) + "&deptType=&besId=&status=&beginDate=&endDate=&besType=&content=&page=1&rows=10"
        response = self.s.post(sms_serach_url, headers=headers, data=search_data)
        content = response.json()['rows'][0]['content'].encode("utf-8")
        r = ur'\xe3\x80\x90(\d{6})\xe3\x80\x91'
        # r=r'(.*)'
        msg = re.findall(r, content)
        return msg[0]

    def get_sms(self,phone):
        interface=appium_init.inital.get_cases_info('interface')
        sms_login_url=interface['sms_login_url']
        sms_serach_url=interface['sms_serach_url']
        print sms_login_url,sms_serach_url

        return self.get_message(str(phone),sms_login_url,sms_serach_url)



if __name__ == '__main__':
    if isinstance(appium_init.inital,Initialization)!=True:
        Init()
    sms=Message()
    print sms.get_sms('19908888801')