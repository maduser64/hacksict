from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    fist_name = models.CharField(max_length=300, verbose_name="Нэр")
    last_name = models.CharField(max_length=300, verbose_name="Овог")
    is_teacher = models.BooleanField(default=False)
    code = models.CharField(max_length=300, verbose_name="Код")
    img = models.ImageField(verbose_name="Зураг", upload_to='/avatar', blank=True)

class Event(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    title = models.CharField(max_length=300, verbose_name="Гарчиг")
    short_desc = models.CharField(max_length=300, verbose_name="Богино тайлбар")
    start_date = models.CharField(verbose_name="Эхлэх Огноо", blank=True)
    finish_date = models.CharField(verbose_name="Дуусах Огноо", blank=True)
    banner_img = models.ImageField(verbose_name="Зураг", upload_to='/event_banner', blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

class Challenge(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    title = models.CharField(max_length=300, verbose_name="Гарчиг")
    short_desc = models.CharField(max_length=300, verbose_name="Богино тайлбар")
    start_date = models.CharField(verbose_name="Эхлэх Огноо", blank=True)
    finish_date = models.CharField(verbose_name="Дуусах Огноо", blank=True)
    banner_img = models.ImageField(verbose_name="Зураг", upload_to='/challenge_banner', blank=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE)

class Submission(models.Model):
    id = models.AutoField('id', primary_key=True, db_index=True)
    submit_file =  models.FileField(upload_to='/submission/%Y/%m/%d')
    challenge_id = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    submit_date = models.CharField(verbose_name="Илгээсэн Огноо", blank=False)
