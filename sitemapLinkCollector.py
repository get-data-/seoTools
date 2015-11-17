# -*- coding: utf-8 -*-
"""
This script takes a sitemap and parses the URLs between <loc></loc> tags.
It stores them into a .csv file in a single column.
"""
from bs4 import BeautifulSoup
import requests
import urllib2 as ur
import re
import csv
sitemapLinks = []
sitemapLoc = raw_input('Enter the location of the sitemap:')
r = requests.get(sitemapLoc)
xml = r.text
links = raw_input('choose a location and file name to save output as csv \n')
soup = BeautifulSoup(xml)
sitemapTags = soup.find_all("sitemap")
nSitemaps = "The number of sitemaps are {0}".format(len(sitemapTags))
#this part is about checking how many sitemaps are within the sitemap
print "The number of sitemaps are {0}".format(len(sitemapTags))
def main():
    if nSitemaps == "The number of sitemaps are 0":
# The first condition is parsing instructions if there are no sitemaps within
# the sitemap that was entered as the sitemapLoc
#       print sitemapLoc
        f = ur.urlopen(sitemapLoc)
        res = f.readlines()
        for d in res:
            data = re.findall('<loc>(http:\/\/.+)<\/loc>',d)
            for i in data:
                sitemLinks.append(i)                
        with open(links,'wb') as fp:
            writer = csv.writer(fp, delimiter='\n')
            writer.writerow(sitemapLinks)
        fp.close()
    else:
# the else condition handles URL parsing for multiple sitemaps within an index.
        for sitemap in sitemapTags:
            print "Currently parsing"+ sitemap.findNext("loc").text
            f = ur.urlopen(sitemap.findNext("loc").text)
            res = f.readlines()
            for d in res:
                data = re.findall('<loc>(http:\/\/.+)<\/loc>',d)
                for i in data:
                    sitemapLinks.append(i)                
            with open(links,'wb') as fp:
                writer = csv.writer(fp, delimiter='\n')
                writer.writerow(sitemapLinks)
            fp.close()
main()
