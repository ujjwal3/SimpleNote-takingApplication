

note_taking = {}


def new_note(key, value):
    note_taking[f"{key}"] = value


def view_nots():
    print(f"{note_taking.items()}")


def specific_note(key):
    if key in note_taking:
        print(f"{key}-{note_taking.get(key)}")
    else:
        print("not exist")


def remove(key):
    if key in note_taking:
        del note_taking[key]
        print(f"Note '{key}' deleted successfully.")
    else:
        print(f"Note '{key}' not found.")





while True:
    print("Welcome to the Simple Note-taking Application!")
    print("1. Create a New Note")
    print("2. View Notes")
    print("3. View a Specific Note")
    print("4. Delete a Note")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = str(input("Enter the title of the note: "))
        content = str(input("Enter the content of the note: "))
        new_note(title, content)

    elif choice == 2:
        print("--- List of Notes ---")
        view_nots()
    elif choice == 3:
        view_note = str(input("Enter the title of the note you want to view: "))
        print(f"--- Note: {view_note} ---")
        specific_note(view_note)
    elif choice == 4:
        del_note = str(input("Enter the title of the note you want to delete: "))
        remove(del_note)
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("INVALID!")
