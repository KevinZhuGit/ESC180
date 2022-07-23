# opening files

with open('data.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    if 'lol' in line.lower():
        print(line)
