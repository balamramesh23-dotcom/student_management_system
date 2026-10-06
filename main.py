from backend.student_manager import StudentManager


def show_menu():
    print("\n1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Performance report")
    print("7. Exit")


def main():
    manager = StudentManager()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.update_student()
        elif choice == "5":
            manager.delete_student()
        elif choice == "6":
            manager.performance_report()
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Wrong choice. Try again.")


if __name__ == "__main__":
    main()
