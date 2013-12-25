from celery.schedules import crontab
from celery.task import periodic_task
from headline.crawler import Crawler
from headline.models import Headline, Press


@periodic_task(run_every=crontab(minute="*/15"))
def crawl_headlines():
    crawler = Crawler()
    headlines = crawler.get_headlines()
    for press_name, title in headlines.iteritems():
        press = Press.objects.get_or_create(name=press_name)
        headline = Headline.objects.filter(press=press).order_by('-id').first()
        if not headline or headline.title != title:
            Headline.objects.create(press=press, title=title)