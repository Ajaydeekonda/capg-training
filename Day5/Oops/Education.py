class School:
    def __init__(self, school_name, location):
        self.school_name = school_name
        self.location = location

    def display_school_info(self):
        print(f"School Name: {self.school_name}")
        print(f"Location: {self.location}")


class UG(School):
    def __init__(self, school_name, location, ug_program):
        super().__init__(school_name, location)
        self.ug_program = ug_program

    def display_ug_info(self):
        self.display_school_info()
        print(f"Undergraduate Program: {self.ug_program}")


class PG(UG):
    def __init__(self, school_name, location, ug_program, pg_program):
        super().__init__(school_name, location, ug_program)
        self.pg_program = pg_program

    def display_pg_info(self):
        self.display_ug_info()
        print(f"Postgraduate Program: {self.pg_program}")


class Student:
    def __init__(self, student_id, name, age):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.pg_details = None  # Holds an instance of PG

    def set_pg_details(self, pg_details):
        self.pg_details = pg_details

    def display_student_info(self):
        print("\n--- Student Information ---")
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
        if self.pg_details:
            print("\n--- Educational Journey ---")
            self.pg_details.display_pg_info()
        else:
            print("\nNo educational details available.")


# Example Usage
def main():
    # Create a student object
    student = Student(101, "Ajay Deekonda", 24)

    # Create PG details (which include UG and School details)
    pg_details = PG(
        school_name="National University",
        location="Delhi",
        ug_program="B.Sc Computer Science",
        pg_program="M.Sc Data Science"
    )
    student.set_pg_details(pg_details)

    # Display full student information
    student.display_student_info()


if __name__ == "__main__":
    main()
