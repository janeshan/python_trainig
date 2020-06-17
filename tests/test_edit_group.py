from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_group(Group(name="edited", header="edited", footer="edited"))
    app.session.logout()