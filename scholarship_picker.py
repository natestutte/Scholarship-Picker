# Scholarship Picker
# Designed and developed by Nate Stutte
# 
# Project created 8.6.2020
# Last update was 8.7.2020
# 
# Repo : https://github.com/magfmur/Scholarship-Picker


import random
import sys

scholarships = []
scholarshipspool = []
scholarshipstrashpool = []

def create_scholarship_dict():
    f = import_file()
    
    for i, a in enumerate(f):
        if i % 2 == 0:
            scholarships.append(dict({"Name" : a.rstrip('\n')}))
        else:
            scholarships[-1]["Link"] = a.rstrip('\n')
    f.close()

    for a in scholarships:
        scholarshipspool.append(a["Name"])

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
    try:
        name = sys.argv[2]
    except:
        return
    for a in scholarships:
        if a["Name"] == name:
            print("Scholarship already exists, please use 'del' command to delete it or 'edit' command to edit it.")
            break
    else:
        try:
            link = sys.argv[3]
        except:
            return

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
    try:
        del_selection = sys.argv[2]
    except:
        return
    for a in scholarships:
        if a["Name"].lower() == del_selection.lower():
            # delete scholarship from file
            delete_scholarship(a)
            break
    else:
        print("Scholarship not found. Make sure scholarship exists or is typed correctly.")

# Commands in progress
def choice_edit():
    pass

def choice_help():
    pass

def choice_help(arg):
    pass

def choice_contributors():
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

# Deleting scholarship "ss" from file
def delete_scholarship(ss):
    with open("Scholarships.txt", "r") as f:
        lines = f.readlines()
    with open("Scholarships.txt", "w") as f:
        for line in lines:
            if line.rstrip('\n') != ss["Name"] and line.rstrip('\n') != ss["Link"]:
                f.write(line)

    name = ss["Name"]
    if name in scholarshipspool:
        scholarshipspool.remove(name)
    else:
        scholarshipstrashpool.remove(name)
    print(name, "has been removed.")

# Main function
def main():
    try:
        selection = sys.argv[1]
    except:
        return

    if selection == "-r":
        create_scholarship_dict()
        choice_random()
    elif selection == "-a":
        create_scholarship_dict()
        choice_add()
    elif selection == "-l":
        create_scholarship_dict()
        choice_list()
    elif selection == "-d":
        create_scholarship_dict()
        choice_del()
    # Commands yet to be added
    elif selection == "-e" or selection == "-h" or selection == "-c":
        print("To be implemented")
    # Invalid command aka any command not recognized
    else:
        print("INVALID OPTION")

if __name__ == "__main__":
    main()
