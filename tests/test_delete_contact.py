from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Николай", middlename="Иванович", secondname="Иванушкин", nickname="ivan",
                                   title="заголовок", company="Ромашка",
                                   address_1="казань чистопольская 33", tel_1="89000000000", tel_2="88888888888",
                                   tel_3="87777777777", mail_1="first@mail.ru",
                                   mail_2="second@mail.ru", mail_3="third@mail.ru", bday="18", bmonth="March",
                                   byear="1989", day="18", month="March", year="2020", address_2="казань петербургская",
                                   home="1",
                                   notes="привет! друзья"))
        app.contact.submit_contact_creation()
    old_contact_list = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contact_list = app.contact.get_contact_list()
    assert len(old_contact_list) - 1 == len(new_contact_list)
