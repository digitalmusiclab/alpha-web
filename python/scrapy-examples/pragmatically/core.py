from DmozSpider import DmozSpider

# scrapy api
from scrapy import signals
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings

def spider_closing(spider):
    """Activates on spider closed signal"""
    reactor.stop()

settings = Settings()

# crawl responsibly
settings.set("USER_AGENT", "Kiran Koduru (+http://kirankoduru.github.io)")
crawler = Crawler(settings)

# stop reactor when spider closes
crawler.signals.connect(spider_closing, signal=signals.spider_closed)

crawler.configure()
crawler.crawl(DmozSpider())
crawler.start()
reactor.run()
