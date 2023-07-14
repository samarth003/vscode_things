class region:
    iteration = 0
    pokemon_chosen = "FAILURE"
    def __init__(self, fname="Misty", lname="Lee", township="Verulean City"):
        self.fname = fname
        self.lname = lname
        self.township = township

    def entrant_intro(self):
        print("Hello, I am " + self.fname + " "+ self.lname  + " "+ "from " + self.township)

    def choose_starter_pokemon(self, name="pikachu"):
        if(name.lower() == "pikachu"):
            self.pokemon_chosen = "SUCCESS"
            print("pika pika pikachu")
        elif(name.lower() == "bulbasaur"):
            self.pokemon_chosen = "SUCCESS"
            print("saur bulbasaur")
        elif(name.lower() == "charmander"):
            self.pokemon_chosen = "SUCCESS"
            print("char char charrr mander")
        self.iteration += 1
        return self.pokemon_chosen, self.iteration
    
    def iterate_check(self, name):
        starter_mon, iter_val = self.choose_starter_pokemon(name)
        if starter_mon != "SUCCESS" and iter_val < 3:
            print("Choose again from the starter pokemons")
        else:
            print("Out of luck, kid. Catch'em in the wild.")
        return starter_mon, iter_val