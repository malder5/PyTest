from model.contact import Contacts


def test_add_contact(app):
    app.session.login(user='admin', password='secret')
    app.contact.create(Contacts(lastname='', firstname='', nickname='', middlename=''))
    app.session.logout()