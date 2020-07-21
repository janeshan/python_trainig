# -*- coding: utf-8 -*-
#import unittest
from model.group import Group
import pytest

testdata = [Group(name="New my group", header="my header", footer="my footer"),
            Group(name="", header="", footer="")]

@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])
def test_add_group(app, group):
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    #app.session.logout()


# def test_add_empty_group(app):
#     old_group_list = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     new_group_list = app.group.get_group_list()
#     assert len(old_group_list) + 1 == len(new_group_list)
#     old_group_list.append(group)
#     assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)


