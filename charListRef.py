charList = {}
file = open("characterList.txt")
key = 0
for line in file:
    charList[key] = line.rstrip()
    key += 1

print(charList.items())