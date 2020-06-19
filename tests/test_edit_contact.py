from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(Contact(firstname="Вика", middlename="Григорьевна", secondname="Пупкина", nickname="vika", title="заголовок 3", company="Ромашка 3",
                               address_1="казань чистопольская 33", tel_1="89000000000", tel_2="88888888888", tel_3="87777777777", mail_1="first@mail.ru",
                               mail_2="second@mail.ru", mail_3="third@mail.ru", bday="18", bmonth="March", byear="1989", day="18", month="March", year="2020", address_2="казань петербургская", home="1",
                               notes="привет! друзья"))
    app.session.logout()
