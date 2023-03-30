"""
Author: Trevor Snedden
Date: 09//22
Class: ISTA 130


Description:
Program reads the data file, turns values into lists; allowing user to view info.
program allows for adding/removing  names.
when done modifying, converts weight from kilo to pounds then writes to new data file.
"""


def find_insert_position(animal, list):
    """Returns [indexed] position of selected animal from alphabetical ordered list.
    Pulling index will not add, remove, or change list's order.
    """
    if animal.title() in list:
        index = list.index(animal.title())
        return index
    elif animal.title() not in list:
        ordered = list.copy()
        ordered = sorted(ordered + [animal], key=str.lower)  # .index(animal)
        # print(ordered)
        index = ordered.index(animal.title())
        return index


# weight = list of animal's weight, brain = list of animal's brain weight
def populate_lists(animal, weight, brain):
    """Function opens .csv data file and generates a list with the animal's species name, weight, and brain weight.(weights are float.)
    names MUST be in title case.
    columns: name   weight  brain weight
    rows: each animal
    """
    with open("BrainBodyWeightKilos.csv", "r") as file:
        weight_file = file.readline()  # split by name,weight,brain
        while weight_file:
            for elem in [weight_file.split(",")]:
                animal.append(elem[0].title())  # [0] == animal
                weight.append(float(elem[1]))  # [1]== animal weight
                brain.append(float(elem[2]))  # [2] ==  brain weight
            weight_file = file.readline()
    return None


def write_converted_csv(new_csv_file, species_list, weight_list, brain_list):
    """Function takes values from {species_list}{weight_list(kilo)}{brain_list(gram)} converts the respective values to Pounds,
    writes values to {new_csv_file}. Species will be Tile case.
    Conversion: kilo*2.205 = pounds, gram*0.0022 = pounds.
    """
    with open(new_csv_file, "w") as new_file:  # will be 'BrainBodyWeightPounds'
        for elem in range(len(species_list)):
            write = f"{species_list[elem]},{round(float(weight_list[elem])*2.205,2)},{round(float(brain_list[elem])*0.0022,2)}\n"
            new_file.write(write)


def main():
    names = []
    body_weights = []
    brain_weights = []
    populate_lists(names, body_weights, brain_weights)
    while True:
        selected_animal = input('\nEnter animal name (or "q" to quit): ')
        if selected_animal != "q" and selected_animal.title() not in names:
            print(f'File does not contain "{selected_animal.title()}".')
            add = input(f'Add "{selected_animal.title()}" to file? (y|n) ')
            if add == "y":
                index = find_insert_position(selected_animal, names)
                names.insert(index, selected_animal.title())
                body_weights.insert(
                    index,
                    input(
                        f'Enter body weight for "{selected_animal.title()}" in kilograms: '
                    ),
                )
                brain_weights.insert(
                    index,
                    input(
                        f'Enter brain weight for "{selected_animal.title()}" in grams:'
                    ),
                )
        elif selected_animal != "q" and selected_animal.title() in names:
            index = find_insert_position(selected_animal, names)
            print(
                f"{selected_animal.title()}: body = {body_weights[index]}, brain = {brain_weights[index]}"
            )
            if input(f'Delete "{selected_animal.title()}"? (y|n)') == "y":
                for d in names, body_weights, brain_weights:
                    del d[index]
        elif selected_animal == "q":
            write_converted_csv(
                "BrainBodyWeightPounds.csv", names, body_weights, brain_weights
            )
            return False


if __name__ == "__main__":
    main()
