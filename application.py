from selenium.webdriver.chrome.webdriver import WebDriver


class Application:
    def __init__(self):
        self.wd = WebDriver(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
        self.wd.implicitly_wait(60)

    def return_group_page(self):
        wd = self.wd

        # Return to groups page
        wd.find_element_by_link_text('groups').click()

    def open_home_page(self):
        wd = self.wd

        # open web-page
        wd.get('http://localhost/addressbook')

    def create_group(self, Group):
        wd = self.wd

        # create group
        wd.find_element_by_link_text('groups').click()

        # Init_group creation
        wd.find_element_by_name('new').click()

        # fill group form
        wd.find_element_by_name('group_name').click()
        wd.find_element_by_name('group_name').clear()
        wd.find_element_by_name('group_name').send_keys('%s' % Group.name)
        wd.find_element_by_name('group_header').click()
        wd.find_element_by_name('group_header').clear()
        wd.find_element_by_name('group_header').send_keys('%s' % Group.header)
        wd.find_element_by_name('group_footer').click()
        wd.find_element_by_name('group_footer').clear()
        wd.find_element_by_name('group_footer').send_keys('%s' % Group.footer)
        # Subimt group creation
        wd.find_element_by_name('submit').click()
        self.return_group_page()

    def login(self, user, password):
        wd = self.wd
        # Login page
        self.open_home_page()
        wd.find_element_by_name('user').click()
        wd.find_element_by_name('user').clear()
        wd.find_element_by_name('user').send_keys('%s' % user)
        wd.find_element_by_name('pass').click()
        wd.find_element_by_name('pass').clear()
        wd.find_element_by_name('pass').send_keys('%s' % password)
        wd.find_element_by_css_selector('input[type=\"submit\"]').click()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text('Logout').click()

    def destroy(self):
        self.wd.quit()
