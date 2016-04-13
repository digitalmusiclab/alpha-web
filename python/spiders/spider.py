import scrapy
import os

from scrapy.crawler import CrawlerProcess
from spiders.spotify import Spotify
#from spiders.echonest import Echonest

process = CrawlerProcess()
process.crawl(Spotify)
#process.crawl(Echonest)
process.start() # the script will block here until all crawling jobs are finished
