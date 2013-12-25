import ujson as json
import urllib

from BeautifulSoup import BeautifulSoup


def get_news_map():
    f = urllib.urlopen('http://newsstand.naver.com/')
    html_content = f.read()
    news_map_json = html_content.split('var pressList = ')[1].split(';')[0]
    return json.loads(news_map_json)


def get_headline(news_page):
    f = urllib.urlopen('http://newsstand.naver.com%s' % news_page)
    html_content = f.read()
    soup = BeautifulSoup(html_content)
    titles = [link.text for link in soup.findAll('a', attrs={'target': '_blank'}) if link.text]
    if not titles:
        print news_page
        return
    return titles[0]

if __name__ == '__main__':
    news_map = get_news_map()
    for news in news_map:
        print news['nm'], '<<<', get_headline(news['page']), '>>>'