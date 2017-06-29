#coding=utf-8

import yagmail
import os
import string

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib



def get_report(result_path):

    reportName = sorted(os.listdir(result_path),
                        key=lambda filename: (os.path.getmtime(result_path + "\\" + filename)))[-1]
    return (result_path + '\\' + reportName)


def post_mail(report_file):
    
    f = open(report_file)
    mail_body = f.read()

    msg = MIMEMultipart()
    html_att = MIMEText(mail_body, 'html', 'utf-8')
    att = MIMEText("html", 'plain', 'utf-8')
    msg.attach(html_att)
    msg.attach(att)


    
    
    #print mail_body
    
    #mail_body = f.read().decode()


    #mail_body.close()



    yag = yagmail.SMTP(user='89605179@qq.com', password='wtqglbdactrhbhji', host='smtp.qq.com', port='587')
    contents = mail_body


    yag.send(to='leHe@quarkfinance.com', subject='2323232', contents=[msg.as_string()])


"""
yag = yagmail.SMTP(
    user="89605179@qq.com",
    password="wtqglbdactrhbhji",
    host="smtp.qq.com",
    port="587"
)
"""



if __name__ == '__main__':
    #a=get_report("E:\\quark_work\\result\\2017-05-27")
    post_mail("E:\\quark_work\\result\\2017-05-27\\2017-05-27-15_25_30_result.html")
    
    