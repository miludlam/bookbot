def main():
    book_path = "books/frankenstein.txt"
    result = print_book_report(book_path)
    return result 


def print_book_report(book):
    text = get_book_text(book)
    word_count = get_book_word_count(text)
    letter_dict = get_book_letter_count(text)
    letter_list_sorted = dict_to_sorted_list(letter_dict)

    # Header text
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document\n")
    for entry in letter_list_sorted:
        print(f"'{entry["letter"]}' was found {entry["count"]} times")

    # Footer text
    print("--- End report ---")
    return 0


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_book_word_count(text):
    return len(text.split())


def get_book_letter_count(text):
    letter_dict = {}
    for letter in text:
        letter = letter.lower()
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict


def dict_to_sorted_list(letter_dict):
    sorted_list = []
    for letter in letter_dict:
        sorted_list.append({"letter": letter, "count": letter_dict[letter]})
    sorted_list.sort(key=sort_by, reverse=True)
    return sorted_list


def sort_by(x):
    return x["count"]


main()