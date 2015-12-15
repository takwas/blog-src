#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tosin Damilare James Animashaun'
SITENAME = u'Volatile Musings of Ace Takwas'


# During development, we want urls to be relative
RELATIVE_URLS = True

PATH = 'content'

TIMEZONE = 'Africa/Lagos'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_CATEGORY = 'Uncategorized'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'


# metadata information: date and slug data from filename
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

TWITTER_USERNAME = 'acetakwas'

# Blogroll
LINKS = (('Powered by Pelican', 'http://getpelican.com/'))
         

# Social widget
SOCIAL = (
	('github', 'http://github.com/takwas'),
	('bitbucket', 'http://bitbucket.org/takwas'),
	('quora', 'http://quora.com/Tosin-Damilare-James-Animashaun:'),
	('google', 'http://goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),)
          
          #('Facebook', 'http://facebook.com/takwas')
          #('Twitter', 'http://twitter.com/acetakwas'),
          #('Google+', 'http://plus.google.com/+TosinAnimashaun/about?hl=en_GB')
          #('Youtube', 'youtube.com/acetakwas'),)


DEFAULT_PAGINATION = 7



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
THEME = "hyde"
#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
DESCRIPTION = 'Pen your thoughts ... they are volatile'