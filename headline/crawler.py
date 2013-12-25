import datetime
import ujson as json
import urllib

from BeautifulSoup import BeautifulSoup


class Crawler(object):
    def get_headlines(self):
        news_map = self._get_news_map()
        headlines = dict()
        for news in news_map:
            headline = self._get_headline(news['page'])
            if not headline:
                now = datetime.datetime.now()
                with open('log/log.txt', 'a') as f:
                    f.write('[%s] Headline not captured : %s\n' % (now, news['page']))
                continue
            headlines[news['nm']] = headline
        return headlines

    def _get_news_map(self):
        f = urllib.urlopen('http://newsstand.naver.com/')
        html_content = f.read()
        news_map_json = html_content.split('var pressList = ')[1].split(';')[0]
        return json.loads(news_map_json)

    def _get_headline(self, news_page):
        f = urllib.urlopen('http://newsstand.naver.com%s' % news_page)
        html_content = f.read()
        soup = BeautifulSoup(html_content)
        titles = [link.text for link in soup.findAll('a', attrs={'target': '_blank'}) if link.text]
        if not titles:
            return
        return titles[0]