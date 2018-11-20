from django.db import models
from django.core.validators import RegexValidator
from django_countries.fields import CountryField

from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
import uuid
import jsonfield


#Signals
from django.db.models.signals import post_save
from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def send_email_institute(sender, instance, created, **kwargs):
#     if created:
#         email = EmailMessage('Subject', 'Body', to=['your@email.com'])
#         email.send()

# Create your models here.


class CustomQuerySet(models.QuerySet):
    def delete(self):
        self.update(is_active=False)

class Institute(TimeStampedModel):

    objects = CustomQuerySet.as_manager()
    name = models.CharField(max_length=30, blank=True, unique=True)
    url_slug = models.SlugField()
    logo = models.ImageField(upload_to = '')
    email = models.EmailField(max_length=70,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    brochure = models.FileField(upload_to='')
    is_active = models.BooleanField(default=True)


    def __unicode__(self):
        return self.url_slug

    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()



class Branch(TimeStampedModel):

    objects = CustomQuerySet.as_manager()
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=True, unique=True)
    url_slug = models.SlugField()
    email = models.EmailField(max_length=70,blank=True)
    street = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=50,blank=True)
    state = models.CharField(max_length=50,blank=True)
    country = CountryField(blank_label='(select country)')
    zip_regex = RegexValidator(regex=r'^\^[1-9][0-9]{5}$')
    zip_code = models.CharField(validators=[zip_regex],max_length=6,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile = models.CharField(validators=[phone_regex], max_length=17)
    brochure = models.FileField(upload_to='')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.url_slug

    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()



class FeeType(TimeStampedModel):

    objects = CustomQuerySet.as_manager()
    name = models.CharField(max_length=50, unique=True)
    amount = models.FloatField()
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.name

    def delete(self):
        self.is_active = False
        self.save()

class Fee(TimeStampedModel):
    
    objects = CustomQuerySet.as_manager()   
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fees_paid = models.ManyToManyField(FeeType)
    amount = models.FloatField(default=0)
    is_active = models.BooleanField(default=True)
    payment_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

    def delete(self):
        self.is_active = False
        self.save()


class Student(TimeStampedModel):
    COURSE_CHOICES = (
        ('M', 'MBA'),
        ('B', 'B.E.'),
        ('C', 'BCA'),
    )

    objects = CustomQuerySet.as_manager()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    enrol_no = models.CharField(max_length=50, blank=True, unique=True)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    course = models.CharField(max_length=1, choices=COURSE_CHOICES)
    birth_date = models.DateField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.enrol_no

    def delete(self):
        self.is_active = False
        self.user.is_active = False
        self.save()


class Transaction(TimeStampedModel):
    # STATUS_CHOICES = (
    #     ('P', 'Pending'),
    #     ('C', 'Completed'),
    #     ('F', 'Failed'),
    #     ('', 'Failed'),
    # )

    objects = CustomQuerySet.as_manager()
    uuid = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paid_amt = models.FloatField(default=0.00)
    status = models.CharField(max_length=20)
    payment_id = models.CharField(max_length=30, null=True)
    request_dump = jsonfield.JSONField()
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.user.username

    def delete(self):
        self.is_active = False
        self.save()


   

