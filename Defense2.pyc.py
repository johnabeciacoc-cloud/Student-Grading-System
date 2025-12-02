students = []
archived_students = []

while True: 
    print("\nLogin Menu")
    print("1. Login")
    print("2. Exit")
    login_choice = input("Enter an option: ")

    if login_choice == '1':
        username = input("Username: ")
        password = input("Password: ")

        if username == "teacher jean" and password == "1234":
            print("Login successful!\n")

            while True:
                print("\n             Student Grading System                 ")
                print("Please add students before proceeding to other options")
                print("1. Add student grades")
                print("2. View student grades")
                print("3. Edit student grades")
                print("4. Archive student")
                print("5. View archived students")
                print("6. Restore archived student")
                print("7. Logout")
                
                choice = input("Enter an option: ")            
                
                if choice == '1':
                    try:
                        n = int(input("Enter number of students to add: "))
                    except ValueError:
                        print("Please enter a valid number.\n")
                        continue
                    for i in range(n):
                        print(f"\nStudent {i+1}")

                        while True:
                            id = input("Enter student ID: ").strip()
                            if not id or any(c not in "0123456789-" for c in id):
                                print("Invalid ID.")
                            elif any(s['id'] == id for s in students): 
                                print("ID already exists. Enter a different ID.")
                            else:
                                break

                        while True:
                            f_name = input("Enter first name: ").title().strip()
                            if not f_name:
                                print("First name cannot be empty.")
                            elif any(n.isdigit() for n in f_name):
                                print("Invalid first name. Numbers are not allowed.")
                            else:
                                break

                        while True:
                            l_name = input("Enter last name: ").title().strip()
                            if not l_name:
                                print("Last name cannot be empty.")
                            elif any(n.isdigit() for n in l_name):
                                print("Invalid last name. Numbers are not allowed.")
                            else:
                                break

                        name = f"{f_name} {l_name}"

                        while True:
                            try:
                                p1 = float(input("Enter P1 Grade 0 to 100: "))
                                p2 = float(input("Enter P2 Grade 0 to 100: "))
                                p3 = float(input("Enter P3 Grade 0 to 100: "))
                                if all(0 <= grade <= 100 for grade in [p1, p2, p3]):
                                    break
                                print("Grades must be between 0 to 100.")
                            except ValueError:
                                print("Invalid input. Enter numbers only.")

                        avg = (p1 + p2 + p3) / 3
                        remark = "Passed" if avg >= 60 else "Failed"
                        students.append({
                            'id': id,
                            'name': name,
                            'P1': p1,
                            'P2': p2,
                            'P3': p3,
                            'average': avg,
                            'remark': remark
                        })
                        print(f"Student {name} added.\n")

                elif choice == '2':
                    if not students:
                        print("No students found.")
                    else:
                        print("\nList of students: ")
                        for i, s in enumerate(students, 1):
                            print(f"{i}. ID:{s['id']} | Name:{s['name']} | "
                                  f"P1:{s['P1']} P2:{s['P2']} P3:{s['P3']} | "
                                  f"Avg:{s['average']:.2f} | {s['remark']}")

                elif choice == '3':
                    if not students:
                        print("No students to edit.")
                        continue
                    
                    for i, s in enumerate(students, 1):
                        print(f"{i}. ID:{s['id']} | Name:{s['name']}")
                   
                    try:
                        num = int(input("Student number to edit: ")) - 1
                        if not (0 <= num < len(students)):
                            print("Invalid number.")
                            continue    
                    except ValueError:
                        print("Invalid input.")
                        continue

                    s = students[num]
                    print(f"Editing {s['name']} (ID:{s['id']})")

                    while True:
                        try:
                            p1 = float(input("Enter student P1 grade  0 to 100: "))
                            p1 = float(input("Enter student P1 grade  0 to 100: "))
                            p1 = float(input("Enter student P1 grade  0 to 100: "))
                            if all(0 <= grade <= 100 for grade in [p1, p2, p3]):
                                break
                            print("Grades must be between 0 to 100.")
                        except ValueError:
                            print("Invalid input. Enter numbers only.")

                    s['P1'], s['P2'], s['P3'] = p1, p2, p3
                    s['average'] = (p1 + p2 + p3) / 3
                    s['remark'] = "Passed" if s['average'] >= 60 else "Failed"
                    print("Grades updated.\n")

                elif choice == '4':
                    if not students:
                        print("No students to archive.")
                        continue

                    for i, s in enumerate(students, 1):
                        print(f"{i}. ID:{s['id']} | Name:{s['name']}")

                    try:
                        num = int(input("Student number to archive: ")) - 1
                        if not (0 <= num < len(students)):
                            print("Invalid number.")
                            continue
                    except ValueError:
                        print("Invalid input.")
                        continue

                    archived_students.append(students.pop(num))
                    print("Student archived.\n")

                elif choice == '5':
                    if not archived_students:
                        print("No archived students.")
                    else:
                        print("\nList of archived students: ")
                        for i, s in enumerate(archived_students, 1):
                            print(f"{i}. ID:{s['id']} | Name:{s['name']} | "
                                  f"Avg:{s['average']:.2f} | {s['remark']}")

                elif choice == '6':
                    if not archived_students:
                        print("No students to restore.")
                        continue

                    for i, s in enumerate(archived_students, 1):
                        print(f"{i}. ID:{s['id']} | Name:{s['name']}")

                    try:
                        num = int(input("Student number to restore: ")) - 1
                        if not (0 <= num < len(archived_students)):
                            print("Invalid number.")
                            continue
                    except ValueError:
                        print("Invalid input.")
                        continue

                    students.append(archived_students.pop(num))
                    print("Student restored.\n")

                elif choice == '7':
                    print("Logging out.\n")
                    break

                else:
                    print("Invalid option.")

        else:
            print("Invalid username or password.")

    elif login_choice == '2':
        print("Exiting program... Goodbye!")
        break

    else:
        print("Invalid option.")
