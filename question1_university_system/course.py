class Course:
    """Represents a course"""

    #initialize a noew course object
    def __init__(self, code, title, credits, enrollement_limit=30, prerequisites=None):
        self.code = code
        self.title = title
        self.credits = credits
        self.enrollement_limit = enrollement_limit #maximum nu of students in the course
        self.prerequisites = prerequisites or [] #List of course codes required before enrolling
        self.enrolled_students = [] # Stores student IDs of enrolled students.

    def has_capacity(self): #check if the course still has available seats
        return len(self.enrolled_students) < self.enrollement_limit #True if capacity is not null, False otherwise
        #Logic: compare current enrolled students with enrollment limit

    def add_student(self, student_id): #Enroll a student in the course
        #student_id is the unique identifier of the student
        if not self.has_capacity():
            raise ValueError("Course is full")
        if student_id in self.enrolled_students:
            raise ValueError("Student already enrolled")
        self.enrolled_students.append(student_id)
        """
        Logic:
        Step 1: Check capacity using has_capacity()
        Step 2: For prevent duplicated ensure the student is not already enrolled
        Step 3: Add student ID to enrolled list if all checks pass
        """

