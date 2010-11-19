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
    request = urllib2.Request(url)
    import openanything, httplib
    httplib.HTTPConnection.debuglevel = 1
    opener = urllib2.build_opener(
         openanything.SmartRedirectHandler())
    f = opener.open(request)


    try:#print data
        r = opener.open(url)
        data =  r.read()
        title = re.search('<title>(.*)</title>', data, re.IGNORECASE).group(1)
    except:
        pass
    if f.status == 301:
        return {"title":title,"url":f.url}
    else:
        return {"title":title,"url":url}
    #print title
