# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import pytest
from contact import Contact
from application2 import Application2


@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.contact_creation(Contact(firstname="Иван", middlename="Иванович", secondname="Иванушкин", nickname="ivan", title="заголовок", company="Ромашка",
                          address_1="казань чистопольская 33", tel_1="89000000000", tel_2="88888888888", tel_3="87777777777", mail_1="first@mail.ru",
                          mail_2="second@mail.ru", mail_3="third@mail.ru", bday="18", bmonth="March", byear="1989", day="18", month="March", year="2020", address_2="казань петербургская", home="1",
                          notes="привет! друзья"))
    app.submit_contact_creation()
    app.logout()


def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True
