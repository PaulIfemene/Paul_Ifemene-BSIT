import tkinter as tk
from tkinter import messagebox

def check_age():
    try:
        age = int(age_entry.get())
        if age >= 18:
            result = "You are eligible to vote!"
        else:
            result = "You are NOT eligible to vote."
        messagebox.showinfo("Voting Eligibility", result)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid age.")

# GUI setup
root = tk.Tk()
root.title("Voting Eligibility Checker")

tk.Label(root, text="Enter your age:").pack(pady=10)
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Button(root, text="Check Eligibility", command=check_age).pack(pady=10)

root.mainloop()# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 


# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 





# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 


# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the ava# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 


# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the ava# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 


# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

   # Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 

# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (ass_1+ass_2+ass_3+ass_4)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams") 
# Exam Verification program
# get values from 4 assignments and store them in a list

ass_1 = int(input("Enter marks for assingment 1: "))
ass_2 = int(input("Enter marks for assingment 2: "))
ass_3 = int(input("Enter marks for assingment 3: "))
ass_4 = int(input("Enter marks for assingment 4: "))

# the list in the variable assignment has the scores from 4 assignments
assignments = [ass_1, ass_2, ass_3, ass_4]
# then we find the ava