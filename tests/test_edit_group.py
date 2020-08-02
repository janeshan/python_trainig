from model.group import Group
import random

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_group_list = db.get_group_list()
    group_ch = random.choice(old_group_list)
    group = Group(name="edited", header="edited", footer="edited")
    app.group.edit_group_by_id(group_ch.id, group)
    new_group_list = db.get_group_list()
    assert len(old_group_list) == len(new_group_list)
    old_group_list[group_ch.id] = group
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_group_list, key=Group.id_or_max()) == sorted(app.group.get_group_list(), key=Group.id_or_max())