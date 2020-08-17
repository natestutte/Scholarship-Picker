# Scholarship Picker
# Designed and developed by Nate Stutte
# 
# Project created 8.6.2020
# Last update was 8.7.2020
# 
# Repo : https://github.com/magfmur/Scholarship-Picker


import random

scholarships = []
scholarshipspool = []
scholarshipstrashpool = []


# Command functions

# choice_random : Picks a random scholarship from scholarshippool and adds it to scholarshiptrashpool
# If there are no scholarships left in the pool, reset scholarshipspool and clear scholarshiptrashpool
def choice_random():
    global scholarshipspool
    if len(scholarshipspool) == 0:
            scholarshipspool = scholarshipstrashpool.copy()
            scholarshipstrashpool.clear()
            print("Reshuffling scholarship pool...")
            
    try:
        scholarshippicked = random.choice(scholarshipspool)
    except IndexError:
        print("Error: List of scholarships is empty, add scholarships first!")
    else:
        scholarshipstrashpool.append(scholarshippicked)
        scholarshipspool.remove(scholarshippicked)
        for a in scholarships:
            if a["Name"] == scholarshippicked:
                print(scholarshippicked, "-", a["Link"])
                break
        else:
            print(scholarshippicked)

# choice_add : Add scholarships name and link
# Must enter a unique scholarship with a non-empty link
# Stores it in 'Scholarship.txt'
def choice_add():
    while True:
        name = input("Post name of scholarship to add: ")
        if name.lower() == "quit" or name == "":
            break
        for a in scholarships:
            if a["Name"] == name:
                print("Scholarship already exists, please use 'del' command to delete it or 'edit' command to edit it.")
                break
        else:
            while True:
                link = input("Post link of " + name + ": ")
                if link != "":
                    break
                else:
                    print("Please enter a valid link.")
            
            scholarships.append(dict([("Name", name), ("Link", link)]))
            scholarshipspool.append(name)
            f = open("Scholarships.txt", "a")
            f.write(name + '\n' + link + '\n')
            f.close()

# List command : Lists all scholarships stored
# Lists them in order that they were added
def choice_list():
    for i, a in enumerate(scholarships):
        print(i + 1, ":", a["Name"], '-', a["Link"])

# Del command : Deletes scholarship from list
# Must give name of scholarship
def choice_del():
    while True:
        name = input("Post name of scholarship to delete: ")
        if name.lower() == "quit" or name == "":
            break
        for a in scholarships:
            if a["Name"].lower() == name.lower():
                # delete scholarship from file
                with open("Scholarships.txt", "r") as f:
                    lines = f.readlines()
                with open("Scholarships.txt", "w") as f:
                    for line in lines:
                        if line.rstrip('\n') != a["Name"] and line.rstrip('\n') != a["Link"]:
                            f.write(line)

                scholarships.remove(a)
                if name in scholarshipspool:
                    scholarshipspool.remove(name)
                else:
                    scholarshipstrashpool.remove(name)
                print(name, "has been removed.")
                break
        else:
            print("Scholarship not found. Make sure scholarship exists or is typed correctly.")
        
def choice_help():
    pass

# Importing/Creating 'Scholarship.txt' file
def import_file():
    try:
        f = open("Scholarships.txt", "r")
    except (OSError, IOError):
        f = open("Scholarships.txt", "x")
        f.close()
        f = open("Scholarships.txt", "r")
    return f


# Main function
def main():

    f = import_file()

    # Create dict of scholarship names and links
    for i, a in enumerate(f):
        if i % 2 == 0:
            scholarships.append(dict({"Name" : a.rstrip('\n')}))
        else:
            scholarships[-1]["Link"] = a.rstrip('\n')
    f.close()

    for a in scholarships:
        scholarshipspool.append(a["Name"])

    # Main loop
    while True:
        selection = input("> ").lower()

        if selection == "random":
            choice_random()
        
        elif selection == "add":
            choice_add()
        
        elif selection == "list":
            choice_list()
        
        elif selection == "del":
            choice_del()

        # Commands yet to be added
        elif selection == "edit" or selection == "help":
            print("To be implemented")
        
        # Quit command : Quits the program :)
        elif selection == "quit":
            break
        
        # Invalid command aka any command not recognized
        else:
            print("INVALID OPTION")


if __name__ == "__main__":
    main()