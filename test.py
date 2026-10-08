"""student grade management system"""


class Student:
    """represent a student and their grades"""
    def __init__(self, student_id, name):
        """Initialize a student with valid information"""
        if not isinstance(student_id, str) or not student_id.strip():
            raise ValueError("student ID cannot be empty")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("student name cannot be empty")

        self.student_id = student_id.strip()
        self.name = name.strip()
        self.grades = []


    def add_grade(self, grade):
        """add a valid student grade"""
        if (
            not isinstance(grade, (int, float))
            or isinstance(grade, bool)
            or not 0 <= grade <= 100
        ):
            print("Error: grade must be numeric and between 0 and 100")
            return False

        self.grades.append(float(grade))
        return True



    def calculate_average(self):
        """calculate the average grade"""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)



    def is_honor_roll(self):
        """determine honor roll eligibility"""
        return bool(self.grades) and self.calculate_average() >= 90



    def remove_grade_by_index(self, index):
        """remove a grade using its index"""
        if (
            not isinstance(index, int)
            or isinstance(index, bool)
            or not 0 <= index < len(self.grades)
        ):
            print("ERROR: invalid grade index")
            return False

        self.grades.pop(index)
        return True



    def remove_grade_by_value(self, grade):
        """remove a grade by its value"""
        try:
            self.grades.remove(grade)
        except ValueError:
            print("ERROR: grade not found")
            return False
        return True





    def letter_grade(self):
        """calculate the letter grade"""
        avg = self.calculate_average()
        if avg >= 90:
            return "A"
        if avg >= 80:
            return "B"
        if avg >= 70:
            return "C"
        if avg >= 60:
            return "D"
        return "F"



    def has_passed(self):
        """determine whether the student passed"""
        return bool(self.grades) and self.calculate_average() >= 60



    def report(self):
        """display the student's academic report"""
        status = "Passed" if self.has_passed() else "Failed"
        print("\n--- STUDENT REPORT ---")
        print(f"Student ID: {self.student_id}")
        print(f"Student Name: {self.name}")
        print(f"Number of Grades: {len(self.grades)}")
        print(f"Average Grade: {self.calculate_average():.2f}")
        print(f"Letter Grade: {self.letter_grade()}")
        print(f"Pass/Fail: {status}")
        print(f"Honor Roll: {self.is_honor_roll()}")



def main():
    """show student grade management"""
    students = [
        Student("S001", "Alice"),
        Student("S002", "Bob"),
    ]

    first_student = students[0]
    first_student.add_grade(95.0)
    first_student.add_grade(85.0)

    first_student.add_grade("Fifty")
    first_student.add_grade(120)

    first_student.report()

    first_student.remove_grade_by_value(85.0)
    first_student.remove_grade_by_index(9)

    first_student.report()

    second_student = students[1]
    second_student.add_grade(55)
    second_student.report()

    try:
        Student("", "")
    except ValueError as error:
        print(f"Error creating student: {error}")


if __name__ == "__main__":
    main()
