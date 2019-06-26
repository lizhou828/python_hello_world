# -*- coding:utf-8 -*-

"""
@Function: Python3.3 邮件发送 含附件（各种类型文件） https://blog.csdn.net/y396397735/article/details/78136753?utm_source=blogxgwz8
@File    :          email_scheduler.py
@Contact :          lizhou@glorypty.com
@License :          (C)Copyright 2019-2020

@Modify Time        @Author      @Version        @Desciption
------------        -------      --------        -----------
2019-6-21 17:10     lizhou         1.0

"""
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

import time

from helloWorld import print_info


def send_email(sendAddr, password, recipientAddrs, subject='', content=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)

    # 添加附件，传送文件
    part = MIMEApplication(
        open(r'2019-6-24.xls', 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="2019-6-24.xls")
    msg.attach(part)

    smtp = smtplib.SMTP()
    smtp.connect("smtp.glorypty.com", '25')
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs, str(msg))
    smtp.quit()


if __name__ == "__main__":
    try:
        subject = 'Python3 测试发送邮件'
        content = '这是一封来自 Python3 编写的测试邮件。'
        start = time.time()
        send_email('lizhou@glorypty.com', 'gr123789', 'lizhou828@126.com', subject, content)
        end = time.time()
        print_info("邮件发送完成，耗时：{}秒".format('%.2f' % (end - start)))
    except Exception as err:
        print(err)

