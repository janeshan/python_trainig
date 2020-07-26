from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

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
    for i in range(n)
    ]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))