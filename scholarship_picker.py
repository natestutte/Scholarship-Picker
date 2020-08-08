import random

scholarships = {}
scholarshipspool = []
scholarshipstrashpool = []

try:
    f = open("Scholarships.txt", "r")
except (OSError, IOError):
    f = open("Scholarships.txt", "x")
    f.close()
    f = open("Scholarships.txt", "r")
finally:
    for i, a in enumerate(f):
        if i % 2 == 0:
            lastkey = a.rstrip('\n')
            scholarships[a.rstrip('\n')] = None
        else:
            scholarships[lastkey] = a.rstrip('\n')
    f.close()

    scholarshipspool = list(scholarships.keys())

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
                print(scholarshippicked, "-", scholarships[scholarshippicked])
        
        elif selection == "add":
            while True:
                name = input("Post name of scholarship to add: ")
                if name in scholarships.keys():
                    print("Scholarship already exists, please use 'del' command to delete it or 'edit' command to edit it.")
                    continue
                if name == "quit" or name == "":
                    break
                while True:
                    link = input("Post link of " + name + ": ")
                    if link != "":
                        break
                    else:
                        print("Please enter a valid link.")
                
                scholarships[name] = link
                scholarshipspool.append(name)
                f = open("Scholarships.txt", "a")
                f.write(name + '\n' + link + '\n')
                f.close()
        
        elif selection == "list":
            for i, a in enumerate(scholarships.keys()):
                print(i + 1, ":", a, '-', scholarships[a])
        
        elif selection == "del" or selection == "edit":
            print("To be implemented")
        
        elif selection == "quit":
            break
        
        else:
            print("INVALID OPTION")
        

