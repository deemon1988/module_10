import requests

sites = [
    'https://www.fl.ru/',
    'https://www.weblancer.net',
    'https://www.freelancejob.ru/',
    'https://kwork.ru',
    'https://work-zilla.com/',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]

from html.parser import HTMLParser


class HTMLTextExtractor(HTMLParser):
    """Class for extracting plain text from HTML content."""

    def __init__(self, base_url):
        super().__init__()
        self.links = []
        self.base_url = base_url

    def handle_starttag(self, tag, attrs):
        if tag in ('link', 'script'):
            attrs = dict(attrs)
            if 'rel' in attrs and attrs['rel'] == 'stylesheet':
                try:
                    link = self._refine(attrs['href'])
                    self.links.append(link)
                except:
                    link = self._refine(attrs['data-href'])
                    self.links.append(link)
            elif 'src' in attrs:
                link = self._refine(attrs['src'])
                self.links.append(link)

    def _refine(self, link):
        if not link.startswith(('http://', 'https://')):
            return f"{self.base_url}/{link.lstrip('/')}"  # Преобразуем относительную ссылку в абсолютную
        return link


import cloudscraper


def _get_html(url):
    try:
        print(f'Go {url}...')
        res = requests.get(url)
    except Exception as exc:
        print(exc)
    else:
        return res.text


for url_site in sites:
    total_bytes = 0

    scraper = cloudscraper.create_scraper()
    response = scraper.get(url_site)
    html_data = response.text
    parser = HTMLTextExtractor(url_site)
    parser.feed(html_data)

    for link in parser.links:

        extra_data = _get_html(url=link)
        if extra_data:
            total_bytes = + len(extra_data)

    print(total_bytes)
    print(f'For url {url_site} need download {total_bytes // 1024} Kb ({total_bytes} bytes)')
