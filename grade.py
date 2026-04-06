marks = int(input("Enter your marks: "))

if marks < 40:
    print("Grade: Fail")
elif 40 <= marks < 50:
    print("Grade: D")
elif 50 <= marks < 60:
    print("Grade: C")
elif 60 <= marks < 75:
    print("Grade: B")
elif 75 <= marks < 90:
    print("Grade: A")
elif marks >= 90:
    print("Grade: O")
else:
    print("Invalid Input")