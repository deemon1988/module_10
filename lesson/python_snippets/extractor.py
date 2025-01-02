from html.parser import HTMLParser
import requests

class LinkExtractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__()
        self.base_url = base_url
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag in ('a', 'link', 'script'):
            attrs = dict(attrs)
            if 'href' in attrs:
                link = self._refine(attrs['href'])
                self.links.append(link)
            elif 'src' in attrs:
                link = self._refine(attrs['src'])
                self.links.append(link)
        else:
            return

    def _refine(self, link):
        if not link.startswith(('http://', 'https://')):
            return f"{self.base_url}/{link.lstrip('/')}"  # Преобразуем относительную ссылку в абсолютную
        return link

#Проверьте остальную часть вашего кода с этим классом.