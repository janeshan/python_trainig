# -*- coding: utf-8 -*-
#import unittest
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="New my group", header="my header", footer="my footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


