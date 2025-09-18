class Department:
    """Represents a department"""

    def __init__(self, name):
        self.name = name
        self.faculty = []
        self.courses = {}

    def add_course(self, course):
        if course.code in self.courses:
            raise ValueError("Course already added")
        self.courses[course.code] = course

    def assign_faculty(self, faculty_id, course_code):
        if course_code not in self.courses:
            raise ValueError("Course not added")
        self.faculty.append(faculty_id)

    def register_student(self, student, semester, course_code):
        if course_code not in self.courses:
            raise ValueError("Course not added")
        course = self.courses[course_code]

        #check prerequisites
        for pre in course.prerequisites:
            passed = False
            for sem_records in student.semesters.values():
                for record in sem_records:
                    if record["course"] == pre and record["grade"] is not None and record["grade"] >= 2.0:
                        passed = True
                        break
                if passed:
                    break
            if not passed:
                raise ValueError("Missing prerequisites")

        #check capacity
        if not course.has_capacity():
            raise ValueError("Course is full")

        #enroll
        course.add_student(student.person_id)
        student.enroll_course(semester, course_code, course.credits)