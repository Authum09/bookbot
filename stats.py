def get_num_words(book_text):
    list_of_words = book_text.split()
    num_of_words = len(list_of_words)
    return num_of_words

def count_characters(book_text):
    characters = {}
    for c in book_text.lower():
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1

    return characters

def sort_on(items):
    return items["num"]

def sort_characters(characters):
    list_of_dict = []

    for char, count in characters.items():
        if char.isalpha():
            list_of_dict.append({"char": char, "num": count})
    
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict





