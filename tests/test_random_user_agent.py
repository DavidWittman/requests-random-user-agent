import re
import unittest

from http.client import _is_illegal_header_value

import requests
import requests_random_user_agent

class TestRandomUserAgent(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()

    def tearDown(self):
        self.session.close()

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

    def test_user_agent_values(self):
        for ua in requests_random_user_agent.USER_AGENTS:
            self.assertFalse(_is_illegal_header_value(ua.encode('utf8')), ua)

    def test_request(self):
        resp = self.session.get('https://httpbin.org/user-agent')

        self.assertEqual(resp.status_code, 200)
        user_agent = resp.json()['user-agent']

        self.assertEqual(
            self.session.headers['User-Agent'],
            user_agent
        )

        self.assertNotIn(
            "python-requests",
            user_agent
        )

    def test_request_without_session(self):
        resp = requests.get('https://httpbin.org/user-agent')

        self.assertEqual(resp.status_code, 200)
        user_agent = resp.json()['user-agent']

        self.assertIn(
            user_agent,
            requests_random_user_agent.USER_AGENTS
        )

        self.assertNotIn(
            "python-requests",
            user_agent
        )

    def test_request_different_without_session(self):
        # TODO(dw): This will occasionally fail because it can
        # randomly pick the same UA twice
        resp = requests.get('https://httpbin.org/user-agent')
        self.assertEqual(resp.status_code, 200)
        first_user_agent = resp.json()['user-agent']

        resp = requests.get('https://httpbin.org/user-agent')
        self.assertEqual(resp.status_code, 200)
        second_user_agent = resp.json()['user-agent']

        self.assertNotEqual(
            first_user_agent,
            second_user_agent
        )
