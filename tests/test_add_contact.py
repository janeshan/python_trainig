# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*5
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_phone(maxlen):
    symbols = string.digits + " " + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_email(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) + "@gmail.com"



testdata = [Contact(firstname="", middlename="", secondname="", nickname="", title="", company="", address_1="",
                    homephone="", mobilephone="", workphone="", mail_1="", mail_2="", mail_3="", address_2="",
                    secondaryphone="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), secondname=random_string("secondname", 20),
            nickname=random_string("nickname", 20), title=random_string("title", 20), company=random_string("company", 20),
            address_1=random_string("address_1", 20), homephone=random_phone(15), mobilephone=random_phone(15),
            workphone=random_phone(15), mail_1=random_email("mail_1", 20), mail_2=random_email("mail_2", 20),
            mail_3=random_email("mail_3", 20), address_2=random_string("address_2", 20), secondaryphone=random_phone(15),
            notes=random_string("notes", 20))
    for i in range(2)
    ]


@pytest.mark.parametrize("contact", testdata, ids = [repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contact_list = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.submit_contact_creation()
    assert len(old_contact_list) + 1 == app.contact.count()
    new_contact_list = app.contact.get_contact_list()
    old_contact_list.append(contact)
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)



def is_element_present(self, how, what):
    try: self.wd.find_element(by=how, value=what)
    except NoSuchElementException as e: return False
    return True

def is_alert_present(self):
    try: self.wd.switch_to_alert()
    except NoAlertPresentException as e: return False
    return True
