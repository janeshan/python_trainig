# -*- coding: utf-8 -*-
#import unittest
from model.group import Group
import pytest
from data.add_group import testdata


@pytest.mark.parametrize("group", testdata, ids = [repr(x) for x in testdata])
def test_add_group(app, group):
    old_group_list = app.group.get_group_list()
    app.group.create(group)
    assert len(old_group_list) + 1 == app.group.count()
    new_group_list = app.group.get_group_list()
    old_group_list.append(group)
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)
    #app.session.logout()




