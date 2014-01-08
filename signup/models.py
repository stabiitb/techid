from django.db import models

# Create your models here.
from django.contrib.auth.hashers import *
from django.template import RequestContext, loader

from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from misc.models import *
import re
def validate_mobile(mobile):
    pattern = "0?[0-9]{10}"
    return re.match(pattern,mobile)


class UserManager(BaseUserManager):
    def create_user(self,email=None,is_active=None,
    	password=None,first_name=None,last_name=None, **extra_fields):
        if is_active == None:
            is_active = True
        user = self.model(
            email=UserManager.normalize_email(email),
            first_name=first_name or '',
            last_name=last_name or '',
            is_active=is_active,**extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  email, password, first_name=None, last_name=None,**extra_fields):
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
from image_cropping import ImageCropField, ImageRatioField

class User(AbstractBaseUser):
    email = models.EmailField(max_length=254, unique=True, db_index=True)
    mobile = models.CharField(max_length=10,null=True,blank=True,validators=[validate_mobile])
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    department = models.ForeignKey(Department,null=True,blank=True,default=1)
    hostel = models.ForeignKey(Hostel,null=True,blank=True,default=1)
    year = models.ForeignKey(Year,null=True,blank=True,default=1)
    ldap_username = models.CharField(max_length=20,null=True,blank=True)
    rollno=models.CharField(max_length=20,null=True,blank=True)
    alternate_email = models.EmailField(null=True,blank=True)
    room = models.CharField(max_length=10)
    skill = models.ManyToManyField(Skill,null=True,blank=True)
    photo = ImageCropField(max_length=100,upload_to='documents/%Y/%m/%d',blank=True,null=True)
    cropping = ImageRatioField('photo', '150x200')
    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.first_name
    
    @property
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        if self.ldap_username:
            return self.ldap_username
        else:
            return "admin"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_superuser(self):
        return self.is_admin

class RegistrationCode(models.Model):
    user = models.OneToOneField(User)
    registration_code = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.email

class ResetCode(models.Model):
    user = models.OneToOneField(User)
    reset_code = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.user.email
