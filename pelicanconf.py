#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Velaron'
SITENAME = 'blog.bds'
SITESUBTITLE = 'i have crippling depression'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('blog', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme
THEME = 'themes/pelican-alchemy/alchemy'
THEME_CSS_OVERRIDES = ['theme/css/oldstyle.css']
THEME_TEMPLATES_OVERRIDES = ['templates']

# Bootstrapify
PLUGIN_PATHS = ['plugins']
PLUGINS = ['pelican-bootstrapify']

BOOTSTRAPIFY = {
    'table': ['table', 'table-striped', 'table-hover'],
    'img': ['img-fluid'],
    'blockquote': ['blockquote'],
}

# Favicon
RFG_FAVICONS = True
EXTRA_PATH_METADATA = {
    'extras/android-chrome-192x192.png': {'path': 'android-chrome-192x192.png'},
    'extras/android-chrome-512x512.png': {'path': 'android-chrome-512x512.png'},
    'extras/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
    'extras/browserconfig.xml': {'path': 'browserconfig.xml'},
    'extras/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extras/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
    'extras/site.webmanifest': {'path': 'manifest.json'},
    'extras/mstile-150x150.png': {'path': 'mstile-150x150.png'},
    'extras/safari-pinned-tab.svg': {'path': 'safari-pinned-tab.svg'}
}

# Misc
STATIC_PATHS = ['extras', 'images']
DEFAULT_CATEGORY = "Uncategorized"
DESCRIPTION = 'welcome to the bodis zone'

# Utterances
UTTERANCES_REPOSITORY = 'Velaron/velaron.github.io'
UTTERANCES_THEME = 'github-light'