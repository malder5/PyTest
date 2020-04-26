from model.contact import Contacts

class ContactsHelper:
    def __init__(self, app):
        self.app = app

    def open_create(self):
        wd = self.app.wd
        wd.find_element_by_css_selector('#nav > ul > li:nth-child(2) > a').click()

    def create(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_css_selector('#nav > ul > li:nth-child(2) > a').click()

        self.fill_group_form(Contacts)

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

    def modify_first(self, Contacts):
        wd = self.app.wd
        wd.find_element_by_css_selector('img[alt="Edit"]').click()

        self.fill_group_form(Contacts)

        wd.find_element_by_name('update').click()
        self.return_contact_page()

    def fill_group_form(self, Contacts):
        wd = self.app.wd
        # fill group form
        self.change_field_value(field_name='firstname', text=Contacts.firstname)
        self.change_field_value(field_name='middlename', text=Contacts.middlename)
        self.change_field_value(field_name='lastname', text=Contacts.lastname)
        self.change_field_value(field_name='nickname', text=Contacts.nickname)
        self.change_field_value(field_name='title', text=Contacts.title)
        self.change_field_value(field_name='company', text=Contacts.company)
        self.change_field_value(field_name='home', text=Contacts.home)
        self.change_field_value(field_name='mobile', text=Contacts.mobile)
        self.change_field_value(field_name='work', text=Contacts.work)
        self.change_field_value(field_name='fax', text=Contacts.fax)
        self.change_field_value(field_name='email', text=Contacts.email)
        self.change_field_value(field_name='email2', text=Contacts.email2)
        self.change_field_value(field_name='email3', text=Contacts.email3)
        self.change_field_value(field_name='homepage', text=Contacts.homepage)
        self.change_field_value(field_name='byear', text=Contacts.byear)
        self.change_field_value(field_name='ayear', text=Contacts.ayear)
        self.change_field_value(field_name='phone2', text=Contacts.phone2)
        self.change_field_value(field_name='new_group', text=Contacts.new_group)
        self.change_field_value(field_name='notes', text=Contacts.notes)
        self.change_field_value(field_name='photo', text=Contacts.photo)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text != None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys('%s' % text)

    def count(self):
        wd = self.app.wd
        self.return_contact_page()
        check = len(wd.find_elements_by_css_selector('input[name="selected[]"]'))
        return len(wd.find_elements_by_css_selector('input[name="selected[]"]'))

    def get_list(self):
        wd = self.app.wd
        self.return_contact_page()
        contacts = []
        elems = wd.find_elements_by_css_selector('tr[name="entry"]') # #maintable > tbody > tr:nth-child(2) > td:nth-child(2)
        for elem in elems:
            text = elem.find_element_by_css_selector('tr[name="entry"] td:nth-child(2)').text
            id = elem.find_element_by_css_selector('input').get_attribute('value')
            contacts.append(
                Contacts(
                    firstname=text,
                    id=id
            ))
        return contacts
