# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="John"
__date__ ="$18.Kas.2010 22:20:10$"
import urllib2
import json

class googleblog():
    def __init(self,ley):
        leys = ley


    def getData(self,key,start):
        url = ('https://ajax.googleapis.com/ajax/services/search/blogs?' +
               'v=1.0&q='+key+'&rsz=8&start='+str(start)+'&key=ABQIAAAAdQEJ3-SLT17i-QKlcZXgwxS0B64ZYAla_DwzCZJThz2xnq87gBSDmBK2DKsNn4o9201-JKCkiXjiUw&userip=127.0.0.1')

        request = urllib2.Request(url, None, {'Referer': "http://www.mstfyntr.com"})
        response = urllib2.urlopen(request)

        # Process the JSON string.
        results = json.load(response)
        #print results
        return results
    def search(self,key):
        results = self.getData(key,0)
        self.searchWrite(results['responseData']['results'])
        t = len(results['responseData']['cursor']['pages']) - 1
        for i in range(1,t):
            page = results['responseData']['cursor']['pages'][i]['start']

            results = self.getData(key,page)
            self.searchWrite(results['responseData']['results'])
             
        

    def searchWrite(self,results):
        for i in results:
            url     = i['blogUrl']
            date    = i['publishedDate']
            title   = i['titleNoFormatting']
            content = i['content']
            postUrl = i['postUrl']
            print postUrl
            print title

