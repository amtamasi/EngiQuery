'''
Created: 07/01/2019
Author: Anthony Tamasi
Description:
    This file serves as the driver program for the EngiQuery search system. This allows for testing and
    encourages code modularity.
'''

#Imports
from crawler import Crawler

def main():
    print("Running...")

    start_url = "http://www.engr.uky.edu/"
    #start_url = "https://blog.acolyer.org/"
    #start_url = "https://www.stanford.edu/"
    #start_url = "https://web.mit.edu"
    start_url = "https://terraria.gamepedia.com/"

    spider = Crawler(start_url, url_limit=2000000, batch_interval=5000, num_workers=8)

    
    spider.startCrawl()
    
    print("Pages crawled:", len(spider.closed_pool))
    print("Remaining left in queue:", spider.work_pool.qsize())

    return

if __name__ == '__main__':
    main()




