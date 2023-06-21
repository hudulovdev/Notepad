def new_file():
    return []

def open_file():
    file_path = input("Enter file path: ")
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return []

def save_file(content):
    file_path = input("Enter file path to save: ")
    with open(file_path, 'w') as file:
        file.writelines(content)
    print("File saved successfully.")

def notepad():
    content = []
    while True:
        print("\n=== Notepad ===")
        print("1. New File")
        print("2. Open File")
        print("3. Save File")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            content = new_file()
        elif choice == '2':
            content = open_file()
        elif choice == '3':
            save_file(content)
        elif choice == '4':
            print("Exiting Notepad.")
            break
        else:
            print("Invalid choice. Please try again.")

        if content:
            print("\n=== File Content ===")
            print(''.join(content))

notepad()
