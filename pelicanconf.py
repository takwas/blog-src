#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from hashlib import md5


SITENAME = u'acetakwas.log();'
DESCRIPTION = r"while True: print    <strong>\</strong>"
SITE_TAGLINE = DESCRIPTION
SITE_SOURCE = u'https://github.com/takwas/blog-src'

AUTHOR = u'Tosin Damilare James Animashaun'


# # helper function to format URLs for BIO
# def get_link(name):
# 	return ('<a href="{url}">{url_title}</a>'
# 			''.format(url=URLS.get(name, '')[0],
# 					  url_title=URLS.get(name, '')[1]))


BIO = (
	u'''
		<p>I'm Tosin Animashaun, a Nigerian, and in here is where I document 
		stuff as I go. </p>
		
		<p>I currently contribute to the technical efforts at 
		<a href="{ta}">TechAdvance</a>, a software development outfit out of 
		Nigeria, that has got her feet in the <a href={pay}>payments</a> and 
		<a href="{trp}">transportation</a> spaces, as well as in the 
		digitisation of government services.</p>
		
		<p>I have previously delved into entrepreneurship with a group of 
		friends at <a href="{krohx}">Krohx</a>, but I am currently on hiatus 
		from this. I have also somewhat unofficially interned with 
		<a href="{niit}">NIIT</a>.</p>

		<p>Aside from my <a href="{dayjob}">day job as a backend developer</a>, 
		I spend a lot of my non-work time <a href="{learning}">garnering more 
		general knowledge</a> as fueling for my autodidact persona. I like to 
		read well written content, and I occasionally try my hands at crafting 
		good stuff like I am doing with this space.
		
		Some other interests of mine include music, art, and psychology.
		</p>

		<p>I am also an avid podcast listener. My listening areas of interest 
		include: technology, psychology and history among others.
		
		</p>
		
		<p>Being an autodidact, I do not possess a college degree -- I do not 
		completely believe in its efficacy -- as I have so far failed at two 
		attempts to obtain at least one.</p>
		
		<p>
		<br/><b>You can email me at </b> acetakwas [at] gmail [dot] com
		</p>
		'''
).format(ta='http://www.techadvance.ng/',
		 pay='http://www.gpayafrica.com/',
		 trp='http://www.bus.com.ng/',
		 krohx='http://krohx.github.io/',
		 niit='http://niitlagos.com/',
		 dayjob='http://ng.linkedin.com/in/acetakwas',
		 learning='http://tosinmash.com/article/wholesome-learning.html')


AUTHOR_SHORTBIO = u'Christian | Programmer | Learner'
AUTHOR_EMAIL = u'acetakwas@gmail.com'
AUTHOR_EMAIL_HASH = md5(AUTHOR_EMAIL.encode('utf-8')).hexdigest()
TWITTER_USERNAME = u'acetakwas'
GITHUB_USERNAME = u'takwas'
GITHUB_URL = u'https://github.com/takwas'
GITHUB_BADGE = True

# LANDING_PAGE_ABOUT = {
# 	'title': SITENAME,
# 	'details': BIO
# }

# PROJECTS = [
# 	{
# 		'name': 'Slack Electioneer (Votebot)',
# 		'url': 'https://github.com/takwas/slack-electioneer',
# 		'description': 'An election conducting Slack bot.'
# 	},
#
# 	{
# 		'name': 'Contact Form',
# 		'url': 'https://github.com/Krohx/contactform',
# 		'description': 'Contact-Us-Form backend for static websites.'
# 	},
#
# 	{
# 		'name': 'Flask App Template',
# 		'url': 'https://github.com/takwas/flask_app_template',
# 		'description': 'A boilerplate codebase for Flask that I wrote when I '
# 					   'first started out with Flask.'
# 	}
# ]

# COMMENTS_INTRO = 'Comments Intro'
STATIC_PATHS = ['theme/images', 'images']

# custom config variable for IRC
IRC_NICK = u'acetakwas'


# During development, we want urls to be relative
RELATIVE_URLS = True

DEFAULT_LANG = u'en'

# Whether folders in "content" should represent categories
USE_FOLDER_AS_CATEGORY = True

DEFAULT_CATEGORY = 'Uncategorized'
DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True

DEFAULT_DATE_FORMAT = '%a %d %B %Y'
TIMEZONE = 'Africa/Lagos'

# DEFAULT_METADATA = ()
# FILENAME_METADATA = '(?P<slug>.*)'  # Extract slug from filename

PATH = 'content/'  # Top-level diretory in which to find content
IGNORE_FILES = ['drafts']  # File or directory patterns to ignore processing
#ARTICLE_DIR = PATH

# IGNORE_FILES = ['.#*', '*.bak']

# SITEURL = 'https://tosinmash.com'

# FEED_DOMAIN = SITEURL
# FEED_ATOM = 'feeds/main.atom.xml'
# FEED_RSS = 'feeds/main.rss.xml'
# FEED_ALL_ATOM = 'feeds/all.atom.xml'
# FEED_ALL_RSS = 'feeds/all.rss.xml'
# CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
# CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
# TAG_FEED_ATOM = 'feeds/%s.atom.xml'
# TAG_FEED_RSS = 'feeds/%s.rss.xml'

