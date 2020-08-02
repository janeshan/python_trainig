import re

def test_details_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phone_from_home_page == merge_phone_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_address_from_home_page == merge_address_like_on_home_page(contact_from_edit_page)


def test_details_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    assert contact_from_view_page.mail_1 == contact_from_edit_page.mail_1
    assert contact_from_view_page.mail_2 == contact_from_edit_page.mail_2
    assert contact_from_view_page.mail_3 == contact_from_edit_page.mail_3
    assert contact_from_view_page.address_1 == contact_from_edit_page.address_1
    assert contact_from_view_page.address_2 == contact_from_edit_page.address_2


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phone_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.mail_1, contact.mail_2, contact.mail_3]))))

def merge_address_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.address_1, contact.address_2]))))
