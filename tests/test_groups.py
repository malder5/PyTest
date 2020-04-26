from model.group import group


def test_add_empty_group(app):
    app.group.create(group(name='', header='', footer=''))


def test_add_group(app):
    app.group.create(group(name='ljfsalrekj', header=';lkj', footer='lkjh'))


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(group(name="test"))
    app.group.modify_first_group(group(name='123', header='123', footer='123'))
