import ujson as json

from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from headline.models import Headline, Press, CrawlLog


HEADLINES_PER_PAGE = 50


def home(request):
    query = request.GET.get('q', '') or ''
    q = Q(press__name__icontains=query) | Q(title__icontains=query)
    headlines = Headline.objects.all().filter(q)\
                        .order_by('-id')[:HEADLINES_PER_PAGE]
    presses = Press.objects.all().filter(name__icontains=query)
    last_log = CrawlLog.objects.all().order_by('-id').first()
    return render(request, 'home.html', dict(headlines=headlines,
                                             presses=presses,
                                             last_log=last_log,
                                             query=query))


def more(request, last_headline_id):
    query = request.GET.get('q', '') or ''
    q = Q(id__lt=last_headline_id) &\
        (Q(press__name__icontains=query) | Q(title__icontains=query))
    headlines = Headline.objects.filter(q).order_by('-id')[:HEADLINES_PER_PAGE]
    headlines = [headline.to_dict() for headline in headlines]
    return HttpResponse(json.dumps(headlines), mimetype='application/json')
