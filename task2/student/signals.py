from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from student.models import Institute, Branch
from django.core.mail import EmailMessage


@receiver(post_save, sender=Branch)
def send_email_institute(sender, instance, created, **kwargs):
    if created:
        email_to = instance.institute.email
        subject = instance.name + " Branch is created"
        body = "Body of email template"
        email = EmailMessage(subject, body, to=[email_to])
        email.send()