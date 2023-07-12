import region_common

MAX_COUNT = 3
def main():
    starter_mon_selected = "FAILURE"
    selection_count = 0
    trainer_fname = input("Enter your first name: ")
    trainer_lname = input("Enter your last name: ")
    trainer_township = input("Enter your township: ")

    kanto = region_common.region(trainer_fname, trainer_lname, trainer_township)
    kanto.entrant_intro()
    
    while (selection_count < MAX_COUNT) and (starter_mon_selected != "SUCCESS"):
        starter_pokemon = input("choose your starter pokemon!")
        starter_mon_selected, selection_count = kanto.iterate_check(starter_pokemon)

if __name__ == "__main__":
    main()