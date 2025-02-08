import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from PersonalNoteManage.project_settings import email_settings


class EmailStrategy:
    def __init__(self, settings=email_settings):
        self.settings = settings

    def send_email(self, to_email, subject, content):
        # 创建邮件对象
        msg = MIMEMultipart()
        msg["From"] = self.settings.get('EMAIL_USER')
        msg["To"] = to_email
        msg["Subject"] = subject

        # 添加邮件正文
        msg.attach(MIMEText(content, "plain", "utf-8"))

        # 连接 SMTP 服务器并发送邮件
        try:
            server = smtplib.SMTP_SSL(self.settings.get('SMTP_SERVER'), self.settings.get('SMTP_PORT'))
            server.login(self.settings.get('EMAIL_USER'), self.settings.get('EMAIL_PASS'))
            server.sendmail(self.settings.get('EMAIL_USER'), to_email, msg.as_string())
            server.quit()
            print("邮件发送成功")
        except Exception as e:
            print("邮件发送失败:", str(e))
