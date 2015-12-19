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
SITE_FULL_URL = SITEURL
SITEROOT = '/'
# During production, we do not want urls to be relative,
# they should instead be relative to <SITEURL> above
RELATIVE_URLS = False


# Feeds config
FEED_DOMAIN = SITEURL
FEED_ATOM = 'feeds/main.atom.xml'
FEED_RSS = 'feeds/main.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
TAG_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_RSS = 'feeds/%s.rss.xml'
#FEED_MAX_ITEMS

# Do not delete the directory; it is git version-controlled
DELETE_OUTPUT_DIRECTORY = False

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""


# Load gravatar for production
SITE_THUMBNAIL = "http://www.gravatar.com/avatar/{0}.jpg?s=80&r=g&d=identicon".format(AUTHOR_EMAIL_HASH)



ARTICLE_URL = 'article/{slug}.html'
ARTICLE_SAVE_AS = 'article/{slug}.html'
CATEGORY_URL = 'category/{slug}.html'
CATEGORY_SAVE_AS = 'category/{slug}.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
CATEGORIES_SAVE_AS = 'categories.html'
TAGS_SAVE_AS = 'tags.html'
INDEX_SAVE_AS = 'index.html'

# YEAR_ARCHIVE_SAVE_AS = u'posts/{date:%Y}/{slug}/index.html'
# MONTH_ARCHIVE_SAVE_AS = u'posts/{date:%Y}/{date:%b}/{slug}/index.html' 
# DAY_ARCHIVE_SAVE_AS = u'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'