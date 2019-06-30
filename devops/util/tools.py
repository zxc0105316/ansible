from django.core.mail import send_mail
import time

class sendmail():
    def __init__(self,receive_addr,sub_info,content_info):
        sub_data = time.strftime("")