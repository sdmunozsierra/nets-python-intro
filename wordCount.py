"""Counts number of words in a file, and orders them."""
import os
import re
import sys
from collections import Counter


def read_file(filename):
    """Reads a file name into a list line by line."""
    with open(filename) as f:
        content = f.readlines()
        content = [x.strip() for x in content]  # Remove whitespace
        return content
    return None  # File not found


def clean_file_contents(content):
    """Cleans unwanted content and creates a list of words out of it."""
    words = []
    for line in content:
        matches = re.sub(r"-", ' ', line)  # Special case replace "-"
        matches = re.sub(r"'", ' ', matches)  # Special case replace "'"
        matches = re.sub(r'[^\w\s]', '', matches)  # Remove everything else
        lines_words = matches.split(" ")  # Split each word
        words = words + [x.lower() for x in lines_words if x]  # update list
    # words.sort()
    return words


def count_ocurrences(words):
    """Creates a dictionary with the ocurrences.
    :returns: tuple with two lists one containing words and the other indices.
    """
    ocurrences = Counter(words)
    ocurrences = Counter(ocurrences)
    words = sorted(ocurrences)
    indices = [ocurrences[value] for value in sorted(ocurrences)]
    return words, indices


def create_file(word_list, ocurrence_list, filename=None):
    """Creates a file with each word and corresponding ocurrence."""
    if not filename:
        filename = "output.txt"
    with open(filename, 'w') as f:
        for idx, _val in enumerate(word_list):
            f.write("{} {}\n".format(word_list[idx], ocurrence_list[idx]))
    return True


def main():
    """Main function."""
    # Get arguments from sys
    outputFname = sys.argv[2]
    inputFname = sys.argv[1]
    filename = "{}/{}".format(os.path.dirname(os.path.abspath(__file__)),
                              inputFname)
    content = read_file(filename)
    words = clean_file_contents(content)
    words, ocurrences = count_ocurrences(words)
    create_file(words, ocurrences, outputFname)


# Run main
main()
