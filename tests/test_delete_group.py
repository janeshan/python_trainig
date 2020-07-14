from model.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_group_list = app.group.get_group_list()
    index = randrange(len(old_group_list))
    app.group.delete_group_by_index(index)
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list[index:index+1] = []
    assert old_group_list == new_group_list



