file = "books/frankenstein.txt"

with open(file) as f:
    file_contents = f.read()
    words = file_contents.split()
    characters = {}
    for w in words:
        for raw_char in w:
            if raw_char.isalpha():
                c = raw_char.lower()
                if c not in characters:
                    characters[c] = 0
                characters[c] = characters[c] + 1

    lst = sorted(
        ((x, characters[x]) for x in characters), key=lambda x: x[1], reverse=True
    )

    print(f"--- Bookbot Report of {file} ---")
    print(f"{len(words)} total words were found in the file")
    print()

    for tp in lst:
        print(f'The "{tp[0]}" character was found {tp[1]} times')

    print()
    print("--- End Report ---")
