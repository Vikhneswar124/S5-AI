# Get marks input from user
marks = float(input("Enter the student's marks (out of 100): "))

# Check and print the grade
if marks >= 90:
    print("Grade A")
elif 75 <= marks < 90:
    print("Grade B")
elif 60 <= marks < 75:
    print("Grade C")
elif 40 <= marks < 60:
    print("Grade D")
else:
    print("Fail")

