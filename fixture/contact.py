from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app


    def open_contact_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/edit.php"):
            wd.find_element_by_link_text("add new").click()


    def create(self, contact):
        wd = self.app.wd
        # contact creation
        self.open_contact_page()
        self.fill_contact_form(contact, wd)
        self.contact_cache = None

    def fill_contact_form(self, contact, wd):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.secondname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_1)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobilephone)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.mail_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.mail_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.mail_3)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondaryphone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def submit_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # contact edition
        el = wd.find_elements_by_name("entry")[index]
        listel = el.find_elements_by_tag_name("td")[7]
        listel.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        # contact edition
        el = wd.find_elements_by_name("entry")[index]
        listel = el.find_elements_by_tag_name("td")[6]
        listel.find_element_by_tag_name("a").click()

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(contact, wd)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.return_home_page()
        self.contact_cache = None


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for el in wd.find_elements_by_name("entry"):
                contactlist = el.find_elements_by_tag_name("td")
                id = contactlist[0].find_element_by_tag_name("input").get_attribute("value")
                all_phone = contactlist[5].text
                all_mails = contactlist[4].text
                all_address = contactlist[3].text
                firstname = contactlist[2].text
                secondname = contactlist[1].text
                self.contact_cache.append(Contact(firstname=firstname, secondname=secondname,
                                                  id=id, all_phone_from_home_page=all_phone,
                                                  all_mails_from_home_page=all_mails, all_address_from_home_page=all_address))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        secondname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        mail_1 = wd.find_element_by_name("email").get_attribute("value")
        mail_2 = wd.find_element_by_name("email2").get_attribute("value")
        mail_3 = wd.find_element_by_name("email3").get_attribute("value")
        address_1 = wd.find_element_by_name("address").get_attribute("value")
        address_2 = wd.find_element_by_name("address2").get_attribute("value")
        return Contact(firstname=firstname, secondname=secondname, id=id,
                        homephone=homephone, workphone=workphone,
                        mobilephone=mobilephone, secondaryphone=secondaryphone, mail_1=mail_1, mail_2=mail_2,
                        mail_3=mail_3, address_1=address_1, address_2=address_2)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        mails = find_elements_by_xpath('//a[@href=mailto]')
        mail_1 = mails[0].text
        mail_2 = mails[1].text
        mail_3 = mails[2].text
        address_1 = address_1[0].text
        address_2 = address_2[1].text
        return Contact(homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryphone=secondaryphone,
                       mail_1=mail_1, mail_2=mail_2, mail_3=mail_3,address_1=address_1, address_2=address_2)




