from question1_university_system.person import Person


class Staff(Person):
    def __init__(self, staff_id, name, email, position):
        super().__init__(staff_id, name, email)
        self.position = position

    def get_responsibilities(self):
        return "Support for the faculty"