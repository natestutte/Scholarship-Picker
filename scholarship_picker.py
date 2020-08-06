import random
from os import path

scholarships = []
scholarshipspool = []

f = open("Scholarships.txt", "w")
f.close()

f = open("Scholarships.txt", "r")
for a in f:
    scholarships.append(a)
f.close()

while True:
    selection = input("> ").lower()
    if selection == "random":
        if len(scholarships) == 0:
            scholarships = scholarshipspool.copy()
            scholarshipspool.clear()
        scholarshippicked = random.choice(scholarships)
        scholarshipspool.append(scholarshippicked)
        scholarships.remove(scholarshippicked)
        print(scholarshippicked)
    elif selection == "add":
        while True:
            selection = input("Post link of scholarship to add: ")
            if selection == "":
                break
            scholarships.append(selection)
            f = open("Scholarships.txt", "a")
            f.write(selection + '\n')
            f.close()
    elif selection == "quit":
        break
    else:
        print("INVALID OPTION")
    
