"""
How to run scrapers programmatically from a script
"""
from spiders.DmozSpider import DmozSpider
from spiders.CraigslistSpider import CraigslistSpider

# scrapy api
from scrapy import signals
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings


# list of crawlers
TO_CRAWL = [DmozSpider, CraigslistSpider]

# list of crawlers that are running
RUNNING_CRAWLERS = []

def spider_closing(spider):
    """Activates on spider closed signal"""
    RUNNING_CRAWLERS.remove(spider)
    if not RUNNING_CRAWLERS:
        reactor.stop()

for spider in TO_CRAWL:
    settings = Settings()

    # crawl responsibly
    settings.set("USER_AGENT", "Kiran Koduru (+http://kirankoduru.github.io)")
    crawler = Crawler(settings)
    crawler_obj = spider()
    RUNNING_CRAWLERS.append(crawler_obj)

    # stop reactor when spider closes
    crawler.signals.connect(spider_closing, signal=signals.spider_closed)
    crawler.configure()
    crawler.crawl(crawler_obj)
    crawler.start()

# blocks process so always keep as the last statement
reactor.run()
