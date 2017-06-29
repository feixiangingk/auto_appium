#coding:utf-8
import yagmail,os
from datetime import  datetime
from appium_init import *
from email.mime.text import MIMEText
#上传附件需要的类
import smtplib
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

    def post_mail(self,to_mail_list,cc_mail_list,resultFile,logFile):

        mail_body=self.get_mail_body(resultFile)

        mail_body1=mail_body.replace( "class=\'hiddenRow\'","class=\''")

        mail_body2 = mail_body1.replace("class=\'popup_window\'", "class=\'popup_window\' style=\'display: block;\'")

        mail_body3 = mail_body2.replace("<a", "<div")

        FROMADDR = 'LeHe@quarkfinance.com'

        #调试邮件
        #TOADDR = ['LeHe@quarkfinance.com', '89605179@qq.com']
       # CCADDR = ['LeHe@quarkfinance.com', '89605179@qq.com']


        #正式邮件
        TOADDR = to_mail_list
        CCADDR=cc_mail_list

        #TOADDR=['LeHe@quarkfinance.com','FanGu@quarkfinance.com','XueLv@quarkfinance.com','V-DingLv@quarkfinance.com','V-YinzhuMing@quarkfinance.com','QingliTian@quarkfinance.com','V-LijiaoLiu@quarkfinance.com']
        # CCADDR = ['QingkangJin@quarkfinance.com', 'DaisyZhou@quarkfinance.com']


        msg = MIMEMultipart()
        msg['Subject'] = u'Quark-UFO自动化测试报告'
        msg['From'] = 'IT-测试部'
       #msg['To'] = to_mail_list
        msg['To'] = ', '.join(TOADDR)
        msg['Cc']=', '.join(CCADDR)

      # print msg['To']
        html_att = MIMEText(mail_body3, 'html', 'utf-8')

        #邮件附件html
        xlsxpart = MIMEApplication(mail_body)
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='Quark-UFO自动化测试报告.html')
        msg.attach(xlsxpart)

        #邮件附件 log
        xlsxpart = MIMEApplication(open(logFile, 'rb').read())
        xlsxpart.add_header('Content-Disposition', 'attachment', filename='Quark-UFO自动化测试日志.log')
        msg.attach(xlsxpart)
        msg.attach(html_att)


        #无账户密码，匿名发送邮件  端口25
        smtp = smtplib.SMTP()
        smtp.connect("mail.quarkfinance.com", 25)
        smtp.sendmail(FROMADDR, TOADDR + CCADDR, msg.as_string())


        #需要账户密码登录发送匿名邮件
        '''
        #smtp = smtplib.SMTP("smtp.qq.com", 587)
        smtp = smtplib.SMTP("mail.quarkfinance.com",587)
        #smtp.connect("smtp.qq.com", "587")
        smtp.starttls()
        smtp.login("quark\lehe","请输入密码")
       # smtp.sendmail(msg['From'], msg['To'].split(',') , msg.as_string())
        smtp.sendmail(FROMADDR,TOADDR + CCADDR, msg.as_string())'''


    def send(self,type):
        #to_mail_list=appium_init.inital.desired_caps['to_mail_list'].split(',')

        if type=='0':
            to_mail_list = appium_init.inital.desired_caps['to_mail_list'].split(',')
            cc_mail_list = appium_init.inital.desired_caps['cc_mail_list'].split(',')
        else:
            to_mail_list = appium_init.inital.desired_caps['tto_mail_list'].split(',')
            cc_mail_list = appium_init.inital.desired_caps['tcc_mail_list'].split(',')


        project_path=appium_init.inital.project_path
        log_path=project_path+"\\log\\"+datetime.now().strftime("%Y_%m_%d")
        result_path=project_path+ "\\result\\" +time.strftime('%Y-%m-%d', time.localtime(time.time()))

        logFile=self.get_FileName(log_path,'log')
        resultFile=self.get_FileName(result_path,'result')
       # mailFile=self.get_FileName(result_path,'send_mail')

        self.post_mail(to_mail_list,cc_mail_list,resultFile,logFile)


        #调试类
    def sendEmail1(msgTo, content, type):
        (attachment, html) = content
        msg = MIMEMultipart()
        msg['Subject'] = type
        msg['From'] = '89605179@qq.com'
        msg['To'] = msgTo
        html_att = MIMEText(html, 'html', 'utf-8')
        att = MIMEText(attachment, 'plain', 'utf-8')
        msg.attach(html_att)
        msg.attach(att)

        smtp = smtplib.SMTP()
        # smtp.connect(HOST, "587")
        smtp.connect("smtp.qq.com", "587")
        smtp.starttls()
        smtp.login("89605179@qq.com", "wtqglbdactrhbhji")
        smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())


if __name__ == '__main__':
    Init()
   # mail=SendMail()
   # mail.send(type=1)

    mail = SendMail()
    # type =0 发送正式邮件  type=1发送测试邮件
    mail_type = appium_init.inital.desired_caps['test_mail']
    print  type(mail_type)
    print mail_type
    mail.send(mail_type)