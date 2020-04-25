from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
import pytest
import time
from group import group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


class test_add_groups(unittest.TestCase):
    def setUp(self):
        self.app = Application

    def test_test_add_empty_group(self):
        wd = self.app.wd
        self.app.login(user='admin', password='secret')
        self.app.create_group(group(name='', header='', footer=''))
        self.app.logout()

    def test_test_add_group(self):
        wd = self.app.wd
        self.app.login(user='admin', password='secret')
        self.app.create_group(group(name='ljfsalrekj', header=';lkj', footer='lkjh'))
        time.sleep(1)
        self.app.logout()

    def tearDown(self):
        self.app.destroy()


if __name__ == '__main__':
    unittest.main()
