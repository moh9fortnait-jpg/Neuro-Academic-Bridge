# Project 11: Neuro-Academic Bridge
# A weighted average calculator for students

def calculate_average(grades_data):
    total_points = sum(grade * coef for grade, coef in grades_data)
    total_coefs = sum(coef for grade, coef in grades_data)
    return total_points / total_coefs if total_coefs > 0 else 0

def main():
    print("--- Neuro-Academic Bridge v1.0 ---")
    subjects = []
    print("Enter grades and coefficients. Type 'done' to calculate.")
    
    while True:
        sub = input("Subject name (or 'done'): ")
        if sub.lower() == 'done': break
        try:
            grade = float(input(f"Grade for {sub} (0-20): "))
            coef = int(input(f"Coefficient for {sub}: "))
            subjects.append((grade, coef))
        except ValueError:
            print("Invalid input.")

    if subjects:
        avg = calculate_average(subjects)
        print(f"\nYour Final Average: {avg:.2f}/20")
        print("Status: " + ("Success! Keep going." if avg >= 10 else "Needs more effort."))