# -*- coding: utf-8 -*-
from plugins.httpOpen import hcon
import time
import sqlite3
import re
from plugins.generals import *

class twitter():

    def __init__(self,firm):
        self.opener = hcon()
        con = sqlite3.connect("%s.sqlite" % firm)
        con.isolation_level = None
        self.cur = con.cursor()

        try:
            self.cur.execute("""
            CREATE  TABLE "tweet" ("id" INTEGER PRIMARY KEY  AUTOINCREMENT  NOT NULL  UNIQUE , "date" DATETIME, "text" TEXT, "from_user" VARCHAR, "from_user_id" INTEGER, "retweet" INTEGER DEFAULT 0)

            """)
            self.cur.execute("""CREATE  TABLE "prop" ("last_check" INTEGER, "refresh_url" VARCHAR, "fetchcount" INTEGER)""")
            self.cur.execute("""ALTER TABLE "tweet" ADD COLUMN "url" VARCHAR""")
            self.cur.execute("""ALTER TABLE "tweet" ADD COLUMN "url_title" VARCHAR""")
        except:
            pass
    def getSearch(self,page):
        data =  self.opener.gJSON(page)
        return data

    def search(self,keyword):



        self.cur.execute("select last_check,refresh_url from prop")
        row = self.cur
        url = ""
        update = 1
        for rr in row:
            url = "http://search.twitter.com/search.json%s" % rr[1]

        if url == "":
            update = 0
            url = "http://search.twitter.com/search.json?q="+keyword+"&rpp=100"



        data =  self.getSearch(url)

        #print data
        #print len(data['results'])
        if update == 1:
            self.cur.execute("update prop set refresh_url = '%s'" % data['refresh_url'])
        else:
            self.cur.execute("insert into prop (refresh_url) values ('%s')" % data['refresh_url'])

        url_count = 0
        total = 0
        print data
        for twit in data['results']:
            #print twit
            total = total + 1
            text =  unicode(twit['text'])
            #print twit['from_user']
            #print text
            print "-" * 20
            #print twit['created_at']
            retw = 0
            if twit['text'].find("RT @") > -1:
                retw = 1
           
            urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
            title = ""
            url = ""
            if len(urls) > 0:
                try:
                    title = unicode(gettitle(urls[0]),"utf-8")
                except:
                    pass
                url = urls[0]
            dd =  time.strptime(twit['created_at'], "%a, %d %b %Y %H:%M:%S +0000")
            #print twit
            self.cur.execute(u"""insert into tweet (url, url_title , date , from_user , from_user_id  ,retweet,text) values ("%s","%s",'%d-%d-%d','%s',%d,%d,"%s")""" % (url,title,dd.tm_year,dd.tm_mon,dd.tm_mday,twit['from_user'],twit['from_user_id'],retw,text))
            
                
            
            #print text
            if text.find("http://") > -1:
                url_count = url_count + 1
        if "next_page" in data:
            elm = True

            #print "next 20"
            while elm:
                #print "http://search.twitter.com/search.json"+data['next_page']
                data =  self.getSearch("http://search.twitter.com/search.json"+data['next_page'])
                
                for twit in data['results']:
            #print twit

                    #print twit
                    total = total + 1
                    text =  unicode(twit['text'])
                    #print twit['from_user']
                    #print text
                    print "-" * 20
                    #print twit['created_at']
                    retw = 0
                    if twit['text'].find("RT @") > -1:
                        retw = 1

                    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
                    title = ""
                    url = ""
                    if len(urls) > 0:
                        try:
                            title = unicode(gettitle(urls[0]),"utf-8")
                        except:
                            pass
                        url = urls[0]
                    dd =  time.strptime(twit['created_at'], "%a, %d %b %Y %H:%M:%S +0000")
                    #print twit
                    self.cur.execute(u"""insert into tweet (url, url_title , date , from_user , from_user_id  ,retweet,text) values ("%s","%s",'%d-%d-%d','%s',%d,%d,"%s")""" % (url,title,dd.tm_year,dd.tm_mon,dd.tm_mday,twit['from_user'],twit['from_user_id'],retw,text))
                    if text.find("http://") > -1:
                        url_count = url_count + 1
        
                if "next_page" in data:
                        elm = True
                        #print "next 20"
                else:
                        elm = False
                print "total : %d" % total
                print "url : %d" % url_count




        self.cur.execute("select date , count(id) as total from tweet group by date order by date")
        for row in self.cur:
            print row[0],row[1]

        self.cur.execute("select from_user , count(id) as total from tweet group by from_user order by total desc")
        for row in self.cur:
            print row[0],row[1]


        self.cur.execute("select url , url_title, count(id) as total from tweet where url_title != '' group by url order by total desc ")
        for row in self.cur:
            print row[0],unicode.encode(row[1],"utf-8"),row[2]
            


        print "total : %d" % total
        print "url : %d" % url_count



