m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
m4 = int(input("Enter marks of subject 4: "))
m5 = int(input("Enter marks of subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total Marks =", total)
print("Percentage =", percentage)

if percentage < 40:
    print("Grade: Fail")
elif 40 <= percentage < 50:
    print("Grade: D")
elif 50 <= percentage < 60:
    print("Grade: C")
elif 60 <= percentage < 75:
    print("Grade: B")
elif 75 <= percentage < 90:
    print("Grade: A")
else:
    print("Grade: O")
