#coding:utf-8
import yagmail,os
from datetime import  datetime
from appium_init import *
from email.mime.text import MIMEText
#上传附件需要的类
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.header import Header

class SendMail(object):
    """docstring for send_mail"""


        #入参测试报告文件路径、文件模糊匹配字符串；查询文件夹，选取最新的文件，返回“文件路径+最新的文件名”
    def get_FileName(self,result_path,re_name):
        file_list=os.listdir(result_path)
        result_list=[]
        for file in file_list:
            if file.find(re_name)!=-1:
                result_list.append(file)
        reportName=sorted(result_list,key=lambda filename:(os.path.getmtime(result_path+"\\"+filename)))[-1]
        return (result_path+'\\'+reportName)


    def get_mail_body(self,report_file):
        f = open(report_file, 'rb')
        mail_body = f.read()
        f.close()
        return mail_body

    def post_mail(self,to_mail_list,resultFile,logFile,mailFile):

        mail = yagmail.SMTP(user='276476197@qq.com', password='gujttwszbatpbieh', host='smtp.qq.com', port='587')
        contents = self.get_mail_body(mailFile)
        mail.send(to=to_mail_list,subject=u'quark—UFO自动化测试报告',
                  contents=[contents,resultFile,logFile])

    def send(self):
        to_mail_list=appium_init.inital.desired_caps['to_mail_list'].split(',')
        project_path=appium_init.inital.project_path

        log_path=project_path+"\\log\\"+datetime.now().strftime("%Y_%m_%d")
        result_path=project_path+ "\\result\\" +time.strftime('%Y-%m-%d', time.localtime(time.time()))

        logFile=self.get_FileName(log_path,'log')
        resultFile=self.get_FileName(result_path,'result')
        mailFile=self.get_FileName(result_path,'send_mail')

        self.post_mail(to_mail_list,resultFile,logFile,mailFile)





if __name__ == '__main__':
    Init()
    mail=SendMail()
    mail.send()
