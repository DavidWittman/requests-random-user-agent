import unittest

import requests
import requests_random_user_agent

class TestRandomUserAgent(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()

    def test_user_agent_is_not_default(self):
        self.assertNotIn(
            "python-requests",
            self.session.headers['User-Agent']
        )

    def test_user_agent_is_random(self):
        # TODO(dw): This will occasionally fail because it can
        # randomly pick the same UA twice
        self.assertNotEqual(
            self.session.headers['User-Agent'],
            requests.Session().headers['User-Agent']
        )
