class Contacts:
    def __init__(self, firstname=None,
                 middlename=None,
                 lastname=None,
                 nickname=None,
                 title=None,
                 company=None,
                 home=None,
                 mobile=None,
                 work=None,
                 fax=None,
                 email=None,
                 email2=None,
                 email3=None,
                 homepage=None,
                 byear=None,
                 ayear=None,
                 phone2=None,
                 bday=None,
                 bmonth=None,
                 aday=None,
                 amonth=None,
                 new_group=None,
                 address=None,
                 address2=None,
                 notes=None,
                 photo=None,
                 id = None,
                 all_phones_from_home_page = None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.ayear = ayear
        self.phone2 = phone2
        self.bday = bday
        self.bmonth = bmonth
        self.aday = aday
        self.amonth = amonth
        self.new_group = new_group
        self.address = address
        self.address2 = address2
        self.notes = notes
        self.photo = photo
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s, %s" %(self.firstname, self.id)

    def __eq__(self, other):
        return self.firstname == other.firstname and self.id == other.id
