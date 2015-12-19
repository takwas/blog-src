#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from hashlib import md5



SITENAME = u'ac3Takwas | reBLOGitations'
DESCRIPTION = u'Pen your thoughts ... they are volatile'
SITE_TAGLINE = DESCRIPTION
SITE_SOURCE = u'https://github.com/takwas/blog-src'
BIO = u'Christian, Programmer, Quoracious reader'
AUTHOR = u'Tosin Damilare James Animashaun'
AUTHOR_SHORTBIO = BIO
AUTHOR_EMAIL = u'acetakwas@gmail.com'
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL).hexdigest()
TWITTER_USERNAME = u'acetakwas'
GITHUB_USERNAME = u'takwas'
GITHUB_BADGE = True


# During development, we want urls to be relative
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'Uncategorized'

TIMEZONE = 'Africa/Lagos'

PATH = 'content/'
#ARTICLE_DIR = PATH


# Feed generation is usually not desired when developing
FEED_ATOM = None #'feeds/main.atom.xml'
FEED_RSS = None #'feeds/main.rss.xml'
FEED_ALL_ATOM = None
FEED_ALL_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
CATEGORY_FEED_ATOM = None
CATEGORY_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None
TRANSLATION_FEED_ATOM = None
TRANSLATION_FEED_RSS = None



# metadata information: date and slug data from filename
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'



SOCIAL_WIDGET_NAME = "Web Hangouts"
LINKS_WIDGET_NAME = "Bookmarks"

GRAB_ICONS = True

# Blogroll
LINKS = (('Blog', '#0'),)

# Social widget
SOCIAL = (
	('quora', 'http://quora.com/Tosin-Damilare-James-Animashaun'),
	('github', 'http://github.com/takwas'),
	('bitbucket', 'http://bitbucket.org/takwas'),
	('goodreads', 'http://goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),)
          
          #('Facebook', 'http://facebook.com/takwas')
          #('Twitter', 'http://twitter.com/acetakwas'),
          #('Google+', 'http://plus.google.com/+TosinAnimashaun/about?hl=en_GB')
          #('Youtube', 'youtube.com/acetakwas'),)




DEFAULT_PAGINATION = 7







# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
THEME = 'plumage'
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']


# Load thumbnail locally for development
SITE_THUMBNAIL = '/theme/img/avatar_acetakwas.jpg'
SITE_THUMBNAIL_TEXT = \
	'''
		A pen in hand,
		speaks volumes
	'''


MENUITEMS = [('Home', '/'), ('About', '/') ]

SITESUBTITLE = DESCRIPTION

