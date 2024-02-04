def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()

    def count_words(book_string):
        words = book_string.split()
        return len(words)
    
    def count_letters(book_string):
        char_dict = {}
        for char in book_string.lower():
            if (char in char_dict) == False:
                char_dict[char] = 1
            else:
                char_dict[char] += 1
        return char_dict
    
    def sort_assist(dict):
        for key in dict:
            return dict[key]

    def generate_findings(book_string):
        num_words = count_words(book_string)
        char_dict = count_letters(book_string)
        letter_dict = {}
        for key in char_dict:
            if key.isalpha():
                letter_dict[key] = char_dict[key]
        #This is one of the sickest things I have learned. LIST COMPREHENSION.
        letter_list = [{k:v} for k, v in letter_dict.items()]
        """
        The Above code equates to:
        letter_list = []
        for key in letter_dict:
            letter_list.append({key,letter_dict[key]})
        """
        letter_list.sort(reverse=True, key=sort_assist)
        print(f"Generated Report for {book}:")
        print(f"{num_words} words were found in the document \n")
        for dict in letter_list:
            for key in dict:
                print(f"The letter {key} was found {dict[key]} times.")
        print("Report Finished.")
        
        
    generate_findings(file_contents)
main()
