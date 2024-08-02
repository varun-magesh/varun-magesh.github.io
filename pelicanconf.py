AUTHOR = 'Varun Magesh'
SITENAME = 'Varun Magesh'
# SITEURL = "http://localhost:8000"
SITEURL = "https://varun-magesh.github.io"
STATIC_PATHS = ['./images', './themes/simple/static', './static']
MENUITEMS = (
    ('Kitchen', '/category/kitchen.html'),
    # ('Research', '/pages/research.html'),
    ('GitHub', 'https://github.com/varun-magesh'),
    ('LinkedIn', 'https://www.linkedin.com/in/varun-magesh/'),
)
CATEGORY_TITLES = {
    'kitchen': 'Notes from the Kitchen',
    'research': 'Research',
}
PATH = "content"

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = "themes/simple"
