def test_add_contact(app):
    app.session.login(user='admin', password='secret')
    app.contact.create()
    elems = app.wd.find_elements_by_css_selector('input[type="text"]')
    with open('names.txt', 'w', encoding='utf8') as f:
        for elem in elems:
                f.write(elem.get_attribute('name'))
                f.write('=None, ')
                print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")
        elems = app.wd.find_elements_by_css_selector('select[name]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")

        elems = app.wd.find_elements_by_css_selector('textarea[name]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")

        elems = app.wd.find_elements_by_css_selector('input[type="file"]')
        for elem in elems:
            f.write(elem.get_attribute('name'))
            f.write('=None, ')
            print(f"self.{elem.get_attribute('name')} = {elem.get_attribute('name')}")

        f.close()

    app.session.logout()