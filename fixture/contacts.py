

class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def create(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#nav > ul > li:nth-child(2) > a').click()
        # wd.find_element_by_link_text('add_new').click()

    def return_contact_page(self):
        wd = self.app.wd
