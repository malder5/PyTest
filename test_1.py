from selenium.webdriver.chrome.webdriver import WebDriver
import unittest
import time
from group import group


class test_add_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
        self.wd.implicitly_wait(60)

    def test_test_add_empty_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)

        self.login(wd, user='admin', password='secret')

        self.create_group(wd, group(name='', header='', footer=''))
        time.sleep(1)
        self.return_group_page(wd)
        self.logout(wd)

    def test_test_add_group(self):
        wd = self.wd
        self.open_home_page(wd)

        self.login(wd, user='admin', password='secret')

        self.create_group(wd, group(name='ljfsalrekj', header=';lkj', footer='lkjh'))
        time.sleep(1)
        self.return_group_page(wd)
        self.logout(wd)

    def logout(self, wd):

        # logout
        wd.find_element_by_link_text('Logout').click()

    def return_group_page(self, wd):
        # Return to groups page
        wd.find_element_by_link_text('groups').click()

    def create_group(self, wd, group):

        # create group
        wd.find_element_by_link_text('groups').click()

        # Init_group creation
        wd.find_element_by_name('new').click()

        # fill group form
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys('%s' % group.name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys('%s' % group.header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys('%s' % group.footer)
        # Subimt group creation
        wd.find_element_by_name('submit').click()

    def login(self, wd, user, password):
        # Login page
        wd.find_element_by_name('user').click()
        wd.find_element_by_name('user').clear()
        wd.find_element_by_name('user').send_keys('%s' % user)
        wd.find_element_by_name('pass').click()
        wd.find_element_by_name('pass').clear()
        wd.find_element_by_name('pass').send_keys('%s' % password)
        wd.find_element_by_css_selector('input[type=\"submit\"]').click()

    def open_home_page(self, wd):
        # open web-page
        wd.get('http://localhost/addressbook')

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
