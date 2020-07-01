from model.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_group_list = app.group.get_group_list()
    app.group.edit_group(Group(name="edited", header="edited", footer="edited"))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)
