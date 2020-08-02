from model.group import Group
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_group_list = db.get_group_list()
    group = random.choice(old_group_list)
    app.group.delete_group_by_id(group.id)
    new_group_list = db.get_group_list()
    assert len(old_group_list) - 1 == len(new_group_list)
    old_group_list.remove(group)
    assert old_group_list == new_group_list
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max()) == sorted(app.group.get_group_list(), key=Group.id_or_max())



