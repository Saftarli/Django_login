from celery import shared_task
from django.core.mail import send_mail
from .models import Blog
from core.models import CustomUser
from django.conf import  settings
import  logging

@shared_task
def send_mail_on_fifth_blog():
    blog_count = Blog.objects.count()
    logging.info(blog_count,'############')

    if blog_count == 5:

        admin_emails = list(CustomUser.objects.filter(is_superuser=True).values_list('email', flat=True))
        logging.info(admin_emails,'###############10202021010########')




        send_mail(
            "5-ci Blog Yaradıldı",
            "Təbriklər! Bu gün sistemdə 5-ci blog yaradıldı.",
            settings.EMAIL_HOST_USER,
            ['tofiqsefterli@gmail.com'],
                fail_silently=False,
            )
        print("Adminə e-poçt göndərildi.")
    else:
        logging.info("#################PROBLEM##################")