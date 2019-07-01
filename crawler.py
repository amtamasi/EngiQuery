'''
Created: 07/01/2019
Author: Anthony Tamasi
Description:
    This file defines our process of crawling the web domain and storing the relevant data found.

'''

#Imports
import time
import os
import requests


class ukySpider():
    """
    This class governs how we crawl the domain
    """
    def __init__(self, start_url=None, url_limit=50000, batch_interval=1000):
        """
        Parameters:
            start_url (str): The url of the website we are going to crawl.
            url_limit (int): The maximum number of urls we want to crawl from that website domain.
            batch_interval (int): The number of urls we crawl before we save their information to the database
                                  and print a report for that 'batch'.
        """
        self.start_url = start_url
        self.url_limit = url_limit
        self.batch_interval = batch_interval

    def save(self, file_name):
        """
        What should I save? The state of the crawler? I can save the state of the crawler AND the URL info
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
        """
        current_crawl_num = 0
        self.crawl(self.start_url, current_crawl_num)

    def crawl(self, url, current_crawl_num):
        """
        Crawl this url domain.
        Parameters:
            url (str): The url that this function will crawl and download information for.
            current_crawl_num = The number of pages that have been crawled so far.
        Returns:
            None.        
        """

    def report(self, start_time=None):
        """
        Print out a report for the user to aid in debugging and provide general statistics.
        Parameters:
            start_time (Datetime): The time at which we first started the crawl.
        Returns:
            None. Prints to standard output
        """
        current_time = time.time()
        print() #Buffer space
        print("----------UKY Spider----------")
        print("Number of (total) pages crawled:", len(self.closed_pool))
        print("Number of pages crawled this batch:", self.batch_interval)
        #print("Number of 'special links':", len(self.special_urls))
        print("Time since started: " + str(round(current_time - start_time, self.time_decimal)) + " seconds")
        print('\n'*5)


        


