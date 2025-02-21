import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://www.divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
        divans = response.css('div._Ud0k')
        print(divans)
        for divan in divans:
           yield {
              'name' : divan.css('div.lsooF span::text').get(),
              'price' : divan.css('div.pY3d2 span::text').get(),
              'url' : divan.css('a').attrib['href']
           }
