# Scholarship Picker
# Designed and developed by Nate Stutte
# 
# Project created 8.6.2020
# Last update was 8.7.2020
# 
# Repo : https://github.com/magfmur/Scholarship-Picker

import random

scholarships = {}
scholarshipspool = []
scholarshipstrashpool = []

# Importing/Creating 'Scholarship.txt' file
try:
    f = open("Scholarships.txt", "r")
except (OSError, IOError):
    f = open("Scholarships.txt", "x")
    f.close()
    f = open("Scholarships.txt", "r")
finally:
    
    # Create dict of scholarship names and links
    for i, a in enumerate(f):
        if i % 2 == 0:
            lastkey = a.rstrip('\n')
            scholarships[a.rstrip('\n')] = None
        else:
            scholarships[lastkey] = a.rstrip('\n')
    f.close()

    scholarshipspool = list(scholarships.keys())

    # Main loop
    while True:
        selection = input("> ").lower()

        # Random command : Picks a random scholarship from scholarshippool and adds it to scholarshiptrashpool
        # If there are no scholarships left in the pool, reset scholarshipspool and clear scholarshiptrashpool
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
        
        # Add command : Add scholarships name and link
        # Must enter a unique scholarship with a non-empty link
        # Stores it in 'Scholarship.txt'
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
        
        # List command : Lists all scholarships stored
        # Lists them in order that they were added
        elif selection == "list":
            for i, a in enumerate(scholarships.keys()):
                print(i + 1, ":", a, '-', scholarships[a])
        
        # Commands yet to be added
        elif selection == "del" or selection == "edit":
            print("To be implemented")
        
        # Quit command : Quits the program :)
        elif selection == "quit":
            break
        
        # Invalid command aka any command not recognized
        else:
            print("INVALID OPTION")
        

