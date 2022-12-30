from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def Check_for_a(value):
    if value[0].lower()=='a':
        raise ValidationError('should not start with a')


def check_for_s(value):
    if value[0].lower()=='s':
        raise ValidationError('should not start with s')



class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True,validators=[Check_for_a])

    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[check_for_s])
    url=models.URLField()

    def __str__(self):
        return self.name


class AccessRecords(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()