vowels = "aeiouAEIOU"
alpha = str(input("Enter alphabet: "))

if len(alpha) > 1:
    exit()

if vowels.find(alpha) == -1:
    print("consonant")
else:
    print("vowel")