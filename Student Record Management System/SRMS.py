import csv,json

CSV_FILE = "srms.csv"

def save_to_csv(data):
    if not data:
        return

    fieldnames = data[0].keys()

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

with open('srms.csv',encoding="utf-8") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f, indent=2)

def load_data():
    with open("data.json","r",encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open("data.json","w",encoding="utf-8") as f:
        json.dump(data,f,indent=2)
    save_to_csv(data)


def clean_empty_keys():
    data = load_data()
    for student in data:
        if "" in student:
            del student[""]
    save_data(data)
    print("Empty keys cleaned successfully")

clean_empty_keys()
def view_students():
    data = load_data()
    if not data:
        print("No records found.")
        return
    for student in data:
        print(student)

def add_student():
    data = load_data()
    grade = float(input("Enter grade:"))
    student = {
        "id": input("Enter ID: "),
        "name":input("Enter name:"),
        "age":int(input("Enter age:")),
        "grade":grade,
        "address":input("Enter address:"),
        "phone":int(input("Enter phone number:")),
        "isScholar": grade > 3.6
    }
    data.append(student)
    save_data(data)
    print("Student added successfully.")

def update_student():
    data = load_data()
    sid = input("Enter the student id to update: ")
    for s in data:
        if s["id"] == sid:
            s["name"] = input(f"Name ({s['name']}): ") 
            s["age"] = input(f"Age ({s['age']}): ") 
            s["address"] = input(f"Address ({s['address']}): ") 
            s["phone"] = input(f"Phone ({s['phone']}): ") 

            grade_input = input(f"Grade ({s['grade']}): ")
            if grade_input:
                s['grade'] = float(grade_input)
            s["isScholar"] = float(s['grade']) > 3.6

            save_data(data)
            print("Student updated.")
            return

    print("Student not found.")
def delete_student():
    data = load_data()
    view_students()
    sid = input("Enter student id to delete: ")
    new_data = [s for s in data if s["id"] != sid]
    if len(new_data) == len(data):
        print("Student not found")
    else: 
        save_data(new_data)
        print("Student deleted.")

def menu():
    while True:
        print("""
1. View Students
2. Add Students
3. Update Students
4. Delete Students
5. Exit
""")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            view_students()
        elif choice == 2:
            add_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            break
        else:
            print("Invalid choice")
menu()
