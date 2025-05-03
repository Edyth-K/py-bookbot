from collections import defaultdict


def get_word_count(text):
    """
    Counts the number of words in a given text.
    
    Args:
        text (str): The text to be analyzed.
        
    Returns:
        int: The number of words in the text.
    """
    
    # Split the text into words and return the count
    return len(text.split())

def get_character_count(text):
    """
    Counts the occurrences of each character in a given text.
    
    Args:
        text (str): The text to be analyzed.
        
    Returns:
        dict: A dictionary with characters as keys and their counts as values.
    """
    
    # Initialize a dictionary to hold character counts
    letter_dict = defaultdict(int)
    
    # Count occurrences of each character in the text
    for char in text:
        letter_dict[char.lower()] += 1
    
    return letter_dict

def sort_on(dict):
    return dict["count"]

def sort_dict(dict):
    """
    Takes a dictionary of characters and their counts and returns a sorted list of dictionaries.

    Args:
        dict (dictionary): dictionary to be sorted

    Returns:
        new_list: The sorted list of dictionaries.
    """
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
    sorted_list = sort_dict(dict)
    for mini_dict in sorted_list:
        print(f"{str(mini_dict["letter"])}: {str(mini_dict["count"])}")
        #print("The '" + str(mini_dict["letter"]) + "' character was found " + str(mini_dict["count"]) + " times.")
