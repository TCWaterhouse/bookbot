def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    sorted_char = get_sorted_list(char_count)
    get_report(book_path, word_count, sorted_char)

def get_book_text(path):
    with open(path) as p:
        return p.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    chars = {}
    for c in text:
        l = c.lower()
        if l in chars:
            chars[l] += 1
        else:
            chars[l] = 1
    return chars  

def sort_on(dict):
    return dict["num"]

def get_sorted_list(char_count):
    sorted_char = []
    for c in char_count:
        if c.isalpha():
            sorted_char.append({"char" : c, "num" : char_count[c]})
        else:
            pass
    sorted_char.sort(reverse=True, key=sort_on)
    return sorted_char

def get_report(book_path, word_count, sorted_char):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    
    for l in sorted_char:
        print(f"The '{l["char"]}' character was found {l["num"]} times")
   
    print("--- End report ---")

main()