# -*- coding: utf-8 -*-
"""
fouyi crawler

@author : Gestalt Lur

@copyright : Copyright 2013, The Fouyi Project

@license : GPL

@version : 0.0.1

@email : youranl@acm.org

@date : 2013-08-07
"""

import logging
import json
from datetime import datetime

import pymongo as pym

from tweetunity.request_timeline import get_tweet_by_id

class FouyiCrawler():
    def __init__(self, tweet_id):
        self.tweet_id = tweet_id

    def crawl(self):
        tweet = get_tweet_by_id


if __name__ == '__main__':
    pass
