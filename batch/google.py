__author__="John"
__date__ ="$18.Kas.2010 23:49:01$"

import urllib2
import json
from plugins import feedparser
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from plugins.generals import *
from common.url_db import *




class youtube():
    key = None
    def __init__(self,keyword):
        self.key = keyword
    def search(self):
        d = feedparser.parse('http://gdata.youtube.com/feeds/api/videos?q='+self.key+'&v=2')
        for i in d.entries:
            user = i.author
            title =  i.title
            url = i.link
            print user , title , url

#open social 
class googleopensocial():
    domains = None
    def __init__(self,domains):
        self.domains = ','.join(domains)
        self.urldb = urldb()

    def getdata(self):
        url = ("http://socialgraph.apis.google.com/lookup?q="+self.domains+"&fme=1&edi=1&edo=1&pretty=1&callback=")
        print url
        request = urllib2.Request(url, None, {'Referer': "http://www.mstfyntr.com"})
        response = urllib2.urlopen(request)

        # Process the JSON string.
        results = json.load(response)
        #print results
        return results
    
    def search(self):
        data =  self.getdata()
        for i in data['canonical_mapping']:
            domain = i
            domain_ref = data['canonical_mapping'][i]
            domain_uri_list =data['nodes'][domain_ref]['unverified_claiming_nodes']
            for i in domain_uri_list:
                self.urldb.adddb(domain_ref,i,"googleopensco","",self.urldb.parsedomain(i))
            domain_uri_list =data['nodes'][domain_ref]['nodes_referenced']
            for i in domain_uri_list:
                #print i
                self.urldb.adddb(domain_ref,i,"googleopensco","",self.urldb.parsedomain(i))
            domain_uri_list =data['nodes'][domain_ref]['nodes_referenced_by']
            for i in domain_uri_list:
                self.urldb.adddb(domain_ref,i,"googleopensco","",self.urldb.parsedomain(i))


# Blog search api
class googleblog():
    def __init(self,ley):
        leys = ley


    def getdata(self,key,start):
        url = ('https://ajax.googleapis.com/ajax/services/search/blogs?' +
               'v=1.0&q='+key+'&rsz=8&start='+str(start)+'&key=ABQIAAAAdQEJ3-SLT17i-QKlcZXgwxS0B64ZYAla_DwzCZJThz2xnq87gBSDmBK2DKsNn4o9201-JKCkiXjiUw&userip=127.0.0.1')

        request = urllib2.Request(url, None, {'Referer': "http://www.mstfyntr.com"})
        response = urllib2.urlopen(request)

        # Process the JSON string.
        results = json.load(response)
        #print results
        return results
    def search(self,key):
        results = self.getdata(key,0)
        self.searchWrite(results['responseData']['results'])
        t = len(results['responseData']['cursor']['pages']) - 1
        for i in range(1,t):
            page = results['responseData']['cursor']['pages'][i]['start']

            results = self.getdata(key,page)
            self.searchwrite(results['responseData']['results'])



    def searchwrite(self,results):
        for i in results:
            url     = i['blogUrl']
            date    = i['publishedDate']
            title   = i['titleNoFormatting']
            content = i['content']
            postUrl = i['postUrl']
            print postUrl
            print title
