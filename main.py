import sys
from stats import get_num_words 
from stats import count_characters
from stats import sort_characters


def get_book_text(filepath):
    with open (filepath) as f:
        file_contents = f.read()
    
    return file_contents

def print_characters(sorted_list, filepath, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    get_text = get_book_text(filepath)
    word_count = get_num_words(get_text)
    character_count = count_characters(get_text)

    sorted_list = sort_characters(character_count)
    print_characters(sorted_list, filepath, word_count)
    


main()