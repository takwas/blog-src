#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *


SITEURL = 'http://takwas.github.io'
# During production, we do not want urls to be relative,
# they should instead be relative to <SITEURL> above
RELATIVE_URLS = False


# Feeds config
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
#FEED_MAX_ITEMS

DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


# Load gravatar for production
SITE_THUMBNAIL = "http://www.gravatar.com/avatar/{0}.jpg?s=80&r=g&d=identicon".format(AUTHOR_EMAIL_HASH)