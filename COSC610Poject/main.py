import re

possibleGuitars = [];

classicGuitar = {"name: Classic Guitar", "yellow", "normal", "cheap"};
metalGuitar = {"name: Metal Guitar", "black", "metal", "expensive"};
rockGuitar = {"name: Rock Guitar", "red", "rock", "expensive"};

listOfSets = [classicGuitar, metalGuitar, rockGuitar]

checkSet = {input("Enter attribute: ")}

count = 0

for count in range(len(listOfSets)):
    if checkSet.issubset(listOfSets[count]):
        for i in listOfSets[count]:
            if re.match("name", i):
                i = i.removeprefix("name: ")
                possibleGuitars.append(i);

print("Recommended guitars: ")
for i in possibleGuitars:
    if i != possibleGuitars[len(possibleGuitars) - 1]:
        print (i, end = ", ")
    else:
        print(i, end=".")
