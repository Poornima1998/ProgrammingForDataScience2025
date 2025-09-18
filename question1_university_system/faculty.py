from person import Person

class Faculty(Person):
    """Base class for faculty members"""

    def __init__(self, person_id, name, email=None, department=None):
        super().__init__(person_id, name, email)
        self.department = department
        self.course_teaching = [] #list of course codes

    def get_responsibilities(self):
        return "Teach, advice for students" #default weekly hours

    def calculated_workload(self):
        return 40.0

class Professor(Faculty):
    def get_responsibilities(self):
        return "Lead courses, supervise students"

    def calculated_workload(self):
        return 45.0

class Lecturer(Faculty):
    def get_responsibilities(self):
        return "Support tasks, teach courses"

    def calculated_workload(self):
        return 40.0

class TA(Faculty):
    def get_responsibilities(self):
        return "Assist in teaching, lab supports and tutorials"

    def calculated_workload(self):
        return 20.0