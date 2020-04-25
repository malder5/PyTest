
def test_add_contacts(app):
    app.session.login(user='admin', password='secret')
    app.contact.open_create()
    elems = app.wd.find_elements_by_css_selector('input[type="text"]')
    with open('names.txt', 'w', encoding='utf8') as f:
        for elem in elems:
                f.write(elem.get_attribute('name'))
                f.write('=None, ')
                print(f"self.change_field_value(field_name='{elem.get_attribute('name')}', text=Contacts.{elem.get_attribute('name')})")
        elems = app.wd.find_elements_by_css_selector('select[name]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            # print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")
        print(
            f"self.change_field_value(field_name='{elem.get_attribute('name')}', text=Contacts.{elem.get_attribute('name')})")

        elems = app.wd.find_elements_by_css_selector('textarea[name]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            # print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")
        print(
            f"self.change_field_value(field_name='{elem.get_attribute('name')}', text=Contacts.{elem.get_attribute('name')})")

        elems = app.wd.find_elements_by_css_selector('input[type="file"]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            # print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")
        print(
            f"self.change_field_value(field_name='{elem.get_attribute('name')}', text=Contacts.{elem.get_attribute('name')})")

        f.close()

    app.session.logout()