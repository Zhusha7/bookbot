def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_character_counts(text)
    print(f"There are {num_words} of words in this book")
    print("List of character counts:")
    for i in char_dict:
        print(f"{i} : {char_dict[i]}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_counts(text):
    chars = {}
    for i in text.lower():
        if i in chars and i.isalpha():
            chars[i] += 1
        elif i.isalpha():
            chars[i] = 1
    return dict(sorted(chars.items(), reverse=True, key=sort_on))

def sort_on(tuple):
    return tuple[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()