# Feed generation is usually not desired when developing
# FEED_ATOM = None #'feeds/main.atom.xml'
# FEED_RSS = None #'feeds/main.rss.xml'
# FEED_ALL_ATOM = None
# FEED_ALL_RSS = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None
# CATEGORY_FEED_ATOM = None
# CATEGORY_FEED_RSS = None
# TAG_FEED_ATOM = None
# TAG_FEED_RSS = None
# TRANSLATION_FEED_ATOM = None
# TRANSLATION_FEED_RSS = None


# metadata information: date and slug data from filename
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'


# SOCIAL_WIDGET_NAME = "Find me on"
# LINKS_WIDGET_NAME = "Bookmarks"

GRAB_ICONS = True

# Blogroll
#LINKS = (('Blog', '#0'),)

# Social widget
SOCIAL = (
	('github', 'http://github.com/takwas'),
	('linkedin', 'http://ng.linkedin.com/in/acetakwas'),
	('quora', 'http://quora.com/Tosin-Damilare-James-Animashaun'),
	('goodreads', 'http://goodreads.com/user/show/41177369-tosin-damilare-james-animashaun'),
	('bitbucket', 'http://bitbucket.org/takwas'),
	('twitter', 'http://twitter.com/acetakwas'),
	# ('facebook', 'http://facebook.com/takwas'),
)

LINKS = SOCIAL

#('Facebook', 'http://facebook.com/takwas')
#('Twitter', 'http://twitter.com/acetakwas'),
#('Google+', 'http://plus.google.com/+TosinAnimashaun/about?hl=en_GB')
#('Youtube', 'youtube.com/acetakwas'),)


DEFAULT_PAGINATION = 200


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


# Settings for current theme
# THEME = 'plumage_takwas'
# THEME = 'themes/plumage_takwas'

# THEME = 'pure'

THEME = 'sundown'
THEME = 'sundown_custom'
THEME = 'my_themes/sundown_custom'

# THEME = 'mediumfox'

# THEME = 'Flex'  # red-themed; profile info left side-bar

# THEME = 'elegant'
# THEME = 'alchemy'
# THEME = 'apricot'
# THEME = 'built-texts'
# THEME = 'dev-random3'
# THEME = 'hyde'
# THEME = 'iris'
# THEME = 'Just-Read'
# THEME = 'MinimalXY'
# THEME = 'mnmlist'
# THEME = 'monospace'
# THEME = 'Nuja'
# THEME = 'pelican-simplegrey'
# THEME = 'pelican-sober'
# THEME = 'taman'
# THEME = 'graymill'
# THEME = 'medio'

#MD_EXTENSIONS = ['codehilite(css_class=codehilite code)']


# Load thumbnail locally for development
# SITE_THUMBNAIL = '/theme/img/avatar_acetakwas.jpg'
# SITE_THUMBNAIL_TEXT = 'A pen in hand speaks volumes.'


# MENUITEMS = (
# 	('Home', '/'),
# 	#(''),
# 	#('Being Christian', '/'),
# 	('Tosinmash', '#about'),
# )

# Extra Jinja2 Pages to be rendered alongside blog content
# TEMPLATE_PAGES = {'src/books.html': 'dest/books.html',
#                   'src/resume.html': 'dest/resume.html',
#                   'src/contact.html': 'dest/contact.html'}

TEMPLATE_PAGES = {
	# 'pages/about-template.html': 'about.html'
}

EXTRA_PATH_METADATA = {
	'theme/images/favicon.ico': {'path': 'favicon.ico'}
}

SITESUBTITLE = SITE_TAGLINE

# DISCLAIMER = False


# # Support for Disqus comments
# DISQUS_SITENAME = 'acetakwas-log'


# ELEGANT THEME CONFIGS

# PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
# MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
# DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))

# STATIC_PATHS = ['theme/images', 'images']
# TAG_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''
# AUTHOR_SAVE_AS = ''

# RECENT_ARTICLES_COUNT (integer)
# COMMENTS_INTRO ('string')
# SITE_LICENSE ('string')
# SITE_DESCRIPTION ('string')
# EMAIL_SUBSCRIPTION_LABEL ('string')
# EMAIL_FIELD_PLACEHOLDER ('string')
# SUBSCRIBE_BUTTON_TITLE ('string')
# MAILCHIMP_FORM_ACTION ('string')
# SITESUBTITLE ('string')
# LANDING_PAGE_ABOUT ({})
# PROJECTS ([{},...])


# SUNDOWN THEME CONFIGS
import urllib.parse

EMAIL = AUTHOR_EMAIL
GRVTR_SIZE = 160
# DEFAULT_GRV_URL = ''

# construct gravatar URL
grvtr_base_url = 'http://www.gravatar.com/avatar/'
email_md5 = md5(EMAIL.lower().encode('utf-8')).hexdigest()
grvtr_query_str = urllib.parse.urlencode({'s': str(GRVTR_SIZE)})
GRV_URL = f'{grvtr_base_url}{email_md5}?{grvtr_query_str}'

WITH_FUTURE_DATES = False

PAGE_PATHS = ['pages']
# PAGE_URL = 'pages/{slug}'
# PAGE_SAVE_AS = 'pages/{slug}.html'
