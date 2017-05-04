#coding=utf-8

import yagmail
import os


def get_report(result_path):

    reportName = sorted(os.listdir(result_path),
                        key=lambda filename: (os.path.getmtime(result_path + "\\" + filename)))[-1]
    return (result_path + '\\' + reportName)


def post_mail(report_file):
    f = open(report_file, 'rb')
    mail_body = f.read()
    f.close()
    yag = yagmail.SMTP(user='89605179@qq.com', password='wtqglbdactrhbhji', host='smtp.qq.com', port='587')
    contents = mail_body



    yag.send(to='leHe@quarkfinance.com', subject='2323232', contents=[mail_body])


"""
yag = yagmail.SMTP(
    user="89605179@qq.com",
    password="wtqglbdactrhbhji",
    host="smtp.qq.com",
    port="587"
)
"""



if __name__ == '__main__':
    a=get_report("E:\\quark_work\\result\\2017-05-03")
    post_mail(a)