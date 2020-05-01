from model.contact import Contacts
import re


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

    def open_home_page(self):
        wd = self.app.wd


    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_css_selector('tr[name="entry"]'): # #maintable > tbody > tr:nth-child(2) > td:nth-child(2)
                cells = row.find_elements_by_tag_name('td')
                firstname = cells[1].text
                lastname = cells[2].text
                id = cells[0].find_element_by_tag_name('input').get_attribute('value')

                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(
                    Contacts(
                        firstname=firstname,
                        lastname=lastname,
                        id=id,
                        home=all_phones[0],
                        mobile=all_phones[1],
                        work=all_phones[2],
                        phone2=all_phones[3]
                ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.return_contact_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[7]
        cell.find_element_by_tag_name('a').click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        homephone = wd.find_element_by_name('home').get_attribute("value")
        workphone = wd.find_element_by_name('work').get_attribute("value")
        mobilephone = wd.find_element_by_name('mobile').get_attribute("value")
        secondaryphone = wd.find_element_by_name('phone2').get_attribute("value")
        return Contacts(
            firstname=firstname, lastname=lastname, id=id,
            home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.return_contact_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name('td')[6]
        cell.find_element_by_tag_name('a').click()


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_css_selector('#content').text
        home = re.search('H:(.*)', text).group(1).strip()
        work = re.search('W:(.*)', text).group(1).strip()
        mobile = re.search('M:(.*)', text).group(1).strip()
        phone2 = re.search('P:(.*)', text).group(1).strip()
        return Contacts(home=home, work=work, mobile=mobile, phone2=phone2)




        # home = re.search("H: (.*)")





