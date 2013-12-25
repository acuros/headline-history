from django.shortcuts import render
from headline.models import Headline, Press, CrawlLog

def home(request):
    headlines = Headline.objects.all().order_by('-id')
    presses = Press.objects.all()
    last_log = CrawlLog.objects.all().order_by('-id').first()
    return render(request, 'home.html', dict(headlines=headlines, presses=presses, last_log=last_log))
