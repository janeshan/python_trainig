# -*- coding: utf-8 -*-
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact

def test_add_contact(app, json_contacts):
    contact = json_contacts
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
