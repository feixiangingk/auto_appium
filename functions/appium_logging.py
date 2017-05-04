#coding:utf-8
import logging,os
from datetime import  datetime

class AppLog():
    '''
    日志类，只有初始化方法，启动以后将实例作为属性传给inital，供框架各处调用记录日志
    '''
    def __init__(self,project_path):
        now=datetime.now().strftime("%Y_%m_%d %H-%M-%S")
        day=datetime.now().strftime("%Y_%m_%d")
        log_path=project_path+"\\log\\"+day+"\\"


        if os.path.exists(log_path)!=True:
            os.mkdir(log_path)
        log_name=log_path+"appium "+now+".log"

        self.logger=logging.Logger('appium_logger')

        #创建写日志句柄
        fh1=logging.FileHandler(log_name)
        fh1.setLevel(logging.INFO)

        #创建控制台输出句柄
        fh2=logging.StreamHandler()
        fh2.setLevel(logging.DEBUG)

        #定义日志输出规则
        formatter=logging.Formatter('%(levelname)s| %(asctime)s |%(message)s')

        #日志句柄绑定规则
        fh1.setFormatter(formatter)
        fh2.setFormatter(formatter)

        #给logger添加句柄
        self.logger.addHandler(fh1)
        self.logger.addHandler(fh2)

if __name__=='__main__':
    log=AppLog('')





