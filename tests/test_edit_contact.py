from model.contact import Contact


def test_edit_contact(app):
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
    app.contact.edit_contact(Contact(firstname="Vika", middlename="Ivanovna", secondname="Kolinka", nickname="vikul", title="title", company="Flower",
                               address_1="Kazan Tatarstan st 5", tel_1="89111111111", tel_2="89222222222", tel_3="87777777777", mail_1="1first@mail.ru",
                               mail_2="2second@mail.ru", mail_3="3third@mail.ru", bday="18", bmonth="March", byear="1989", day="18", month="March", year="2020", address_2="Kazan Chistopol 11", home="1",
                               notes="Hi!"))

