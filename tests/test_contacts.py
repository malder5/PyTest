from model.contact import Contacts


def test_add_contact(app):
    old_list = app.contact.get_list()
    app.contact.create(Contacts(lastname='123', firstname='123', home='777777777'))
    new_list = app.contact.get_list()
    assert len(old_list)+1 == len(new_list)

def test_delete_contact(app):
    if app.contact.count() <= 1:
        app.contact.create(Contacts(lastname='123', firstname='123', home='777777777'))

    old_list = app.contact.get_list()
    app.contact.delete_first_contact()
    new_list = app.contact.get_list()
    assert len(old_list)-1 == len(new_list)
    old_list[0:1] = []
    assert old_list == new_list


def test_modify_first_contact(app):
    if app.contact.count() < 1:
        app.contact.create(Contacts(lastname='123', firstname='123', home='777777777'))

    old_list = app.contact.get_list()
    app.contact.modify_first(Contacts(lastname='vassya', firstname='visilyevich', home='888888888'))
    new_list = app.contact.get_list()
    assert len(old_list) == len(new_list)
