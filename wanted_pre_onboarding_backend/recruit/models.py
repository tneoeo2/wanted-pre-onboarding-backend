from django.db import models
from accounts.models import User


class Company(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='회사_id')
    name = models.CharField(max_length=255, verbose_name='회사명')
    country = models.CharField(max_length=255, verbose_name= '국가')
    region = models.CharField(max_length=255, verbose_name= '지역')

    def __str__(self):
        return self.name
    
    
class Recruit(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE,verbose_name='회사명') 
    position = models.CharField(max_length=255, verbose_name='채용포지션')
    reward = models.PositiveIntegerField(verbose_name='채용보상금')
    detail = models.TextField(verbose_name='채용내용')
    skill = models.CharField(max_length=255,  verbose_name='사용기술')

    def __str__(self):
        return self.position
    
    
class Apply(models.Model):
    recruit = models.ForeignKey(Recruit, on_delete=models.CASCADE, verbose_name='채용공고')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='지원자')

    def __str__(self):
        return f"{self.user}의 지원 내역"    
    
