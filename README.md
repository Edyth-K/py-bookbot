# BookBot

*BookBot is a guided project from [Boot.dev](https://www.boot.dev).*

BookBot is a simple Python script that processes .txt files and outputs a total word count and a sorted breakdown of alphabetic character frequencies.

## Features
- Count total words in a text file
- Count and sort characters, case-insensitive
- Output cleanly formatted stats to the console

## Project Structure
```
bookbot/
├── main.py         # Entry point: handles file I/O and output
├── stats.py        # Core logic for counting words and characters
```

## Usage
1. Save your book or text content in a ```.txt``` file.
2. Run the script from the command line:
```
python3 main.py <path_to_text_file>
```
**Example:**
```
python3 main.py books/frankenstein.txt
```

## How It Works
- ```main.py```: Reads the file, calls utility functions, and prints results.
- ```stats.py```:
  - ```get_word_count(text)```: Splits the text by whitespace to count words.
  - ```get_character_count(text)```: Tallies character occurrences (case-insensitive).
  - ```print_character_count(dict)```: Sorts alphabetic characters by frequency and prints results.

## Example Output
```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 74587 total words
--------- Character Count -------
e: 9053
t: 6710
a: 5740
...
============= END ===============
```
