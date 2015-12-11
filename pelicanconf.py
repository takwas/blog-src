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

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 7



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for theme
THEME = "pelican_themes/pelican-themes/monospace"
MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']
DESCRIPTION = 'Pen your thoughts ... they are volatile'