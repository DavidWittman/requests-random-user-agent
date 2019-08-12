import os
import random

import requests.utils

__version__ = "0.0.13"

USER_AGENTS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'useragents.txt')
with open(USER_AGENTS_FILE) as fh:
    USER_AGENTS = fh.read().splitlines()

requests.utils.default_user_agent = lambda: random.choice(USER_AGENTS)
