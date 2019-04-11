from django.test import TestCase
from django.test import Client


class TestDjangoGlobalRequest(TestCase):

    def test_01(self):
        browser = Client()
        response = browser.get("/test/")
        assert response.content == b'OK'
