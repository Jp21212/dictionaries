def main():
    grades = {"Maya": 100, "Jp": 99, "Erica": 98, "Vincent": 80}
    fetch_grade(grades)

def fetch_grade(studnet_grades):
    for grade in studnet_grades:
        print(f"{grade} has a grade of {studnet_grades[grade]}")

main()