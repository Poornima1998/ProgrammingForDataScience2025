from question1_university_system.course import Course
from question1_university_system.department import Department
from question1_university_system.faculty import Faculty
from question1_university_system.student import Student, StudentRecord


def main():
    #Create department
    cs_department = Department("Computer Science")

    #Add faculty
    p1 = Faculty(101, "Dr. Dileepa", "dileepa@nibm.lk", "Professor")
    t1 = Faculty(102, "Mrs. Anurangi", "anurangi@nibm.lk", "TA")
    cs_department.add_faculty(p1)
    cs_department.add_faculty(t1)

    #Create Courses
    intro_prog = Course("CS101", "Programming for Data Science")
    data_struct = Course("CS102", "Data Science", prerequisites=["CS101"], max_enrollment=2)
    cs_department.add_course(intro_prog)
    cs_department.add_course(data_struct)

    #Create Students
    s1 = Student(100, "Poornima Weerasinghe", "poornima@nibm.lk", "Undergraduate")
    s2 = Student(101, "Maheshi Wasala", "maheshi@nibm.lk", "Graduate")

    #Enroll courses and capacity check
    s1.enroll_course("CS101")
    try:
        intro_prog.enroll_student(s1)
    except ValueError as e:
        print(e)

    try:
        data_struct.enroll_student(s1)  #Should fail, missing prerequisite CS101 in course list
    except ValueError as e:
        print(e)

    #Add GPA per semester
    s1.add_gpa("Semester1", 3.8)
    s1.add_gpa("Semester2", 3.6)
    print(f"{s1.name} GPA: {s1.calculate_gpa()}")
    print(f"{s1.name} Academic Status: {s1.get_academic_status()}")

    #polymorphism
    people = [p1, t1, s1]
    for person in people:
        print(f"{person.name} - Responsibilities: {person.get_responsibilities()}")
        if isinstance(person, Faculty):
            print(f"Workload hours: {person.calculate_workload()}")

    secure_record = StudentRecord(s1)
    secure_record.set_gpa(3.7)
    print(f"Secure GPA for {s1.name} is {secure_record.get_gpa()}")


if __name__ == "__main__":
    main()
