from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.forms import BooleanField

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, fullname, password=None):
        if not username:
            raise ValueError('아이디를 입력해주세요.')
        user = self.model(
            username=username,
            email=email,
            fullname=fullname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, username, email, fullname, password=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            fullname=fullname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField("아이디", max_length=50, unique=True)
    password = models.CharField("비밀번호", max_length=128)
    fullname = models.CharField("실명", max_length=50)
    email = models.EmailField("이메일", max_length=254)
    
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    
    REQUIRED_FIELDS = ['fullname', 'email'] 
    
    objects = UserManager()
    
    def __str__(self):
        return self.fullname
    
    def has_perm(self, perm, obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin