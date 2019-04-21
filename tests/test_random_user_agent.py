import unittest

import requests
import requests_random_user_agent

class TestRandomUserAgent(unittest.TestCase):
    def test_user_agent_is_not_default(self):
        session = requests.Session()
        user_agent = session.headers['User-Agent']
        self.assertNotIn("python-requests", user_agent)

    def test_user_agent_is_random(self):
        # TODO(dw): This will occasionally fail because it can
        # randomly pick the same UA twice
        session = requests.Session()
        user_agent_1 = session.headers['User-Agent']
        session = requests.Session()
        user_agent_2 = session.headers['User-Agent']
        self.assertNotEqual(user_agent_1, user_agent_2)
