from model.group import group


def test_add_empty_group(app):
    app.session.login(user='admin', password='secret')
    app.group.create(group(name='', header='', footer=''))
    app.session.logout()


def test_add_group(app):
    app.session.login(user='admin', password='secret')
    app.group.create(group(name='ljfsalrekj', header=';lkj', footer='lkjh'))
    app.session.logout()


def test_modify_group(app):
    app.session.login(user='admin', password='secret')
    app.group.modify_first_group(group(name='123', header='123', footer='123'))
    app.session.logout()
