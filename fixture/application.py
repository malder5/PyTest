from selenium.webdriver.chrome.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(executable_path=r'C:\Users\Roman\Downloads\chromedriver.exe')
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd

        # open web-page
        wd.get('http://localhost/addressbook')

    def destroy(self):
        self.wd.quit()
