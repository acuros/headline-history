#-*-coding:utf8-*-
import datetime
import re
import ujson as json
import urllib

from pyquery import PyQuery

ignore_list = [u'아이뉴스24', u'월스트리트저널']


class Crawler(object):
    def get_headlines(self):
        news_map = self._get_news_map()
        headlines = dict()
        for news in news_map:
            if news['nm'] in ignore_list:
                continue
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
        html = f.read()
        pq = PyQuery(html)
        link_item = pq('a[target="_blank"]:first')
        title = link_item.text()
        if title:
            return title

        headline_link_items = pq('a[href="%s"]' % link_item.attr('href')).items()
        texts = [item.text() for item in headline_link_items if item.text()]
        if len(texts) > 1:
            return texts[0]

        candidate = [text for text in texts
                     if len(re.findall(r'\.+', text)) < 2 and len(text) < 80]
        if candidate:
            return candidate[0]