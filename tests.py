import unittest
from tornado.testing import AsyncHTTPTestCase
from tornado.httpclient import HTTPRequest
from tornado.ioloop import IOLoop
import time

import doorbot

class TestDoorbotApp(AsyncHTTPTestCase):
    def get_app(self):
        return doorbot.app

    def test_backdoor(self):
        response = self.fetch('/backdoor')
        self.assertEqual(response.code, 200)
        self.assertEqual(False, doorbot.controller.is_locked())
        self.io_loop.add_timeout(time.time() + 1.1, self.stop)
        self.wait()
        self.assertEqual(True, doorbot.controller.is_locked())

    def test_groupme(self):
        req = HTTPRequest(url=self.get_url('/callback'), method='POST', body='{"text": "unlock"}')
        self.http_client.fetch(req, self.stop)
        response = self.wait()
        self.assertEqual(response.code, 200)
        self.assertEqual(False, doorbot.controller.is_locked())
        self.io_loop.add_timeout(time.time() + 1.1, self.stop)
        self.wait()
        self.assertEqual(True, doorbot.controller.is_locked())
