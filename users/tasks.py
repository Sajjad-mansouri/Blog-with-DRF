from django.core.mail import EmailMessage
import time
from celery import shared_task

@shared_task()
def mail_send(mail_subject,message,to_email):
	time.sleep(30)
	email=EmailMessage(mail_subject,message,to=[to_email])
	email.send()