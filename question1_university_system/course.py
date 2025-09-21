class Course:
    """Represents a course"""

    #initialize a new course object
    def __init__(self, code, title, credits, enrollement_limit=30, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.enrollement_limit = enrollement_limit #maximum nu of students in the course
        self.prerequisites = prerequisites or [] #List of course codes required before enrolling
        self.enrolled_students = [] # Stores student IDs of enrolled students.

    def has_capacity(self):
        #check if the course still has available seats
        return len(self.enrolled_students) < self.enrollement_limit

    def add_student(self, student_id):
        # Add a student if there's space and not already enrolled
        if not self.has_capacity():
            raise ValueError("Course is full")
        if student_id in self.enrolled_students:
            raise ValueError("Student already enrolled")
        self.enrolled_students.append(student_id)

