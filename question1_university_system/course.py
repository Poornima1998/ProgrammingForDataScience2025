class Course:
    def __init__(self, code, title, max_enrollment=30, prerequisites=None):
        self.code = code
        self.title = title
        self.max_enrollment = max_enrollment
        self.prerequisites = prerequisites or []
        self.enrolled_students = []

    def has_capacity(self):
        return len(self.enrolled_students) < self.max_enrollment

    def enroll_student(self, student):
        # Check prerequisite courses
        if any(prereq not in student.get_courses() for prereq in self.prerequisites):
            raise ValueError(f"Student lacks prerequisites for {self.title}")
        if not self.has_capacity():
            raise ValueError("Course full")
        if student not in self.enrolled_students:
            self.enrolled_students.append(student)

    def drop_student(self, student):
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
