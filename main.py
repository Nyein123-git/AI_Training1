
# Student Performance Analyzer
# Python for AI - Day 1


# Fixed grade categories using a tuple
GRADE_CATEGORIES = ("Excellent", "Good", "Pass", "Fail")


def calculate_average(scores):
    """Return the average score."""
    if not scores:
        return 0
    return sum(scores) / len(scores)


def classify_grade(score):
    """Return the student's grade."""
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 80:
        return GRADE_CATEGORIES[0]
    elif score >= 60:
        return GRADE_CATEGORIES[1]
    elif score >= 40:
        return GRADE_CATEGORIES[2]
    else:
        return GRADE_CATEGORIES[3]


def count_passed(students):
    """Return the number of passing students."""
    return sum(
        1 for student in students
        if student["Score"] >= 40
    )


def get_valid_integer(prompt, minimum, maximum=None):
    """Get a valid integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if value < minimum:
                print(f"Value must be at least {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
            else:
                return value

        except ValueError:
            print("Please enter a valid whole number.")


def get_valid_float(prompt, minimum=0, maximum=None):
    """Get a valid numeric value from the user."""
    while True:
        try:
            value = float(input(prompt))

            if value < minimum:
                print(f"Value must be at least {minimum}.")
            elif maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
            else:
                return value

        except ValueError:
            print("Please enter a valid number.")


def collect_students():
    """Collect information for at least five students."""
    students = []

    number_of_students = get_valid_integer(
        "Enter number of students (minimum 5): ", 5
    )

    for i in range(number_of_students):
        print(f"\n--- Student {i + 1} ---")

        while True:
            name = input("Enter student name: ").strip()
            if name:
                break
            print("Name cannot be empty.")

        age = get_valid_integer("Enter age: ", 1)
        study_hours = get_valid_float(
            "Enter study hours: ", 0
        )
        score = get_valid_float(
            "Enter Python score (0-100): ", 0, 100
        )

        # Dictionary stores each student's information
        student = {
            "Name": name,
            "Age": age,
            "Study Hours": study_hours,
            "Score": score,
            "Grade": classify_grade(score)
        }

        students.append(student)

    return students


def display_report(students):
    """Display student records and summary statistics."""
    scores = [student["Score"] for student in students]

    print("\n" + "=" * 15 + " STUDENT PERFORMANCE REPORT " + "=" * 15)

    for student in students:
        print(f"\nName: {student['Name']}")
        print(f"Age: {student['Age']}")
        print(f"Study Hours: {student['Study Hours']}")
        print(f"Score: {student['Score']}")
        print(f"Grade: {student['Grade']}")

    total_students = len(students)
    average_score = calculate_average(scores)
    highest_score = max(scores)
    lowest_score = min(scores)
    passed_students = count_passed(students)
    failed_students = total_students - passed_students

    # Find the student with the highest score
    top_student = max(students, key=lambda student: student["Score"])

    print("\n" + "=" * 20 + " SUMMARY " + "=" * 20)
    print(f"Total Students: {total_students}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Highest Score: {highest_score}")
    print(f"Lowest Score: {lowest_score}")
    print(f"Passed Students: {passed_students}")
    print(f"Failed Students: {failed_students}")
    print(f"Top Student: {top_student['Name']}")


def main():
    """Main program."""
    print("=" * 10 + " STUDENT PERFORMANCE ANALYZER " + "=" * 10)

    students = collect_students()
    display_report(students)

    print("\nStudent Performance Analyzer completed successfully!")


if __name__ == "__main__":
    main()
