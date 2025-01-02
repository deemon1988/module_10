import threading

import requests
import cloudscraper


from learning_html_parser import HTML_Parser


url = 'https://www.weblancer.net'
sites = [
    'https://www.fl.ru',
    'https://www.weblancer.net/',
    'https://www.freelancejob.ru/',
    #'https://kwork.ru',
    'https://work-zilla.com/',
    'https://iklife.ru/udalennaya-rabota-i-frilans/poisk-raboty/vse-samye-luchshie-sajty-i-birzhi-v-internete.html',
]


class PageSizer(threading.Thread):
    def __init__(self, site_url):
        super().__init__()
        self.site_url = site_url
        self.total_bytes_size = 0


    def run(self):
        html_data = self._get_html(self.site_url)
        parser = HTML_Parser(self.site_url)
        parser.feed(html_data)
        links = parser.links
        #print(links)

        for link in links:
            extract_data = self._get_html(link)
            self.total_bytes_size =+ len(extract_data)
        print(self.total_bytes_size)

    def _get_html(self, url):
        print(f'Go {url} ...')
        scraper = cloudscraper.create_scraper()
        response = scraper.get(url)
        return response.text

th_sizers = [PageSizer(site_url=url) for url in sites]
for sizer in th_sizers:
    sizer.start()
    sizer.join()

# thread = PageSizer(site_url=url)
# thread.start()
# thread.join()
