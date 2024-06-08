def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_character_counts = convert_character_dict_to_sorted_list(num_characters)

    # Generate and print the report
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in sorted_character_counts:
        print(f"The '{item['character']}' character was found {item['count']} times")
    print("--- End report ---")


def get_num_words(text):
    """
    This function takes a string and returns the number of words in the string.
    """
    words = text.split()
    return len(words)


def get_book_text(path):
    """
    This function reads the text from the book
    """
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    """
    This function takes a string and returns a dictionary with the number of times
    each character appears in the string, converting all characters to lowercase.
    """
    char_count = {}

    # Convert text to lowercase
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

    return char_count

def convert_character_dict_to_sorted_list(char_count):
    """
    This function takes a dictionary of character counts and converts it to a list
    of dictionaries, then sorts the list by the number of occurrences.
    """
    # Convert the dictionary to a list of dictionaries
    char_list = [{"character": char, "count": count} for char, count in char_count.items()]

    # Sort the list by the number of occurrences (count) in descending order
    sorted_char_list = sorted(char_list, key=lambda x: x["count"], reverse=True)

    return sorted_char_list
    
main()
