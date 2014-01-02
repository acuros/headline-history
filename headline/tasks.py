from celery.schedules import crontab
from celery.task import periodic_task
from headline.crawler import Crawler
from headline.models import Headline, Press, CrawlLog


@periodic_task(run_every=crontab(minute="*/5"))
def crawl_headlines():
    crawler = Crawler()
    headlines = crawler.get_headlines()
    updated_presses = []
    for press_name, headline in headlines.iteritems():
        press, created = Press.objects.get_or_create(name=press_name)
        last_headline = Headline.objects.filter(press=press)\
                                        .order_by('-id')\
                                        .first()
        if not last_headline or last_headline.title != headline['title']:
            updated_presses.append(press)
            Headline.objects.create(press=press,
                                    title=headline['title'],
                                    link=headline['link'])
    log = CrawlLog.objects.create()
    log.updated_presses.add(*updated_presses)
