students = [{
    "CPSID": ,
    "Combo,Name": " ",
    "LName": "  ",
    "FName": "  ",
    "MName": "  ",
    "HR": "  ",
    "GL": ,
    "Email": [" "]
}]

#Just here for backup

import student_data
students = student_data.students
def find_student_by_name(students):
    first_name = input("Enter student's first name (no spaces): ")
    last_name = input("Enter student's last name (no spaces): ")

    for student in students:
        if student["FName"].lower() == first_name.lower() and student["LName"].lower() == last_name.lower():
            print("Student Found!")
            print(f"CPS ID: {student['CPSID']}")
            print(f"Homeroom: {student['HR']}")
            print(f"Grade Level: {student['GL']}")
            print(f"Primary Email: {student['Email'][0]}")
            return
    print("Student not found")
#Previous code option instead of lines 34-35.
        #     break
        # else:
        #     print(" Student not found")
        #     break
def add_student_info(students):
    cps_id = int(input("Enter CPS ID: "))

    for student in students:
        if student["CPSID"] == cps_id:
            print("Error: CPS ID already exists.")
            return

    first = input("First Name: ")
    last = input("Last Name: ")
    middle = input("Middle Name: ")
    homeroom = input("Homeroom: ")
    grade = int(input("Grade Level: "))
    email1 = input("Primary Email: ")
    email2 = input("Secondary Email: ")

    new_student = {
        "CPSID": cps_id,
        "Combo,Name": f"{last}, {first}",
        "LName": last,
        "FName": first,
        "MName": middle,
        "HR": homeroom,
        "GL": grade,
        "Email": [email1, email2]
    }

    students.append(new_student)

    print("Student successfully added!")
    print(f"Total students: {len(students)}")
    print("New Student Record:")
    print(new_student)

print("1. Search for student")
print("2. Add a student")
print("3. Exit")
user_choice = input("Choose an option, 1, 2, or 3: ")
for user in user_choice:
    if user_choice == "1":
        find_student_by_name(students)
        anything_else = input("Anything else?(Y or N): ")
    elif user_choice == "2":
        add_student_info(students)
        anything_else = input("Anything else?(Y or N): ")
    elif user_choice == "3":
        print("Okay, have a nice day!")
        break
    else: 
        print("Sorry that's not a valid value, please try again.")
        anything_else = input("Anything else?(Y or N): ")
    if anything_else == "Y":
        new_choice = input("Type 1 to search for student data, type 2 to add student data: ")
        if new_choice == "1":
            find_student_by_name(students)
        elif new_choice == "2":
            add_student_info(students)
        else: 
            print("Sorry that's not a valid value, please try again.")
    elif anything_else == "N":
        print("Okay, have a nice day!")
    else:
        print("There seems to be a typo, please try again")
