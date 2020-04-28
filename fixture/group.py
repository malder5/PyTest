from model.group import Group
from sys import maxsize

class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, Group):
        wd = self.app.wd

        # create group
        wd.find_element_by_link_text('groups').click()

        # Init_group creation
        wd.find_element_by_name('new').click()

        self.fill_group_form(Group)
        # Subimt group creation
        wd.find_element_by_name('submit').click()
        self.return_group_page()
        self.group_cache = None

    def fill_group_form(self, Group):
        # fill group form
        self.change_field_value(field_name='group_name', text=Group.name)
        self.change_field_value(field_name='group_header', text=Group.header)
        self.change_field_value(field_name='group_footer', text=Group.footer)

    def change_field_value(self, text, field_name):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys('%s' % text)

    def return_group_page(self):
        wd = self.app.wd

        # Return to groups page
        wd.find_element_by_link_text('groups').click()

    def delete_first_group(self):
        wd = self.app.wd
        # create group
        wd.find_element_by_link_text('groups').click()
        self.select_first_group()
        # Delete first group
        wd.find_element_by_css_selector('input[type="submit"][name="delete"]').click()
        self.return_group_page()
        self.group_cache = None


    def modify_first_group(self, Group):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_css_selector('input[type="submit"][name="edit"]').click()
        # Fill modification form
        self.fill_group_form(Group)
        # submit modification
        wd.find_element_by_css_selector('input[name="update"]').click()
        self.return_group_page()
        self.group_cache = None


    def open_group_page(self):
        # Open Groups
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text('groups').click()

    def select_first_group(self):
        wd = self.app.wd
        # Select first group
        wd.find_element_by_css_selector('input[type="checkbox"]').click()
    def select_group_by_index(self, index):
        wd = self.app.wd
        # Select first group
        elems = wd.find_elements_by_css_selector('input[type="checkbox"]')
        elems[index].click()

    def modify_group_by_index(self, index, Group):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_css_selector('input[type="submit"][name="edit"]').click()
        # Fill modification form
        self.fill_group_form(Group)
        # submit modification
        wd.find_element_by_css_selector('input[name="update"]').click()
        self.return_group_page()
        self.group_cache = None



    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_css_selector('input[name="selected[]"]'))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for elem in wd.find_elements_by_css_selector('span.group'):
                text = elem.text
                id = elem.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(name=text, id=id))
            return list(self.group_cache)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        # create group
        wd.find_element_by_link_text('groups').click()
        self.select_group_by_index(index)

        # Delete first group
        wd.find_element_by_css_selector('input[type="submit"][name="delete"]').click()
        self.return_group_page()
        self.group_cache = None
