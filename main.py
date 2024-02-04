def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    def count_words(book_string):
        words = book_string.split()
        return len(words)
    def count_letters(book_string):
        letter_dict = {}
        for char in book_string.lower():
            if (char in letter_dict) == False:
                letter_dict[char] = 1
            else:
                letter_dict[char] += 1
        return letter_dict

    count_words(file_contents)
    count_letters(file_contents)
main()
