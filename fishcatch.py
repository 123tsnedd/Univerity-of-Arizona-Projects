"""
Author: Trevor Snedden
Date: 11/23/22
Class: ISTA 130

Description:
Extract / creates dictionary from supplied data. key:value = fish_name: weights of caught fish.
final result is a alphabetically depicted chart with number of fish cought(exluding fish with weights labeled as 'NA'); 
American name of fish; mean wt of fish.
    Each line sequence in supplied file:
    0) fish caught number.      1) species code 1-7        2) weight in grams.
    3) length1 nose-tail base.   4) length2 nose-tail notch.    5) length3 nose-end of tail
    6) Height% max height as % of length3.    7) Width% max width of length3
    8) Sex  1=male,  0=female.   (numbers based on index)
"""


def fish_dict_from_file(file):
    """creates dictionary of fish from supplied file. Key will be the fish and float(value) will be the weight.
    each fish will have a single list of all weight value. if there is a NA in fish weihts
    skip fish
    """

    fish_name_dict = {
        1: "Bream",
        2: "Whitefish",
        3: "Roach",
        4: "?",
        5: "Smelt",
        6: "Pike",
        7: "Perch",
    }
    fish_weight = {}  # contains {american fish name[1]: weight[2]}
    with open(file, "r") as fish_file:
        for line in fish_file:
            line = line.strip().split()
            if line[2] != "NA":
                name = fish_name_dict.get(int(line[1]))
                weight = float(line[2])
                if name not in fish_weight:
                    fish_weight[name] = [weight]
                elif name in fish_weight:
                    fish_weight[name].extend([weight])
    return dict(sorted(fish_weight.items()))


def main():
    fish_results = fish_dict_from_file("fishcatch.dat")
    """# NAME    MEAN WT"""
    print("#".rjust(4), "NAME".ljust(10), "MEAN WT".rjust(10))
    for fish in fish_results:
        print(
            str(len(fish_results[fish])).rjust(4),
            fish.ljust(10),
            str(round(sum(fish_results[fish]) / len(fish_results[fish]), 1)).rjust(9)
            + "g",
        )


if __name__ == "__main__":
    main()
