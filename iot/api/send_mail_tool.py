from users.models import EmailVerify
from random import randint
from django.core.mail import send_mail
from iot.settings import EMAIL_FROM

 def get_random_code(code_length=8):
    code_source = '1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        code += code_source[randint(0,len(code_source)-1)]
    return code

def send_email_verify(email,send_type):
    code = get_random_code()
    if send_type == 'change':
        code = get_random_code(4)
    email_ver = EmailVerify()
    email_ver.email = email
    email_ver.send_type = send_type
    email_ver.code = code
    email_ver.save()
    if send_type == 'captcha':
        send_title = '欢迎注册：'
        send_body = '请输入你的验证码，你的验证码是：'+code
        send_mail(send_title,send_body,EMAIL_FROM,[email])
