import ujson as json

from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from headline.models import Headline, Press, CrawlLog


HEADLINES_PER_PAGE = 50


def home(request):
    headlines = Headline.objects.all().order_by('-id')[:HEADLINES_PER_PAGE]
    presses = Press.objects.all()
    last_log = CrawlLog.objects.all().order_by('-id').first()
    return render(request, 'home.html', dict(headlines=headlines,
                                             presses=presses,
                                             last_log=last_log))


def more(request, last_headline_id):
    headlines = Headline.objects.filter(id__lt=last_headline_id)\
                        .order_by('-id')[:HEADLINES_PER_PAGE]
    headlines = [dict(id=headline.id,
                      pressName=headline.press.name,
                      link=headline.link,
                      title=headline.title,
                      crawledTime=datetime.strftime(headline.crawled_time,
                                                    '%y-%m-%d %H:%M'))
                 for headline in headlines]
    return HttpResponse(json.dumps(headlines), mimetype='application/json')
