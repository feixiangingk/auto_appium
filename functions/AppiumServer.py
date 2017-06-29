#coding=utf-8

import os
import urllib
from urllib2 import  URLError
from multiprocessing import Process
from appium_init import *
import threading


class AppiumServer:

    def __init__(self):
        # global appium_command, baseUrl
        # appium_command ='node "D:\\phone\\Appium\\node_modules\\appium\\bin\\appium.js"'
        self.appium_command=appium_init.inital.appium_command
       # print(self.appium_command)

        #openAppium = readConfigLocal.getcmdValue("openAppium")

        self.baseUrl="http://0.0.0.0:4723/wd/hub"
        #baseUrl = readConfigLocal.getConfigValue("baseUrl")

    def start_server(self):
        """start the appium server
        :return:
        """
        t1 = RunServer(self.appium_command)
        # print (self.appium_path)
        p = Process(target=t1.start())
        p.start()

    def stop_server(self):
        """stop the appium server
        :return:
        """
        # kill myServer
       # os.popen('pkill node')
        os.system('taskkill /f /im node.exe')

    def re_start_server(self):
        """reStart the appium server
        """
        self.stop_server()
        self.start_server()

    def is_runnnig(self):
        """Determine whether server is running
        :return:True or False
        """
        response = None
        url = self.baseUrl+"/status"
        try:
            response = urllib.urlopen(url, timeout=5)

            if str(response.getcode()).startswith("2"):
                return True
            else:
                return False
        except URLError:
            return False
        finally:
            if response:
                response.close()


class RunServer(threading.Thread):

    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd

    def run(self):
       # print  self.cmd
        os.system(self.cmd)


if __name__ == "__main__":

    oo = AppiumServer()
    oo.stop_server()
    import  time
    time.sleep(3)
    oo.start_server()
    print("strart server")
    print("running server")
    oo.stop_server()
    print("stop server")
