# main.py
from faculty import Professor, Lecturer, TA
from student import UndergraduateStudent, GraduateStudent, SecureStudentRecord
from staff import Staff

def demo():
    # Faculty
    p1 = Professor("F001", "Dr. Dileepa")
    p2 = Lecturer("F002", "Anurangi")
    p3 = TA("F003", "Nuran")

    # Students
    s1 = UndergraduateStudent("S001", "Dave")
    s2 = GraduateStudent("S002", "Eve")

    # Staff
    st1 = Staff("ST001", "Kamal", role="Administrator")
    st2 = Staff("ST002", "Nimali", role="Librarian")

    # Secure record for graduate student
    secure = SecureStudentRecord(s2)

    # Print faculty
    for f in [p1, p2, p3]:
        print(f.describe(), "->", f.get_responsibilities())

    # Print students
    for s in [s1, s2]:
        print(s.describe(), "->", s.get_responsibilities())

    # Enroll student and record grade
    s1.enroll_course("Fall2025", "CS101", 3)
    s1.record_grade("Fall2025", "CS101", 3.5)
    print("GPA:", s1.calculate_gpa())
    print("Academic Status:", s1.get_academic_status())

    # Print staff
    for staff in [st1, st2]:
        print(staff.describe(), "->", staff.get_responsibilities())

if __name__ == "__main__":
    demo()
