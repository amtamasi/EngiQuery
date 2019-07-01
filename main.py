'''
Created: 07/01/2019
Author: Anthony Tamasi
Description:
    This file serves as the driver program for the EngiQuery search system. This allows for testing and
    encourages code modularity.
'''

#Imports
from crawler import ukySpider
import time

if __name__ == '__main__':
    print("Running...")

    start_url = "http://www.engr.uky.edu/"
    start = time.time() #Start our timer to measure how long the crawl takes.

    spider = ukySpider(start_url, url_limit=10000, batch_interval=20)

    print("Starting crawl...")
    spider.startCrawl()
    print("Finished crawling!")
    spider.report(start)





