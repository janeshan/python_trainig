import pymysql.cursors
from model.group import Group
from model.contact import Contact

class DBFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list=[]
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, title, company, address, home, mobile,"
                           " work, email, email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes from addressbook")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company, address, home, mobile, work, email,
                 email2, email3, bday, bmonth, byear, aday, amonth, ayear, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, secondname=lastname,
                                    nickname=nickname, title=title, company=company, address_1=address, homephone=home,
                                    mobilephone=mobile, workphone=work, secondaryphone=phone2, mail_1=email,
                                    mail_2=email2, mail_3=email3, bday=bday, bmonth=bmonth, byear=byear, day=aday,
                                    month=amonth, year=ayear, notes=notes, address_2=address2))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()


