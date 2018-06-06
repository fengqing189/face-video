from django.db import models

class User(models.Model):
    username = models.CharField(verbose_name='考生姓名',max_length=64)
    id_number = models.CharField(verbose_name='考生身份证',max_length=18)
    phone = models.IntegerField(verbose_name='考生手机号码')


