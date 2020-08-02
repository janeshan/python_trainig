# -*- coding: utf-8 -*-
#import unittest
from model.group import Group


def test_add_group(app, db, json_groups):
    group = json_groups
    old_group_list = db.get_group_list()
    app.group.create(group)
    new_group_list = db.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    #app.session.logout()




