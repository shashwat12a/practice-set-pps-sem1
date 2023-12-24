n = int(input("Enter n: "))

if n%2!=0:
    print("Not Win")
elif n%2==0 and (n>=2 and n<=5):
    print("Win")
elif n%2==0 and (n>=6 and n<=20):
    print("Not  Win")
else:
    print("Win")

