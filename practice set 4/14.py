email = ""
for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    email = email + ch

print(email)