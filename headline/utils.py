#-*-coding:utf8-*-
import datetime

from django.utils import timezone


def to_relative_time(event_time):
    event_time = event_time.astimezone(timezone.get_current_timezone())
    event_time = event_time.replace(tzinfo=None)
    delta = datetime.datetime.now() - event_time
    if delta < datetime.timedelta(seconds=10):
        return u'방금'
    elif delta < datetime.timedelta(minutes=1):
        return u'몇십 초 전'
    elif delta < datetime.timedelta(hours=1):
        return u'%d분 전' % (delta.seconds // 60)
    elif delta < datetime.timedelta(days=1):
        return u'%d시간 전' % (delta.seconds // 60 // 60)
    elif delta < datetime.timedelta(days=7):
        return u'%d일 전' % delta.days
    elif delta < datetime.timedelta(days=60):
        return u'%d주 전' % (delta.days // 7)
    elif delta < datetime.timedelta(days=365):
        return u'%d달 전' % (delta.days // 30)
    else:
        return u'머나먼 시간'
