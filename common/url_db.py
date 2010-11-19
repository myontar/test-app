# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="John"
__date__ ="$19.Kas.2010 01:13:39$"
import sqlite3
from plugins.generals import *
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class urldb():
    def __init__(self):
        con = sqlite3.connect("db/url_grab.sqlite")
        con.isolation_level = None
        self.cur = con.cursor()


    def adddb(self,url,from_url,from_service,service_id,from_domain):
        domain = self.parsedomain(url)
        self.cur.execute(""" insert into urllist (url,from_url,from_service,service_id,domain,from_domain) values ('%s','%s','%s','%s','%s','%s') """ % (url,from_url,from_service , service_id , domain,from_domain))

    #def addkey(self,url,keyword,from_service,service_id):
        

    def parsedomain(self,url):
        data =  url.split("://")[1].split("/")[0]
        data = data.split(".")
        return data[len(data)-2] + "." + data[len(data)-1]
