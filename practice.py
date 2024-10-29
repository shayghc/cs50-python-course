names = []

with open("names.txt", "r") as file:
    for line in file:
        names.append(line.strip())
        
with open("names.txt", "w") as file:
    for name in sorted(names):
        file.write(f"{name}\n")