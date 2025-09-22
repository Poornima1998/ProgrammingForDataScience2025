from person import Person

class Student(Person):
    def __init__(self, person_id, name, email, level):
        super().__init__(person_id, name, email)
        self.level = level  # 'Undergraduate' or 'Graduate'
        self.courses = []
        self.semester_grades = {}

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)

    def calculate_gpa(self):
        total_points = 0
        total_courses = 0
        for grades in self.semester_grades.values():
            for grade in grades:
                total_points += grade
                total_courses += 1
        if total_courses == 0:
            return 0.0
        return round(total_points / total_courses, 2)

    def get_academic_status(self):
        gpa = self.calculate_gpa()
        if gpa >= 3.7:
            return "Dean's List"
        elif gpa < 2.0:
            return "Probation"
        else:
            return "Good Standing"

    def get_responsibilities(self):
        return "Attend classes, complete assignments and exams"
