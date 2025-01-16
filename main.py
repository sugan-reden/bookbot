def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book_path(book_path)
    word_count = count_words(file_contents)
    print(file_contents)
    print(f"Word count: {word_count}")

def count_words(message):
    words = message.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_book_path(path):
    with open(path) as f:
        return f.read()

main()
# print("hello world")
