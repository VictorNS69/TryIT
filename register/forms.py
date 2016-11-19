from register.models import RegisterCompany


class RegisterCompanyForm():
    def __init__(self, data):
        self.contact_name = data.get('name', '')
        self.company = data.get('company', '')
        self.email = data.get('email', '')
        self.phone = data.get('phone', '')

        self.sponsor = data.get('sponsor', False)
        self.sponsor_type = data.get('sponsor_type', 0)
        self.sponsor_date = data.get('sponsor_date', '')

        self.topic = data.get('topic', '')
        self.description = data.get('description', '')
        self.document = data.get('document', '')

    def is_valid(self):
        if self.contact_name == '' or self.email == '' or self.phone == '':
            return False

        if isinstance(self.sponsor, bool) and self.sponsor:
            types = {i[0] for i in RegisterCompany.SPONSOR_TYPE}
            if self.sponsor_type not in types:
                return False

        if self.topic == '' or self.description == '':
            return False

        return True