from model.contact import Contacts


def test_add_contact(app):
    app.session.login(user='admin', password='secret')
    app.contact.create(Contacts(lastname='123', firstname='123', home='777777777'))
    app.session.logout()

def test_delete_contact(app):
    app.session.login(user='admin', password='secret')
    app.contact.delete_first_contact()
    app.session.logout()