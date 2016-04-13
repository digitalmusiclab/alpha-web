import scrapy
import logging
import json
class Echonest(scrapy.Spider):
    name = "echonest"
    # 
    # f = open('workfile')
    # start_urls = [url.strip() for url in f.readlines()]
    # f.close()

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        jsondata = json.loads(response.body)
        self.logger.info('length:%s', jsondata['tracks']['total'])

        tracks_found = jsondata['tracks']['total']
        # isrc found more than one track
        if (tracks_found > 1):
            self.logger.info("Must determine proper track, too many tracks")

        elif (tracks_found == 1):
            self.logger.info("Found one track, determine if track is correct")
            self.fuzzyMatch()


    def fuzzyMatch(self):
        self.logger.info("started fuzzy matching")
