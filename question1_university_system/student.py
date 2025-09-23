from person import Person

class Student(Person):
    def __init__(self, person_id, name, email, student_type):
        super().__init__(person_id, name, email)
        self.student_type = student_type  # 'Undergraduate' or 'Graduate'
        self._courses = []
        self._gpa_record = {}  # semester -> GPA

    def enroll_course(self, course):
        if course not in self._courses:
            self._courses.append(course)

    def drop_course(self, course):
        if course in self._courses:
            self._courses.remove(course)

    def calculate_gpa(self):
        if not self._gpa_record:
            return 0.0
        total = sum(self._gpa_record.values())
        return round(total / len(self._gpa_record), 2)

    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.7:
            return "Dean's List"
        elif gpa < 2.0:
            return "Probation"
        else:
            return "Good Standing"

    def get_courses(self):
        return self._courses

    def add_gpa(self, semester, gpa):
        if 0.0 <= gpa <= 4.0:
            self._gpa_record[semester] = gpa
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    def get_responsibilities(self):
        return "Attend classes, complete assignments, and exams"

# Encapsulation with SecureStudentRecord
class SecureStudentRecord:
    def __init__(self, student):
        self.__student = student
        self.__gpa = 0.0

    def set_gpa(self, gpa):
        if 0.0 <= gpa <= 4.0:
            self.__gpa = gpa
        else:
            raise ValueError("GPA out of range")

    def get_gpa(self):
        return self.__gpa
