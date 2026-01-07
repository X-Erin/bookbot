def word_counter(book_text):
    book_words = book_text.split()
    return f"Found {len(book_words)} total words"

def sort_num(letters):
    return letters["num"]

def letter_counter(book_text):
    book_letters = {}
    for ch in book_text:
        ch = ch.lower()
        if ch in book_letters:
            book_letters[ch] += 1
        else:
            book_letters[ch] = 1
    return book_letters

def sort_letter_counter(book_letters):
    sorted_letters = []
    for ch in book_letters:
        num = book_letters[ch]
        sorted_letters.append({"char": ch, "num": num})
    sorted_letters.sort(reverse=True, key=sort_num)
    return sorted_letters
