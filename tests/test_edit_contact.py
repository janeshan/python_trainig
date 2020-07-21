from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Николай", middlename="Иванович", secondname="Иванушкин", nickname="ivan",
                                   title="заголовок", company="Ромашка",
                                   address_1="казань чистопольская 33", homephone="89000000000", mobilephone="88888888888",
                                   workphone="87777777777", mail_1="first@mail.ru",
                                   mail_2="second@mail.ru", mail_3="third@mail.ru", bday="18", bmonth="March",
                                   byear="1989", day="18", month="March", year="2020", address_2="казань петербургская",
                                   secondaryphone="86666666666",
                                   notes="привет! друзья"))
        app.contact.submit_contact_creation()
    old_contact_list = app.contact.get_contact_list()
    index = randrange(len(old_contact_list))
    contact = Contact(firstname="Vika", middlename="Ivanovna", secondname="Kolinka", nickname="vikul", title="title", company="Flower",
                               address_1="Kazan Tatarstan st 5", homephone="89111111111", mobilephone="89222222222", workphone="87777777777", mail_1="1first@mail.ru",
                               mail_2="2second@mail.ru", mail_3="3third@mail.ru", bday="18", bmonth="March", byear="1989", day="18", month="March", year="2020", address_2="Kazan Chistopol 11", secondaryphone="86666666666",
                               notes="Hi!")
    contact.id = old_contact_list[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) == len(new_contact_list)
    old_contact_list[index] = contact
    assert sorted(old_contact_list, key=Contact.id_or_max) == sorted(new_contact_list, key=Contact.id_or_max)