from django.db import models

class User(models.Model):
    name= models.CharField('이름', max_length=20, null=False)
    #password = models.CharField