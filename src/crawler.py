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
from bs4 import BeautifulSoup
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse


class ukySpider():
    """
    This class governs how we crawl the domain
    """
    def __init__(self, start_url=None, url_limit=500000, batch_interval=1000, num_workers=5):
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
            target_url (string): The current url we are trying to scrape.
            current_crawl_num (int): A counter to track how many total pages we have scraped so far.
            batch_crawl_num (int): A counter to track how many pages we scraped in this batch.
        """
        start_time = time.time()
        current_crawl_num = 0
        batch_crawl_num = 0


        while current_crawl_num < self.url_limit:
            try:
                target_url = self.work_pool.get(timeout=5)
                print("Now Crawling: {}".format(target_url))
                if target_url not in self.closed_pool:
                    self.closed_pool.add(target_url)
                    job = self.pool.submit(self.scrapePage, target_url)
                    job.add_done_callback(self.postCrawlCallback)
                print("FInished crawling: {}".format(target_url))

            except Empty:
                return
            except Exception as e:
                print("Error at {}".format(target_url))
                print(e)
                print()
                continue

            current_crawl_num += 1
            batch_crawl_num += 1
            if(current_crawl_num % self.batch_interval == 0):
                self.report(start_time=start_time)
                batch_crawl_num = 0 #Reset counter for number of pages crawled this batch.

        self.report(start_time=start_time)

        


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
            html (Response.text): The text HTML of the url scraped.
        Returns:
            None.
        """

        soup = BeautifulSoup(html, 'lxml')
        links = soup.find_all('a', href=True)
        for link in links:
            url = link['href']
            print("LINK[HREF]: {}".format(url))
            print()
            if url.startswith('/') or url.startswith(self.start_url):
                url = urljoin(self.start_url, url)
                print("URLS TO ADD: {}".format(url))
                print()
                if url not in self.closed_pool:
                    print("\t Adding this url: {}".format(url))
                    print()
                    self.work_pool.put(url)


    def scrapeInfo(self, html):
        """
        Scrape the information you want from this webpage.
        Parameters:
            html (Response.text): The text HTML of the url scraped.
        Returns:

        """

        return

    def scrapePage(self, url):
        """
        Scrape this url and return the HTTP response. If it can't get the url, print out an error.
        Parameters:
            url (string): The url to be scraped.
        Returns:
            response (Requests Response): The HTTP response object of this url.
        """

        try:
            response = requests.get(url, timeout=3)
            return response
        except requests.RequestException as e:
            #print("Request Error at {}".format(url))
            print("Request Error")
            print(e)
            print()
            return 

    def postCrawlCallback(self, res):
        """
        Called to 'complete the job' for a particular url. This function is called on that url's response to
        ensure it was a successful response and then parse the url's links and scrape its relevant content.
        Parameters:
            res (Requests Response): The response received from the url we are scraping.
        Returns:
            None.
        """

        result = res.result()
        if result and result.status_code == 200:
            self.parseLinks(result.text)
            self.scrapePage(result.text)

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
            print("----------UKY Spider--------------------")
            print("Number of (total) pages crawled:", len(self.closed_pool))
            print("Number of pages crawled this batch:", self.batch_interval)
            #print("Number of 'special links':", len(self.special_urls))
            print("Time since started: " + str(round(current_time - start_time, time_decimal)) + " seconds")
            print("----------------------------------------")
            print('\n'*5) #Buffer space


        


