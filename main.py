# step 1
def main():
    book_path = "books/frankenstein.txt"
    count = 0
    text = get_book_text(book_path)
    count = get_word_count(text)
    characters = get_character_count(text)
    print(f"--- Begin Report of {book_path} ---\n")
    print(f"{count} words found in document\n")
    sorted_characters = {k: characters[k] for k in sorted(characters)}
    for char in sorted_characters:
        if char.isalpha():
            print(f"the {char} character was found {sorted_characters[char]} times")
    print("--- End of Report ---\n")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    characters = {}
    for character in text:
        lower = character.lower()
        if lower in characters:
            characters[lower] += 1
        else:
            characters[lower] = 1
    return characters


if __name__ == '__main__':
    main()
