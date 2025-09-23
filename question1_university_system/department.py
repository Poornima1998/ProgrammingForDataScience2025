from faculty import Faculty
from student import Student

class Department:
    def __init__(self, name):
        self.name = name
        self.faculty_list = []
        self.course_list = []

    def add_faculty(self, faculty):
        if isinstance(faculty, Faculty):
            self.faculty_list.append(faculty)

    def add_course(self, course):
        self.course_list.append(course)

    def get_faculty(self):
        return self.faculty_list

    def get_courses(self):
        return self.course_list
