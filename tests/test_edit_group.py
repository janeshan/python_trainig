from model.group import Group

def test_edit_group(app):
    app.group.edit_group(Group(name="edited", header="edited", footer="edited"))