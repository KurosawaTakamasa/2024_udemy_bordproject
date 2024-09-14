from django.db import models

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    sns_image = models.ImageField(upload_to='')
    goods = models.IntegerField()
    read = models.IntegerField()
    readtext = models.TextField()