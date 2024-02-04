def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    def count_words(book_string):
        words = book_string.split()
        return len(words)
    count_words(file_contents)
main()
