#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bradlee Speice'
SITENAME = u'Bradlee Speice'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/bspeice'),
        ('LinkedIn', 'https://www.linkedin.com/in/bradleespeice'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['pelican-plugins/']
PLUGINS = ['liquid_tags.notebook']
NOTEBOOK_DIR = 'notebooks'

THEME='nest'
#NEST_INDEX_HEADER_TITLE="Bradlee Speice"
NEST_INDEX_HEADER_SUBTITLE="Exploring the intersection of Computer Science and Financial Engineering"
NEST_HEADER_LOGO="images/logo.svg"
