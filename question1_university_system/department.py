class Department:
    """Represents a department"""

    def __init__(self, name): #Initialize a department
        self.name = name
        self.faculty = [] # List of faculty IDs associated with this department
        self.courses = {} # Courses are stored in a dictionary for quick lookup by course code

    def add_course(self, course): #Add course to the department
        if course.code in self.courses:
            raise ValueError("Course already added")
        self.courses[course.code] = course

    def assign_faculty(self, faculty_id, course_code): #Assign a faculty member to a specific course
        if course_code not in self.courses:
            raise ValueError("course does not exist in the department")
        self.faculty.append(faculty_id)

    def register_student(self, student, semester, course_code): #Register a student for a course in a given semester
        """
        Flow:
        1. Check if course exists in department
        2. Validate that student meets all prerequisites
        3. Check if course has available capacity
        4. Enroll student in course and update their academic record
        """
        if course_code not in self.courses:
            raise ValueError("Course not added")
        course = self.courses[course_code]

        #check prerequisites
        for pre in course.prerequisites:
            passed = False
            for sem_records in student.semesters.values():
                for record in sem_records:
                    # Student must have taken prerequisite with grade >= 2.0 (C grade)
                    if record["course"] == pre and record["grade"] is not None and record["grade"] >= 2.0:
                        passed = True
                        break
                if passed:
                    break
            if not passed:
                raise ValueError("Missing prerequisites")

        #check course capacity
        if not course.has_capacity():
            raise ValueError("Course is full")

        #enroll student
        course.add_student(student.person_id)
        student.enroll_course(semester, course_code, course.credits)