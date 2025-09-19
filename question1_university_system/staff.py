from person import Person

class Staff(Person):
    """General university staff - admin, technical, support."""

    def __init__(self, person_id, name, role, email=None): #Inherits from Person
        super().__init__(person_id, name, email)
        self.role = role  # e.g., "Administrator", "Librarian", "Lab Technician"

    def get_responsibilities(self): #Method overriding (polymorphism)
        return f"Handle {self.role} duties and support university operations."
