from stats import get_word_count, get_character_count, print_character_count
# stats.py
import sys

def get_book_text(path_to_file):
    """
    Reads the contents of a file and returns it as a string.
    
    Args:
        path_to_file (str): The path to the file to be read.
        
    Returns:
        str: The contents of the file.
    """
    
    # Open the file in read mode and return its contents
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

if __name__ == '__main__':
    # Check if sys.argv has two entries
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Define the path to the book file
    path = sys.argv[1]    

    # Get the text from the book file
    text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print("--------- Character Count -------")
    print_character_count(get_character_count(text))
    print("============= END ===============")

    