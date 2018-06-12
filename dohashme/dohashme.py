"""
PROBLEM
Write code to find a six letter string of characters that contains only
letters from
    'acdefgilmnoprstuwy'
Such that the hash('the strinng') is
    '18754844497'
If hash is defined as the function found on this file.


ANALYSIS
Hashes obtained from this function will be a set of ordered numbers
if strings are constructed of consecutively characters for the given
alphabet. For example:

    hash("a") = 259
    hash("c") = 260

So we can find the candidates moving from right to left and checking
if is near the result as show in dehash function.
"""

alphabet = ""


def hash(st):
    global alphabet
    h = 7
    letters = alphabet
    for i in range(len(st)):
        h = h * 37 + letters.index(st[i])
    return h


def set_alphabet(custom_alphabet):
    global alphabet
    alphabet = custom_alphabet


def get_str_from_coord(coordinates):
    return "".join([alphabet[i] for i in coordinates])


def dehash(target_number, length=6):
    # start from first array of characters ie: 'aaaaaa'
    result = [0 for i in range(length)]
    # for each position in the string we are looking for.
    for i in range(len(result)):
        # if the target hash number is greater we try next character.
        while hash(get_str_from_coord(result)) <= target_number:
            result[i] = result[i]+1
            # special case last alphabet letter.
            if result[i] >= len(alphabet):
                break
        # when hash number is lower we just take over, so pick the last character
        result[i] = result[i] - 1
    return get_str_from_coord(result)


if "main" in __name__:
    letters = "acdefgilmnoprstuwy"
    set_alphabet(letters)
    target = 18754844497
    length = 6
    result = dehash(target, length=length)
    print("hash('{}') gives '{}' hash.".format(result, target))
