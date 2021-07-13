from django.db import models

# Create your models here.
# 해당 application이 필요한 데이터베이스를 정의할 수 있는 code입니다

class Riot(models.Model):
    api_key = models.CharField(max_length=50,null=True)