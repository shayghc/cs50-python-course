names = []


for _ in range(6):
    name = input("Enter name: ")
    names.append(name)
    
for name in names[:-1]:
    print(f"{name}, ", end="")
    
print(f"and {names[len(names) - 1]} are all Connollys")