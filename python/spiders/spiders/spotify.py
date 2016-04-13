import scrapy
import logging
import json
import time
class Spotify(scrapy.Spider):
    name = "spotify"
    with open('db.json') as data_file:
        data = json.load(data_file)

    start_urls=[]

    for row in data['database']:
        start_urls.append("https://api.spotify.com/v1/search?q=isrc:" + row['isrc'] + "&type=track")

    def parse(self, response):
        self.logger.info('Parse function called on %s', response.url)
        jsondata = json.loads(response.body)
        self.logger.info('length:%s', jsondata['tracks']['total'])

        tracks_found = jsondata['tracks']['total']

        print(data)
        # isrc found more than one track
        if (tracks_found > 1):
            self.logger.info("Must determine proper track, too many tracks")

        elif (tracks_found == 1):
            self.logger.info("Found one track, determine if track is correct")
            self.fuzzyMatch()



    def fuzzyMatch(self):
        time.sleep(5)
        self.logger.info("started fuzzy matching")
