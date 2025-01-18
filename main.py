def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_path(book_path)

    word_count = count_words(file_contents)
    # print(f"Word count: {word_count}")

    lowered_content = file_contents.lower()

    character_counts = check_seen_characters(lowered_content)
    # print(character_counts)
    # print(type(character_counts))

    # print(file_contents)
    # print(lowered_content)
    # print("The above content should be all lowercase.")

    # Making a nice report
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words were found in the document")
    print("\n")
    for i in character_counts:
        print(f"The '{i}' character was found {character_counts[i]} times")
    print("--- End report ---")

def check_seen_characters(lowered_text):
    seen_characters = {}
    # count = 1
    for c in lowered_text:
        if c not in seen_characters and c.isalpha():
            seen_characters[c] = 1
        elif c in seen_characters and c.isalpha():
            seen_characters[c] += 1
    # print(seen_characters)
    return seen_characters

def count_words(message):
    words = message.split()
    return len(words)

def get_book_path(path):
    with open(path) as f:
        return f.read()

main()
# print("hello world")
