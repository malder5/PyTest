from model.group import group


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(group(name='', header='', footer=''))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(group(name='ljfsalrekj', header=';lkj', footer='lkjh'))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(group(name="test"))

    old_groups = app.group.get_group_list()
    app.group.modify_first_group(group(name='123', header='123', footer='123'))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
