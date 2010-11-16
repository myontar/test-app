# -*- coding: utf-8 -*-
__author__="John"
__date__ ="$16.Kas.2010 01:34:16$"

import urllib2
import re
from cookielib import CookieJar


def gettitle(url):
    title = ""
    cj = CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
   
   
    try:#print data
        r = opener.open(url)
        data =  r.read()
        title = re.search('<title>(.*)</title>', data, re.IGNORECASE).group(1)
    except:
        pass
    return title
    #print title
