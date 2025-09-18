# student.py
from person import Person

class Student(Person):   # Inherit from Person now
    """Base student class."""

    def __init__(self, person_id, name, email=None):
        super().__init__(person_id, name, email)  # call Person's __init__
        self.semesters = {}  # semester -> list of courses
        self.current_enrollments = []  # courses not yet graded

    def enroll_course(self, semester, course_code, credits):
        """Enroll in a course for a semester."""
        self.semesters.setdefault(semester, [])
        if course_code in self.current_enrollments:
            raise ValueError(f"Already enrolled in {course_code}")
        self.semesters[semester].append({"course": course_code, "grade": None, "credits": credits})
        self.current_enrollments.append(course_code)

    def drop_course(self, semester, course_code):
        """Drop a course if not yet graded."""
        records = self.semesters.get(semester, [])
        for record in records:
            if record["course"] == course_code and record["grade"] is None:
                records.remove(record)
                self.current_enrollments.remove(course_code)
                return
        raise ValueError(f"Cannot drop {course_code}; either graded or not enrolled.")

    def record_grade(self, semester, course_code, grade):
        """Record a grade for a course."""
        if not 0.0 <= grade <= 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0")
        records = self.semesters.get(semester, [])
        for record in records:
            if record["course"] == course_code:
                record["grade"] = grade
                if course_code in self.current_enrollments:
                    self.current_enrollments.remove(course_code)
                return
        raise ValueError(f"{course_code} not found in semester {semester}")

    def calculate_gpa(self, semesters=None):
        """Calculate GPA across all or selected semesters."""
        total_points = 0
        total_credits = 0
        semesters_to_use = semesters if semesters else self.semesters.keys()
        for sem in semesters_to_use:
            for record in self.semesters.get(sem, []):
                if record["grade"] is not None:
                    total_points += record["grade"] * record["credits"]
                    total_credits += record["credits"]
        if total_credits == 0:
            return 0.0
        return round(total_points / total_credits, 2)

    def get_academic_status(self):
        """Return academic standing based on GPA."""
        gpa = self.calculate_gpa()
        if gpa >= 3.7:
            return "Dean's List"
        if gpa < 2.0:
            return "Probation"
        return "Good Standing"


class UndergraduateStudent(Student):
    def get_responsibilities(self):
        return "Attend lectures, complete assignments, participate in labs."


class GraduateStudent(Student):
    def get_responsibilities(self):
        return "Conduct research, attend seminars, complete advanced coursework."


class SecureStudentRecord:
    """Wrap a Student object and protect sensitive data."""

    def __init__(self, student):
        self.__student = student  # private attribute

    def get_student_name(self):
        return self.__student.name

    def get_gpa(self):
        return self.__student.calculate_gpa()

    def set_grade(self, semester, course_code, grade):
        if not 0.0 <= grade <= 4.0:
            raise ValueError("Grade must be between 0.0 and 4.0")
        self.__student.record_grade(semester, course_code, grade)
