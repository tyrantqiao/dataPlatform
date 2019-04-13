# _*_ encoding:utf-8 _*_
from random import Random

from django.core.mail import send_mail,EmailMessage
from iot.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_email(email, send_type='register'):
    code = random_str(6)
    if send_type == 'register':
        email_title = '邮箱注册'
        email_body = '您的验证码为：{0}，5分钟内注册有效'.format(code)
        try:
            #msg = EmailMessage(email_title,email_body,EMAIL_FROM, to=[email])
            #msg.send()
            send_status = send_mail(email_title, email_body, EMAIL_FROM, [email],fail_silently=False)
        except:
            return code,'error'
        if send_status:
            return code,send_status
    elif send_type == 'forget':
        email_title = '密码找回'
        email_body = '您的验证码为: {0}，5分钟内'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return code, send_status, send_type
    elif send_type == 'update_email':
        email_title = '系统邮箱修改'
        email_body = '您的邮箱验证码为：{0}, 5分钟内'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return code, send_status, send_type

if __name__ == "__main__":
    send_register_email("tyrantqiao@qq.com")
