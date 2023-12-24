year = int(input(""))
if year < 1582:
    print("Not within the Gregorian calender period")
    exit(0)

if (year%4==0) and (year%100!=0):
    print("Leap year")
elif (year%400==0) and (year%100==0):
    print("Leap year")
else:
    print("common year")