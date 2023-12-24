secret_number = 1234

while True:
    num = int(input("enter number: "))
    if num == secret_number:
        print("Well done, muggle! You are free now.")
        break
    else:
        print("Ha ha! You're stuck in my loop!")