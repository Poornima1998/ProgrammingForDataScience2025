class Course:
    def __init__(self, code, title, max_enrollment=30, prerequisites=None):
        self.code = code
        self.title = title
        self.max_enrollment = max_enrollment
        self.prerequisites = prerequisites or []
        self.enrolled_students = []

    def capacity(self):
        return len(self.enrolled_students) < self.max_enrollment

    def enroll_student(self, student):
        #Check prerequisite courses
        for prereq in self.prerequisites:
            if prereq not in student.get_courses():
                raise ValueError(f"Student is not eligible for {self.title}")
        if not self.capacity():
            raise ValueError("Course is full")
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def remove_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
