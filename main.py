# -*- coding: utf-8 -*-
from batch.twitter import twitter
from batch.google import googleblog , youtube , googleopensocial
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

import time
a = googleopensocial(["atlasjet.com"])
a.search()
    
