from model.group import Group
from random import randrange

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    group = Group(name="edited", header="edited", footer="edited")
    group.id = old_group_list[index].id
    app.group.edit_group_by_index(index, group)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[index] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)