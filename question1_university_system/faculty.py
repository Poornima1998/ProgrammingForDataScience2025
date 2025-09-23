from person import Person

class Faculty(Person):
    def __init__(self, person_id, name, email, faculty_type):
        super().__init__(person_id, name, email)
        self.faculty_type = faculty_type  # 'Professor', 'Lecturer', 'TA'

    def get_responsibilities(self):
        if self.faculty_type == "Professor":
            return "Conduct research, teach courses, advise students"
        elif self.faculty_type == "Lecturer":
            return "Teach courses and prepare materials"
        elif self.faculty_type == "TA":
            return "Assist in teaching and grading"
        else:
            return super().get_responsibilities()

    def calculate_workload(self):
        if self.faculty_type == "Professor":
            return 40  # Hours per week
        elif self.faculty_type == "Lecturer":
            return 30
        elif self.faculty_type == "TA":
            return 20
        else:
            return 0