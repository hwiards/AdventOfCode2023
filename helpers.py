
def char_to_number(character: str, reference = None):
    if len(character) != 1:
        print("Not a character")
        return None

    if reference == None:
        if not character.isalpha():
            print(f"{character} is not alphabetic")
            return None

        if character.islower():
            return ord(character) - ord('a')
        if character.isupper():
            return ord(character) - ord('A')
    else:
        if len(reference) == 1:
            return ord(character) - ord(reference)
        if reference == "lu":
            if character.islower():
                return ord(character) - ord('a')
            if character.isupper():
                return ord(character) - ord('A') + 26

        if reference == 'ul':
            if character.islower():
                return ord(character) - ord('a') + 26
            if character.isupper():
                return ord(character) - ord('A')


def grouped(iterable, n):
    return zip(*[iter(iterable)]*n)