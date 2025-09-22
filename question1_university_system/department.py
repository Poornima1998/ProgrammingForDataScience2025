class Department:
    def __init__(self, name):
        self.name = name
        self.faculty_members = []
        self.courses = []

    def add_faculty(self, faculty):
        self.faculty_members.append(faculty)

    def add_course(self, course):
        self.courses.append(course)
