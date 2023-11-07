import os
import datetime
import subprocess

# Initial directory
initial_dir = "f:\\"

# Function to search for files
def search():
    search_dir = input("Enter the directory to search (or press Enter to use the initial dir): ")
    if not search_dir:
        search_dir = initial_dir

    option = int(input("Enter search option (1=name, 2=extension, 3=date, 4=size): "))

    if option == 1:
        search_by_name(search_dir)
    elif option == 2:
        search_by_extension(search_dir)
    elif option == 3:
        search_by_date(search_dir)
    elif option == 4:
        search_by_size(search_dir)
    else:
        print("Invalid option. Please select a valid search option.")
        search()

# Search by name
def search_by_name(directory):
    name = input("Enter the name to search (e.g., 'dash' or 'cat'): ")
    print("Example results:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if name in file:
                print(file + " in " + os.path.join(root))

# Search by extension
def search_by_extension(directory):
    extension = input("Enter the file extension (e.g., .pdf, .docx): ")
    print("Matching files:")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                print(os.path.join(root, file))

# Search by size
def search_by_size(directory):
    size_str = input("Enter the file size (e.g., '1000kb' or '1mb'): ")
    try:
        size, unit = size_str[:-2], size_str[-2:].lower()
        size = float(size)
        if unit == "kb":
            size_in_bytes = size * 1024
        elif unit == "mb":
            size_in_bytes = size * 1024 * 1024
        else:
            print("Invalid size format. Please use 'kb' or 'mb' for units.")
            return

        print(f"Files with size {size} {unit}:")
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_size = os.path.getsize(os.path.join(root, file))
                if file_size == size_in_bytes:
                    print(os.path.join(root, file))
    except ValueError:
        print("Invalid size format. Please use a valid number followed by 'kb' or 'mb'.")


# Search by date
def search_by_date(directory):
    date_option = int(input("Select date option (1=on the date, 2=between dates): "))
    if date_option == 1:
        date_str = input("Enter the date (e.g., 'YYYY-MM-DD'): ")
        try:
            date = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            print("Files created on the specified date:")
            for root, dirs, files in os.walk(directory):
                for file in files:
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root, file)))
                    if creation_time.date() == date.date():
                        print(os.path.join(root, file))
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
    elif date_option == 2:
        start_date_str = input("Enter the start date (e.g., 'YYYY-MM-DD'): ")
        end_date_str = input("Enter the end date (e.g., 'YYYY-MM-DD'): ")
        try:
            start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")
            print("Files created between the specified dates:")
            for root, dirs, files in os.walk(directory):
                for file in files:
                    creation_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root, file)))
                    if start_date.date() <= creation_time.date() <= end_date.date():
                        print(os.path.join(root, file))
        except ValueError:
            print("Invalid date format. Please use 'YYYY-MM-DD'.")
    else:
        print("Invalid date option. Please select a valid option.")
        search_by_date(directory)
# Function to create a file
def creation():
    create_dir = input("Enter the directory to create a file (or press Enter to use the initial dir 'f:\\'): ")
    if not create_dir:
        create_dir = initial_dir

    file_name = input("Enter the file name with extension (e.g., 'example.txt'): ")
    subprocess.Popen(['notepad.exe', file_name])
    file_path = os.path.join(create_dir, file_name)

    if os.path.exists(file_path):
        print(f"'{file_path}' already exists. Choose a different name or location.")
        creation()
    else:
        try:
            with open(file_path, 'w'):
                print(f"File '{file_name}' has been successfully created at '{create_dir}'.")
        except Exception as e:
            print(f"Error: {e}")
            print(f"File '{file_name}' could not be created.")
def delete():
    file_to_delete = input("Enter the file path to delete: ")
    if os.path.exists(file_to_delete):
        os.remove(file_to_delete)
        print(f"'{file_to_delete}' has been deleted.")
    else:
        print(f"'{file_to_delete}' does not exist.")

# Main menu and code execution
while True:
    print("\nMain Menu:")
    print("1. Search for files")
    print("2. Create a folder and open a file")
    print("3. Delete a file")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        search()
    elif choice == 2:
        creation()
    elif choice == 3:
        delete()
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")