from collections import defaultdict

def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)

    print(f"Analysis of {path}")
    print(f"Word Count: {word_count}")
    print_character_count(character_count)
    print("End of Analysis.")

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_character_count(text):
    letter_dict = defaultdict(int)
    for char in text:
        letter_dict[char.lower()] += 1
    return letter_dict

def sort_character_count_list(dict):
    new_list = []
    for key in dict:
        if key.isalpha():
            temp_dict = {}
            temp_dict["letter"] = key
            temp_dict["count"] = dict[key]
            new_list.append(temp_dict)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

def print_character_count(dict):
    sorted_list = sort_character_count_list(dict)
    for mini_dict in sorted_list:
        print()
        print("The '" + str(mini_dict["letter"]) + "' character was found " + str(mini_dict["count"]) + " times.")

def sort_on(dict):
    return dict["count"]

if __name__ == '__main__':
    main()