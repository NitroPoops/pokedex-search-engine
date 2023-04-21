import pandas as pd
import random

# Load the Pokemon.csv file into a DataFrame
path = "../Pokemon.csv"
pokedex = pd.read_csv(path)


# Displays all Pokemons without truncation
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)
pd.set_option("display.max_row", None)


def display_menu():
    """Display a menu of options for the user to choose from."""

    print(
        """==================================================================
Pokedex Search Engine Menu:
1. Display selected number of Pokemons with types and statistics
2. Display the first Pokemon of a Type of the user's choice
3. Display all Pokemons with Total Base stat of the user's choice
4. Display all Pokemons with minimum set of stats
5. Display all legendary Pokemons of Types of the user's choice
0. Exit
=================================================================="""
    )


# Option 1
def display_pokemon_stats(num_pokemon):
    """Display selected number of Pokemons with types and statistics."""

    print(pokedex.head(num_pokemon))
    print()


# Option 2
def display_first_pokemon_of_type(pokemon_type):
    """Display the first Pokemon of a Type of the user's choice."""

    matching_pokemon = pokedex.loc[pokedex["Type 1"] == pokemon_type]
    print()
    if matching_pokemon.empty:
        print("There are no Pokemons with type", pokemon_type)
    else:
        print(matching_pokemon.head(1))
    print()


# Option 3
def display_pokemon_with_total_base_stat(total_stat):
    """Display all Pokemons with Total Base stat of the user's choice."""

    matching_pokemon = pokedex.loc[pokedex["Total"] == total_stat]
    print()
    if matching_pokemon.empty:
        print("No Pokemon with total base stat", total_stat)
    else:
        print(matching_pokemon)
    print()


# Option 4
def display_pokemon_with_minimum_stats(hp, attack, defense, sp_atk, sp_def, speed):
    """Display all Pokemons with a minimum set of stats."""

    print()
    print(
        pokedex.loc[
            (pokedex["HP"] >= hp)
            & (pokedex["Attack"] >= attack)
            & (pokedex["Defense"] >= defense)
            & (pokedex["Sp. Atk"] >= sp_atk)
            & (pokedex["Sp. Def"] >= sp_def)
            & (pokedex["Speed"] >= speed)
        ]
    )
    print()


# Option 5
def display_legendary_pokemon_of_type(type_1, type_2):
    """Display all legendary Pokemons of Types of the user's choice."""

    legendaries = pokedex.loc[pokedex["Legendary"] == True]
    print()
    print(
        legendaries.loc[
            (legendaries["Type 1"] == type_1) & (legendaries["Type 2"] == type_2)
        ]
    )
    print()


# Surpise within exit option
def surprise():
    """One in three chance of prompting user before exiting the programme."""

    if random.randint(1, 3) == 1:
        fav_pokemon = input(
            "\nWait! Before you go, input your favourite Pokemon: "
        ).capitalize()

        if fav_pokemon in pokedex["Name"].values:
            print(f"\nGood choice. This is {fav_pokemon}'s stats:")
            print(pokedex.loc[pokedex["Name"] == fav_pokemon].head(1))
        else:
            print("Nevermind.")


# Display menu and take in user's inputs
while True:
    display_menu()
    option = int(input("\nEnter an option: "))

    if option == 1:
        num_pokemon = int(input("\nEnter the number of Pokemons to display: "))
        display_pokemon_stats(num_pokemon)

    elif option == 2:
        pokemon_type = input("\nEnter the Type of Pokemon to display: ").capitalize()
        display_first_pokemon_of_type(pokemon_type)

    elif option == 3:
        total_stat = int(input("\nEnter the Total Base stat to display: "))
        display_pokemon_with_total_base_stat(total_stat)

    elif option == 4:
        print()
        hp = int(input("Enter the minimum HP: "))
        attack = int(input("Enter the minimum Attack: "))
        defense = int(input("Enter the minimum Defense: "))
        sp_atk = int(input("Enter the minimum Sp. Atk: "))
        sp_def = int(input("Enter the minimum Sp. Def: "))
        speed = int(input("Enter the minimum Speed: "))
        display_pokemon_with_minimum_stats(hp, attack, defense, sp_atk, sp_def, speed)

    elif option == 5:
        type_1 = input("Enter Pokemon type 1: ").capitalize()
        type_2 = input("Enter Pokemon type 2: ").capitalize()
        display_legendary_pokemon_of_type(type_1, type_2)

    elif option == 0:
        surprise()

        print("\nGoodbye!")
        break

    else:
        print("Invalid option. Please try again.\n")
