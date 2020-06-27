from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    app.group.edit_group(Group(name="edited", header="edited", footer="edited"))
