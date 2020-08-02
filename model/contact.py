from sys import maxsize

class Contact:

    def __init__(self, firstname = None, middlename = None, secondname = None, nickname = None, title = None, company = None,
                 address_1 = None, homephone = None, mobilephone = None, workphone = None, mail_1 = None, mail_2 = None, mail_3 = None, byear = None,
                 year = None, address_2 = None, secondaryphone = None, notes = None, bday = None, bmonth = None, day = None, month = None, id = None,
                 all_phone_from_home_page = None, all_mails_from_home_page=None, all_address_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.secondname = secondname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address_1 = address_1
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.mail_1 = mail_1
        self.mail_2 = mail_2
        self.mail_3 = mail_3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.day = day
        self.month = month
        self.year = year
        self.notes = notes
        self.address_2 = address_2
        self.id = id
        self.all_phone_from_home_page = all_phone_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page
        self.all_address_from_home_page = all_address_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.secondname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.secondname == other.secondname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
