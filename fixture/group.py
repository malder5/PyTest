

class GroupHelper:
    def __init__(self, app):
        self.app = app
    def create(self, Group):
        wd = self.app.wd

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


    def return_group_page(self):
        wd = self.app.wd

        # Return to groups page
        wd.find_element_by_link_text('groups').click()