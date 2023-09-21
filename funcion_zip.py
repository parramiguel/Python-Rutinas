names = ("Luis", "Diego", "Andrés", "Carlos")
ages = [15, 30, 26, 12, 40]
text = "Geekiepedia"

print(names)
print(ages)
print(text)

print("\nFunción zip() como iterable: \n")
combination = zip(names, ages, text)
print(combination)

print("\nFunción zip() con la función list(): \n")
combination = list(zip(names, ages, text))
print(combination)

print("\nFunción zip() con la función tuple(): \n")
combination = tuple(zip(names, ages, text))
print(combination)

print("\nFunción zip() con for: \n")
for name, age, s_text in zip(names, ages, text):
    print(name, age, s_text)
