import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="aNAMI@123",  # Change this to your MySQL password
    database="hospital"
)
cursor = conn.cursor()

def add_patient():
    """Add a new patient."""
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    disease = input("Enter Disease: ")
    contact = input("Enter Contact Number: ")

    cursor.execute("INSERT INTO patients (name, age, disease, contact) VALUES (%s, %s, %s, %s)", (name, age, disease, contact))
    conn.commit()
    print("Patient added successfully!")

def view_patients():
    """Display all patients."""
    cursor.execute("SELECT * FROM patients")
    records = cursor.fetchall()

    if not records:
        print("No patients found.")
    else:
        print("\nID\tName\tAge\tDisease\tContact")
        print("-" * 50)
        for row in records:
            print(row[0], "\t", row[1], "\t", row[2], "\t", row[3], "\t", row[4])
        print()

def delete_patient():
    """Delete a patient by ID."""
    view_patients()
    patient_id = input("Enter Patient ID to delete: ")

    cursor.execute("DELETE FROM patients WHERE id = %s", (patient_id,))
    conn.commit()

    if cursor.rowcount > 0:
        print("Patient deleted successfully!")
    else:
        print("Patient ID not found.")

def update_patient():
    """Update patient details."""
    view_patients()
    patient_id = input("Enter Patient ID to update: ")

    name = input("Enter New Name: ")
    age = input("Enter New Age: ")
    disease = input("Enter New Disease: ")
    contact = input("Enter New Contact Number: ")

    cursor.execute("UPDATE patients SET name = %s, age = %s, disease = %s, contact = %s WHERE id = %s",
                   (name, age, disease, contact, patient_id))
    conn.commit()

    if cursor.rowcount > 0:
        print("Patient details updated successfully!")
    else:
        print("Patient ID not found.")

while True:
    print("\n1. Add Patient\n2. View Patients\n3. Delete Patient\n4. Update Patient\n5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_patient()
    elif choice == "2":
        view_patients()
    elif choice == "3":
        delete_patient()
    elif choice == "4":
        update_patient()
    elif choice == "5":
        conn.close()
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")