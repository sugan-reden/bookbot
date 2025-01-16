def count_words(message):
    words = message.split()
    count = 0
    for word in words:
        count += 1
    return count

def get_book_path(path):
    with open(path) as f:
        return f.read()

# print("hello world")
