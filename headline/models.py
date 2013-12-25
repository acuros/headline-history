from django.db import models


class Press(models.Model):
    name = models.CharField(max_length=50)


class Headline(models.Model):
    press = models.ForeignKey(Press)
    title = models.TextField()
    link = models.TextField()
    crawled_time = models.DateTimeField(auto_now_add=True)


class CrawlLog(models.Model):
    updated_presses = models.ManyToManyField(Press)
    crawled_time = models.DateTimeField(auto_now_add=True)