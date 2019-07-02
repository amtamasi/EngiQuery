# EngiQuery
EngiQuery is a search engine built for the University of Kentucky's web domain.    

## Motivation
This web crawler was originally built for CS 485-002 (Web Crawling Techniques and Applications) at the University of Kentucky under Dr. 
Brent Seales, with the purpose of indexing, ranking, and searching the engineering subdomain. This initial system crawled over 3000 pages in the engineering subdomain, tracking over 500,000 links between web pages. EngiQuery ranked these web documents and returned relevant pages based on a query supplied by the user.  

It has since been co-opted to be a search engine for all of the UK domain by improving the original structure for crawling, indexing, and searching. I really enjoyed this project during the class, and wanted to expand upon it. I had the highest reported peak crawl speed in the class, but it was only around 7 pages crawled per second. I wanted to build on that to make it faster and more generalized, so that I could quickly crawl any website of interest (but particularly the UK domain).  

I was also interested in learning about multi-threading, and felt this would be a good opportunity to do so.


## Files
  * pagecrawler.py - My implementation for a web crawler. Right now, this crawler is semi-tailored towards engr.uky.edu and the issues that arose while dealing with that particular domain. 
  
  * pagerank.py - My implementation for Google's PageRank algorithm. This implementation takes an adjacency matrix representation of a web link graph and calculates the PageRank vector using the Power Method/Iteration. 
  
  
## Future Improvements
  1. Implement "politeness". Crawler should respect robots.txt files.
  2. Make the crawler and URL classes more generalized. The URL class should contain any information you need about a URL
     The crawler class should be able to hold more information about the particular crawl. In addition, the crawler should be able to 
     crawl ANY URL, not just be tailored toward the engr.uky.edu subdomain.
  3. Find ways to make the crawler run faster (more pages crawled / second)
  4. Make the crawler more robust, less prone to errors. In particular, the main try/except statement is not conducive to debugging
     because the crawler can fail in multiple places. The try statement should include less than it does to isolate issues/errors.
  5. Storage of url information should be efficient and more purposeful
  6. Build a class for the section of code that is for the query search functionality. This is messy and can be cleaned up.
  7. On the same note, be more intentional with the design of the query search section. Work on this in tandem with the next avenue (8).
  8. Identify which data structures can be changed out to aid in optimization (e.g. changing a list to a hash table).
  9. Increase modularity. Separate the files for PageRank, the crawler, information retrieval methods, and the query engine.
