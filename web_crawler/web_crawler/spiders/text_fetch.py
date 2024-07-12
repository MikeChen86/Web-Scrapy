from scrapy.http import Response
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class TextFetchSpider(CrawlSpider):
    name = "text_fetch"
    allowed_domains = ["127.0.0.1"]
    start_urls = ["http://127.0.0.1:8000/company"]
    rules = (
        Rule(LinkExtractor(allow=r'^(?!#).*'), callback='parse_item', follow=True),
    )

    def parse_item(self, response: Response):
        self.logger.info('Crawled URL: %s', response.url)
        yield {
            'title': self.inner_text_quick(response.css('body')),
            'url': response.url,
        }

    @staticmethod
    def inner_text_quick(elements):
        return [[el.strip() for el in element.css('*::text').getall() if el.strip() != ''] for element in elements]
