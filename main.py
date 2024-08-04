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

    print(f"--- Bookbot Report of {file} ---")
    print(f"{len(words)} total words were found in the file")
    print()

    print()
    print("--- End Report ---")
