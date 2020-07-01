# -*- coding: utf-8 -*-
#import unittest
from model.group import Group


def test_add_group(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group(name="New my group", header="my header", footer="my footer"))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)
    #app.session.logout()


def test_add_empty_group(app):
    old_group_list = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_group_list = app.group.get_group_list()
    assert len(old_group_list) + 1 == len(new_group_list)


