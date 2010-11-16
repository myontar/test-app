import urllib
import urllib2
import re
from cookielib import CookieJar, DefaultCookiePolicy
import json

class hcon():

    def __init__(self):
        cj = CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        self.opener = opener

    def getUrl(self,url,param=None):
        r = self.opener.open(url)
        return r.read()

    def gJSON(self,url,param=None):
        r = self.opener.open(url)
        data =  r.read()
        return json.loads(data)


