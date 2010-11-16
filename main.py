# -*- coding: utf-8 -*-
from batch.twitter import twitter
import time
a = twitter("mynet_main")
while True:
    a.search("mynet")
    time.sleep(600)
