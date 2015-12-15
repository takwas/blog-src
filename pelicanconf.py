#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tosin Damilare James Animashaun'
SITENAME = u'Volatile Musings of Ace Takwas'
SITEURL = 'http://takwas.github.io'

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


TWITTER_USERNAME = 'acetakwas'

# Blogroll
LINKS = (('Github', 'github.com/takwas'),
         ('Bitbucket', 'bitbucket.org/takwas'),
         ('Powered by Pelican', 'getpelican.com/'),)
         

# Social widget
SOCIAL = (('Quora', 'quora.com/Tosin-Damilare-James-Animashaun:'),
          ('Goodreads', 'goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),
          ('Facebook', 'facebook.com/takwas'),
          ('Twitter', 'twitter.com/acetakwas'),
          ('Google+', 'plus.google.com/+TosinAnimashaun/about?hl=en_GB'),)
          #('Youtube', 'youtube.com/acetakwas'),)


DEFAULT_PAGINATION = 7



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
THEME = "pelican_themes/hyde"
MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
DESCRIPTION = 'Pen your thoughts ... they are volatile'