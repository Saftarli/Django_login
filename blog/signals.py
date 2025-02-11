from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from blog.models import Blog
from core.models import CustomUser
from django.conf import settings
from blog.tasks import  send_mail_on_fifth_blog

@receiver(post_save, sender=Blog)
def check_blog_count_and_send_mail(sender, instance, created, **kwargs):
    if created:
        send_mail_on_fifth_blog.apply_async()