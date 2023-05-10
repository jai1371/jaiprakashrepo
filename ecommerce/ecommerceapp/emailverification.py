from django.conf import settings
from django.core.mail import send_mail

def send_email_token(email,token):
    try:
        subject = 'welcome dear to our website'
        message = f'Hi click here to verify eamil http://127.0.0.1:8000/verify/{token}/'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, email_from, recipient_list)
        print('sent')
    except Exception as e:
        print('not sent')
        return False
    return True


