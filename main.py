import random


def starter_Pokemon():
    pokemon_list = ["Bulbasaur", "Charmander", "Squirtle"]
    return random.choice(pokemon_list)


def main():
    print("Welcome to the world of Pokemon!")
    print("Please choose your starter Pokemon:")
    print("1. Bulbasaur")
    print("2. Charmander")  
    print("3. Squirtle")    
    print("Or type 'random' to get a random starter")

    choice = input("Enter the number of your choice: ")

    if choice == "1":
        print("You chose Bulbasaur! A Grass/Poison type Pokemon.")
    elif choice == "2":
        print("You chose Charmander! A Fire type Pokemon.")
    elif choice == "3":
        print("You chose Squirtle! A Water type Pokemon.")
    elif choice == "random":
        pokemon = starter_Pokemon()
        print(f"You got {pokemon} as your starter Pokemon!")
    elif choice == "4":
        print("You chose to exit the game. Goodbye!")
    else:
        print("Invalid choice. Please choose a valid starter Pokemon.")
    
if __name__ == "__main__":
    main()