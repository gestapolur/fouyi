# -*- coding: utf-8 -*-
""" fouyi crawler request handler for flask """

import logging
import json

from flask import Flask
from flask import render_template
from flask import request

__author__ = "Gestalt Lur"
__copyright__ = "Copyright 2013, The Fouyi Project"
__license__ = "GPL"
__version__ = "0.0.1"
__email__ = "youranl@acm.org"

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/post_tweet_id', methods=['POST'])
def CrawlerHandler():
    crawler = FouyiCrawler( tweet_id )
    return render_template('index.html')

@app.route('/', methods=['POST', 'GET'])
def MainPage():
    return render_template('index.html')


if __name__ == '__main__':
    # app.debug = True
    # app.run()
    tweet_id = long(raw_input())
    c = FouyiCrawler( tweet_id )
    c.crawl()
