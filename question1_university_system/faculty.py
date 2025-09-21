from person import Person

class Faculty(Person):
    """Base class for faculty members"""

    def __init__(self, person_id, name, email=None, department=None): #Initializing a faculty member
        super().__init__(person_id, name, email)
        self.department = department #helps associate faculty with academic units
        self.course_teaching = [] #list of course they are assigned

    def get_responsibilities(self):
        #Define responsibilities of a generic faculty member
        return "Teach, advice for students" #default weekly hours

    def calculated_workload(self):
        #Calculate weekly workload in hours. Default workload set to 40 hrs/week.
        return 40.0

class Professor(Faculty):
    def get_responsibilities(self): #ovverride
        return "Lead courses, supervise students"

    def calculated_workload(self): #ovverride
        return 45.0

class Lecturer(Faculty):
    def get_responsibilities(self): #ovverride
        return "Support tasks, teach courses"

    def calculated_workload(self): #ovverride
        return 40.0

class TA(Faculty):
    def get_responsibilities(self): #ovverride
        return "Assist in teaching, lab supports and tutorials"

    def calculated_workload(self): #ovverride
        return 20.0