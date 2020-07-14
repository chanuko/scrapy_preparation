import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ExampleSpider(CrawlSpider):
    name = 'example'

    rules = (
            Rule(LinkExtractor(allow=r'contact/'), callback='parse_contact', follow=True),
            )

    def __init__(self, *args, **kwargs):
        super(ExampleSpider, self).__init__(*args, **kwargs)

        self.start_urls = ["https://about.mercari.com/"]
        self.allowed_domains = ["about.mercari.com"]


    def parse_contact(self, response):
        print(self.url)
        pass
