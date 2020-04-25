

class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_css_selector('#nav > ul > li:nth-child(2) > a').click()

        wd.find_element_by_name('firstname').click()
        wd.find_element_by_name('firstname').clear()
        wd.find_element_by_name('firstname').send_keys(Contacts.firstname)

        wd.find_element_by_name('lastname').click()
        wd.find_element_by_name('lastname').clear()
        wd.find_element_by_name('lastname').send_keys(Contacts.lastname)

        wd.find_element_by_name('home').click()
        wd.find_element_by_name('home').clear()
        wd.find_element_by_name('home').send_keys(Contacts.home)

        wd.find_element_by_name('submit').click()
        self.return_contact_page()

    def return_contact_page(self):
        wd = self.app.wd

        # Return to groups page
        wd.find_element_by_css_selector('img[title="Addressbook"]').click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[title="Edit"]').click()

        wd.find_element_by_css_selector('input[value="Delete"]').click()

        self.return_contact_page()
