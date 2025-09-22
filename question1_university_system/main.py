from person import Person
from student import Student
from faculty import Faculty
from department import Department


def main():
    # Create department
    cs_department = Department("Computer Science")

    # Add faculty
    p1 = Faculty(101, "Dr. Dileepa", "dileepa@nibm.lk", "Professor")
    p2 = Faculty(102, "Mrs. Anurangi", "anurangi@nibm.lk", "TA")
    cs_department.add_faculty(p1)
    cs_department.add_faculty(p2)

    # Create a student
    s1 = Student(201, "Poornima Weerasinghe", "poornima.w@nibm.lk", "Undergraduate")

    # Enroll student in courses
    s1.enroll_course("Programming for Data Science")
    s1.semester_grades = {
        "2024": [3.5, 4.0, 3.7],
        "2025": [3.8, 3.9, 3.6]
    }

    # Print stuff demonstrating polymorphism
    people = [p1, p2, s1]

    for person in people:
        print(f"{person.name}: {person.get_responsibilities()}")

    # Display GPA and status
    print(f"{s1.name} GPA: {s1.calculate_gpa()}")
    print(f"{s1.name} Academic Status: {s1.get_academic_status()}")

    # Show department info
    print(f"Department: {cs_department.name}")
    print("Faculty Members:")
    for fac in cs_department.faculty_members:
        print(f"- {fac.name} ({fac.faculty_type})")


if __name__ == "__main__":
    main()
