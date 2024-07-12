from scrapy.crawler import CrawlerProcess


def scrape_web_text():
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })
    # process.crawl(WebTextSpider)
    process.start()


if __name__ == '__main__':
    scrape_web_text()
