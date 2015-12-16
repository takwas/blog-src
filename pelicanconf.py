#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tosin Damilare James Animashaun'
SITENAME = u'Volatile Musings of Ace Takwas'


# During development, we want urls to be relative
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

DEFAULT_CATEGORY = 'Uncategorized'

TIMEZONE = 'Africa/Lagos'

PATH = 'content'


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

TWITTER_USERNAME = 'acetakwas'

# Blogroll
LINKS = (('Powered by Pelican', 'http://getpelican.com/'))
         

# Social widget
SOCIAL = (
	('github', 'http://github.com/takwas'),
	('bitbucket', 'http://bitbucket.org/takwas'),
	('quora', 'http://quora.com/Tosin-Damilare-James-Animashaun'),
	('goodreads', 'http://goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),)
          
          #('Facebook', 'http://facebook.com/takwas')
          #('Twitter', 'http://twitter.com/acetakwas'),
          #('Google+', 'http://plus.google.com/+TosinAnimashaun/about?hl=en_GB')
          #('Youtube', 'youtube.com/acetakwas'),)


BIO = "Programmer, Quoracious reader, Christian"

DEFAULT_PAGINATION = 7



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
THEME = "hyde"
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
DESCRIPTION = 'Pen your thoughts ... they are volatile'