import random

scholarships = []
scholarshipspool = []
scholarshipstrashpool = []

try:
    f = open("Scholarships.txt", "r")
except FileNotFoundError:
    f = open("Scholarships.txt", "x")
    f.close()
    f = open("Scholarships.txt", "r")
finally:
    for a in f:
        scholarships.append(a)
    f.close()

    scholarshipspool = scholarships.copy()

    while True:
        selection = input("> ").lower()
        if selection == "random":
            if len(scholarshipspool) == 0:
                scholarshipspool = scholarshipstrashpool.copy()
                scholarshipstrashpool.clear()
            
            try:
                scholarshippicked = random.choice(scholarshipspool)
            except IndexError:
                print("Error: List of scholarships is empty, add scholarships first!")
            else:
                scholarshipstrashpool.append(scholarshippicked)
                scholarshipspool.remove(scholarshippicked)
                print(scholarshippicked)
        
        elif selection == "add":
            while True:
                selection = input("Post link of scholarship to add: ")
                if selection == "":
                    break
                scholarships.append(selection)
                scholarshipspool.append(selection)
                f = open("Scholarships.txt", "a")
                f.write(selection + '\n')
                f.close()
        
        elif selection == "list":
            for i, a in enumerate(scholarships):
                print(i + 1, "-", a)
        
        elif selection == "quit":
            break
        
        else:
            print("INVALID OPTION")
        

