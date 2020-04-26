from model.group import group

def test_delete_first_group(app):

    if app.group.count() == 0:
        app.group.create(group(name="test"))

    app.group.delete_first_group()
