# Production settings, used by `make publish` and `make github`.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *  # noqa: F401,F403,E402

SITEURL = "https://theartofkubernetes.com"
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = "feeds/all.atom.xml"

DELETE_OUTPUT_DIRECTORY = True
