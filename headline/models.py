from datetime import datetime
from django.db import models
from utils import to_relative_time


class Press(models.Model):

    class Meta:
        verbose_name = u'Press'
        verbose_name_plural = u'Presses'

    def __unicode__(self):
        return u'%s' % self.name

    name = models.CharField(max_length=50)


class Headline(models.Model):

    class Meta:
        verbose_name = u'Headline'
        verbose_name_plural = u'Headlines'

    def __unicode__(self):
        return u'<%s> %s' % (self.press.name, self.title)

    press = models.ForeignKey(Press)
    title = models.TextField()
    link = models.TextField()
    crawled_time = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return dict(
            id=self.id,
            press_name=self.press.name,
            link=self.link,
            title=self.title,
            crawled_time=self.crawled_time.strftime('%y-%m-%d %H:%M'),
            relative_crawled_time=to_relative_time(self.crawled_time)
        )


class CrawlLog(models.Model):

    class Meta:
        verbose_name = u'CrawlLog'
        verbose_name_plural = u'CrawlLogs'

    def __unicode__(self):
        return u'crawled at %s' % self.crawled_time.strftime(u'%m/%d %H:%M')

    updated_presses = models.ManyToManyField(Press)
    crawled_time = models.DateTimeField(auto_now_add=True)
