inp1 = input("enter a char: ")

if len(inp1) > 1:
    print("input too long")
    exit(0)

if inp1.isupper() == True:
    print(inp1.lower())
else:
    print(inp1.upper())