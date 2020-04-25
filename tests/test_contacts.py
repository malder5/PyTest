from model.contact import Contacts


def test_add_contact(app):
    app.contact.create(Contacts(lastname='123', firstname='123', home='777777777'))


def test_delete_contact(app):
    app.contact.delete_first_contact()


def test_modify_first_contact(app):
    app.contact.modify_first(Contacts(lastname='vassya', firstname='visilyevich', home='888888888'))
