import sys
from stats import word_counter, letter_counter, sort_letter_counter

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    book_text = get_book_text(sys.argv[1])
    book_letters = sort_letter_counter(letter_counter(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(word_counter(book_text))
    print("--------- Character Count -------")
    for entry in book_letters:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
