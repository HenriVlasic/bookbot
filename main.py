def main():
    book_path = "./books/frankenstein.txt"
    book = get_book(book_path)
    num_words = get_num_words(book)
    num_letters = get_num_letters(book)
    create_report(book_path, num_words, num_letters)

def get_num_words(book):
    words = book.split()
    return len(words)

def get_book(path):
    with open(path) as f:
        return f.read()

def get_num_letters(book):
    letters_dict = {}
    for letter in book:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict

def create_report(book_path, num_words, num_letters):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print("")
    for letter in num_letters:
        print(f"The '{letter}' character was found {num_letters[letter]} times")
    print("--- End report ---")

main()
