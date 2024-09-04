# Exam Verification program
# the list in the variable assignment has the scores from 4 assignments
assignments = [78,85,95,64]
# then we find the avarage of all the values in in assignment and store it in a variable coursework_marks  
coursework_score = (78+85+95+64)/4
# then print/display the value in the variable coursework_marks  
print(f"Your coursework score is:", coursework_score, f"out of 100")

# Use of conditional statment to check if a student is eligible to sit for exams
if coursework_score >= 35:
    print(f"congratulations, You are qualified to site for the Exams")

else:
    print(f"Sorry, you are not qualified to sit foe the Exams")    