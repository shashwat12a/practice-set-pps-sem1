english = int(input("Enter marks of english: "))
maths = int(input("Enter marks of maths: "))
physics = int(input("Enter marks of physics: "))
chemistry = int(input("Enter marks of chemistry: "))
cs = int(input("Enter marks of cs:"))

total = (english+maths+physics+chemistry+cs)
per = (total/500)*100

print("avgerage percentage is:", per)