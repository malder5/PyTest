import re
from model.contact import Contacts


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    list_merge = merge_phones_from_like_on_home_page(
        contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == list_merge

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2

def merge_phones_from_like_on_home_page(contact):
    return '\n'.join(filter(lambda x: x!='',
        map(lambda x: clear(x), filter(lambda x: x is not None,
                                       [(contact.home), (contact.mobile), (contact.work), (contact.phone2)]))))

def clear(s):
    return re.sub('[() -]','', s)

