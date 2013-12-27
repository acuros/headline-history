from django.db import models
from utils import to_relative_time


class Press(models.Model):
    name = models.CharField(max_length=50)


class Headline(models.Model):
    press = models.ForeignKey(Press)
    title = models.TextField()
    link = models.TextField()
    crawled_time = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return dict(id=self.id,
                      press_name=self.press.name,
                      link=self.link,
                      title=self.title,
                      crawled_time=to_relative_time(self.crawled_time)
                    )


class CrawlLog(models.Model):
    updated_presses = models.ManyToManyField(Press)
    crawled_time = models.DateTimeField(auto_now_add=True)
