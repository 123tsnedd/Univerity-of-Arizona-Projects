"""
Author: Trevor Snedden
Date: 11/28/22
Class: ISTA 130
Description:
file line order: emoticon - tweet ID - user id - timestamp

This algorithm, only interested in emoticon[0] & user ID[2]
"""


def load_twitter_dicts_from_file(file, emoticons_to_ids, ids_to_emoticons):
    """reads file and loads two dicts(strip quotes & Strings casting to int will fail.
    .dat file's emoticon and user ID are double quoted ""ID"", strip outer quotes.
    return None."""

    with open(file, "r") as f:
        line = f.readline().replace('"', "").split()
        while line:
            if line[0] not in emoticons_to_ids:
                emoticons_to_ids[line[0]] = [line[2]]
            elif line[0] in emoticons_to_ids:
                emoticons_to_ids[line[0]].extend([line[2]])
            if line[2] not in ids_to_emoticons:
                ids_to_emoticons[line[2]] = [line[0]]
            elif line[2] in ids_to_emoticons:
                ids_to_emoticons[line[2]].extend([line[0]])
            line = f.readline().replace('"', "").split()
        return None


def find_most_common(dict):
    """function returns the key with the longest list.
    ex.  :).ljust(21) occurs(notjsut)  871.rjust(9) times"""
    max_key = max(dict, key=lambda key: len(dict[key]))  # get key with max value len.
    val_len = len(
        dict.get(max(dict, key=lambda key: len(dict[key])))
    )  # get key with max value len.
    print(f"{max_key.ljust(20)} occurs {str(val_len).rjust(8)} times")
    return max_key


def main():
    emoticons_to_ids = {}
    ids_to_emoticons = {}

    load_twitter_dicts_from_file(
        "twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons
    )
    # find_most_common(emoticons_to_ids)
    print("Emoticons:", len(emoticons_to_ids))
    print("UserIDs:  ", len(ids_to_emoticons))
    for x in range(5):
        max_key = find_most_common(emoticons_to_ids)
        emoticons_to_ids.pop(max_key)


if __name__ == "__main__":
    main()
