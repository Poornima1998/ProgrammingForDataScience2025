class Person:
    """Base class for all people in the university"""
    def __init__(self, person_id, name, email=None):
        self.person_id = person_id
        self.name = name
        self.email = email

    def describe(self):
        """Return a description of the person"""
        return f'{self.name} ({self.person_id})'

    def get_responsibilities(self):
        """General responsibilities of a person"""
        return "General resonsibilities as a member of the university"

class Staff(Person):
    """University staff member"""
    def get_responsibilities(self):
        return "Support tasks"