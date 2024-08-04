file = "books/frankenstein.txt"

with open(file) as f:
    raw_file = f.read()
    all_words = raw_file.split()

    characters = {}
    for word in all_words:
        for char in word:
            if char.isalpha():
                letter = char.lower()
                if letter not in characters:
                    characters[letter] = 0
                characters[letter] += 1

    ordered_letter_count_list = sorted(
        ((letter, characters[letter]) for letter in characters),
        key=lambda letter_count_tuple: letter_count_tuple[1],
        reverse=True,
    )

    print(f"--- Bookbot Report of {file} ---")
    print(f"{len(all_words)} total words were found in the file")
    print()

    for item in ordered_letter_count_list:
        print(f'The "{item[0]}" character was found {item[1]} times')

    print()
    print("--- End Report ---")
