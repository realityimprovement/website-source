#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Alistair Magee'
SITENAME = 'Reality Improvement'
SITESUBTITLE = 'A Blog and some Comics'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
SUBCATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

MENUITEMS = [('Home', 'http://www.realityimprovement.com')]

# Blogroll
LINKS = (
         ('Dresden Codak', 'http://dresdencodak.com/'),
         ('XKCD', 'http://xkcd.com'),
         ('Dinosaur Comics', 'http://www.qwantz.com/'),
         ('Questionable Content', 'http://questionablecontent.net'),
         ('Saturday Morning Breakfast Cereal', 'http://www.smbc-comics.com/'),
         ('Something Positive', 'http://somethingpositive.net/'),
         ('Extra Ordinary', 'http://www.exocomics.com/'),
         ('Order of the Stick', 'http://www.giantitp.com/Comics.html'),
         ('Hyperbole and a half', 'http://hyperboleandahalf.blogspot.com/'),
         ('Twenty Sided', 'http://www.shamasyoung.com/twentysidedtale'),
         ('Citizen Radio', 'http://wearecitizenradio.com'),
         ('Nerdist', 'http://www.nerdist.com/podcast/nerdist'),
         ('The Tod Glass Show', 'http://www.nerdist.com/podcast/the-todd-glass-show/'),
         )

# Social widget
SOCIAL = (('My Twitter', 'twitter.com/alistairmagee'),
          ('More photos on my Flikr', 'www.flikr.com/photos/alistairmagee'),)

DEFAULT_PAGINATION = 10

THEME = 'theme/flex'


PLUGIN_PATH = '/home/alistair/development/waterbird/pelican-plugins'
PLUGINS = ['summary', 'subcategory', 'custom_article_urls', 'clean_summary', 'neighbors']

#PLUGIN SETTINGS

SUBCATEGORY_URL = ('{fullurl}/')
SUBCATEGORY_SAVE_AS = os.path.join('{savepath}', 'index.html') 

CUSTOM_ARTICLE_URLS = {
    'Comic/One Shots' : {'URL': 'one-shot-comics/{slug}/', 
            'SAVE_AS': os.path.join('one-shot-comics', '{slug}', 'index.html')},
    }

CLEAN_SUMMARY_MAXIMUM = 0
CLEAN_SUMMARY_MINIMUM_ONE = False


#STANDARD SETTINGS

STATIC_PATHS = ['images', 'wp-content', 'theme/flex/assests']
ASSET_SOURCE_PATHS = ('theme/flex/static/css',)

ARTICLE_URL = '{date:%Y}/{date:%B}/{slug}/'
ARTICLE_SAVE_AS = os.path.join('{date:%Y}', '{date:%B}', '{slug}', 'index.html')

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = os.path.join('{slug}', 'index.html')

CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = os.path.join('{slug}', 'index.html')

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = os.path.join('tag', '{slug}', 'index.html')

DEFAULT_CATEGORY = 'random'
USE_FOLDER_AS_CATEGORY = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
