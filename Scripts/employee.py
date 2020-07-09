class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def fullname(self):
        return self.firstname + " " + self.lastname

    @property
    def email(self):
        return self.firstname + "." + self.lastname + "@email.com"

    @property
    def firstname(self):
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        if type(value) is not str:
            raise TypeError("Insert a string")
        self._firstname = value
