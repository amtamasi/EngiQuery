'''
Created: 07/01/2019
Author: Anthony Tamasi
Description:
    This file defines our process of crawling the web domain and storing the relevant data found.
Notes:
    Partial inspiration from "https://edmundmartin.com/multi-threaded-crawler-in-python/" to incorporate
    multi-threading.
'''

#Imports
import time
import os
import requests
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


class ukySpider():
    """
    This class governs how we crawl the domain
    """
    def __init__(self, start_url=None, url_limit=50000, batch_interval=1000, num_workers=20):
        """
        Parameters:
            start_url (str): The url of the website we are going to crawl.
            url_limit (int): The maximum number of urls we want to crawl from that website domain.
            batch_interval (int): The number of urls we crawl before we save their information to the database
                                  and print a report for that 'batch'.
            num_workers (int): The number of maximum thread workers we want for ThreadPoolExecutor.
        Variables:
            start_url (str): The url of the website we are going to crawl.
            url_limit (int): The maximum number of urls we want to crawl from that website domain.
            batch_interval (int): The number of urls we crawl before we save their information to the database
                                  and print a report for that 'batch'.
            work_pool (Queue): Contains the urls that we still need to crawl.
            closed_pool (Set): Contains the urls that we have already crawled.
            pool (ThreadPoolExecutor): Lets us submit jobs to multi-thread work for multiple workers.
        """
        self.start_url = start_url
        self.url_limit = url_limit
        self.batch_interval = batch_interval

        self.work_pool = Queue()
        self.closed_pool = set([])
        self.pool = ThreadPoolExecutor(max_workers=num_workers)

        self.work_pool.put(start_url)


    def save(self, file_name):
        """
        Save the state of the crawler object. 
        Parameters:
            file_name (str): The name of the file you want to save the crawler information to.
        Returns:
            None. Creates file and saves to it.
        """

    def load(self, file_name):
        """
        Load the state of a crawler into this crawler object.
        Parameters:
            file_name (str): The name of the file you want to load crawler information from.
        Returns:
            None. Updates the state of this crawler.
        """

    def startCrawl(self):
        """
        Kicks off the original crawl.

        Variables:
            job (Future): The current job for a single url to crawl.
        """
        current_crawl_num = 0
        self.crawl(self.start_url, current_crawl_num)

        while True:
            try:
                target_url = self.work_pool.get(timeout=45)
                if target_url not in self.closed_pool:
                    self.closed_pool.add(target_url)
                    job = self.pool.submit(self.crawl, target_url)
                    job.add_done_callback(self.postCrawlCallback)

            except Empty:
                return
            except Exception as e:
                print(e)
                continue


    def crawl(self, url, current_crawl_num):
        """
        Crawl this url domain.
        Parameters:
            url (str): The url that this function will crawl and download information for.
            current_crawl_num = The number of pages that have been crawled so far.
        Returns:
            None.        
        """


        current_crawl_num += 1

    def parseLinks(self, html):
        """
        Add all unique links to the work pool to be crawled.
        Parameters:
            html (): 
        Returns:
            None.
        """

    def scrapeInfo(self, html):
        """

        Parameters:
            html (): 
        """

    def postCrawlCallback(self, res):
        """
        Adds the 
        Parameters:
            res (Requests Response): 
        """

        result = res.result()
        if result and result.status_code == 200:
            self.parseLinks(result.text)
            self.scrapeInfo(result.text)

    def report(self, start_time=None):
        """
        Print out a report for the user to aid in debugging and provide general statistics.
        Parameters:
            start_time (Datetime): The time at which we first started the crawl.
        Returns:
            None. Prints to standard output
        Variables:
            current_time (DateTime): The current time on the computer.
            time_decimal (int): The number of decimals you want to round the time to.
        """

        if(start_time is None):
            print("Nothing crawled yet, there is nothing to report!")
        else:
            current_time = time.time()
            time_decimal = 3

            print() #Buffer space
            print("----------UKY Spider----------")
            print("Number of (total) pages crawled:", len(self.closed_pool))
            print("Number of pages crawled this batch:", self.batch_interval)
            #print("Number of 'special links':", len(self.special_urls))
            print("Time since started: " + str(round(current_time - start_time, time_decimal)) + " seconds")
            print('\n'*5) #Buffer space


        


