 RoyceSpratling_assignment_3.py
# Step 1

student_name = "Royce Spratling"
current_gpa = 3.2        # between 1.0 and 4.0
study_hours = 25         # integer
social_points = 50       # integer
stress_level = 40        # between 0 and 100

print(f"Welcome to College Life Adventure, {student_name}!")
print("Starting stats:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")
print("\nChoose your course load:")
print("A) Light (12 credits)")
print("B) Standard (15 credits)")
print("C) Heavy (18 credits)")

choice = input("Your choice: ")

if choice == "A":
    # Light course load
    study_hours += 5
    stress_level -= 5
    print("You chose a light course load. You have more time to study and relax.")

elif choice == "B":
    # Standard course load
    study_hours += 2
    stress_level += 5
    print("You chose a standard course load. A balanced semester ahead.")

else:     # Covers choice == "C" and also any invalid input
    # Heavy course load
    if current_gpa >= 3.5:
        study_hours += 3
        stress_level += 15
        print("You took a heavy load but your high GPA helps you handle it.")
    else:
        study_hours -= 2
        stress_level += 25
        print("You took a heavy load and it’s a struggle. Your stress increased!")

print(f"\nUpdated stats after course selection:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# -----------------------
# Step 3: Study Strategy
# -----------------------

print("\nTime to choose a study strategy!")
available_subjects = ["Programming", "Math", "English", "History"]

print("Available subjects to focus on:")
print("- Programming")
print("- Math")
print("- English")
print("- History")

study_choice = input("Which subject will you focus on? ")

# First, explicitly check for invalid input using NOT IN
if study_choice not in available_subjects:
    print("Invalid subject choice. You wasted study time.")
    stress_level += 10
    current_gpa -= 0.1

else:  # valid choice
    print(f"You chose to focus on {study_choice}.")

    # Use logical operators to adjust stats
    if study_choice == "Programming" or study_choice == "Math":
        current_gpa += 0.2
        stress_level += 5
        print("STEM subjects improved your GPA but increased stress.")
    elif study_choice == "English" or study_choice == "History":
        current_gpa += 0.1
        social_points += 10
        print("Humanities improved your GPA slightly and boosted social life.")

print(f"\nStats after study decision:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

# -----------------------
# Step 4: Final Semester Assessment
# -----------------------

print("\nFinal Semester Assessment!")

final_choice = input("Enter a number (1, 2, or 3) to decide your final path: ")

# Check type with identity operator
if type(final_choice) is str:   # using 'is' for type comparison
    if final_choice.isdigit():
        final_choice = int(final_choice)

        # Now use 'is' for the actual final decision
        if final_choice is 1:
            if current_gpa >= 3.5 and stress_level < 60:
                print("Ending 1: Honors Graduate! You balanced study and stress well.")
            else:
                print("Ending 1: Graduated, but it was a tough journey.")

        elif final_choice is 2:
            if social_points >= 60 and stress_level < 70:
                print("Ending 2: Social Butterfly! You made lifelong friends.")
            else:
                print("Ending 2: You partied hard, but your academics suffered.")

        elif final_choice is 3:
            if stress_level > 70:
                print("Ending 3: Burnout… You pushed too hard and need a break.")
            else:
                print("Ending 3: You maintained balance and graduated steadily.")

        else:
            print("Invalid final path number.")
    else:
        print("Invalid input: expected a number.")
else:
    print("Error: final_choice is not a string as expected.")

print("\nFinal Stats:")
print(f"GPA: {current_gpa}")
print(f"Study Hours: {study_hours}")
print(f"Social Points: {social_points}")
print(f"Stress Level: {stress_level}")

