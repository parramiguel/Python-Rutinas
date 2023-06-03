string = input("Put your string here: ")

letter_count = {}
for letter in string:
    if not letter in letter_count:
        letter_count[letter] = 1
    else:
        letter_count[letter] += 1
print(letter_count)
