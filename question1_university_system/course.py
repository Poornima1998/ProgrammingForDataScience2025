class Course:
    """Represents a course"""

    def __init__(self, code, title, credits, enrollement_limit=30, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.enrollement_limit = enrollement_limit
        self.prerequisites = prerequisites or []
        self.enrolled_students = []

    def has_capacity(self):
        return len(self.enrolled_students) < self.enrollement_limit

    def add_student(self, student_id):
        if not self.has_capacity():
            raise ValueError("Course is full")
        if student_id in self.enrolled_students:
            raise ValueError("Student already enrolled")
        self.enrolled_students.append(student_id)

