import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divanpars"
    allowed_domains = ["divan.ru"]  # Домен не должен содержать протокол (https://)
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data.csv',
        'FEED_EXPORT_ENCODING': 'utf-8',  # Обеспечивает правильную кодировку для CSV
    }

    def parse(self, response):
        divans = response.css('div._Ud0k')
        for divan in divans:
            yield {
                'name': divan.css('div.lsooF span::text').get(),
                'price': divan.css('div.pY3d2 span::text').get(),
                'url': divan.css('a').attrib['href']
            }