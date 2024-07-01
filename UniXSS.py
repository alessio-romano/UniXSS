import unicodedata
import urllib.parse
import sys
import argparse
from tabulate import tabulate

def unicode_mapping():
    character_mapping = {
        # Lowercase Letters
        "a": "%c2%aa",
        "b": "%e1%b5%87",
        "c": "%e1%b6%9c",
        "d": "%e1%b5%88",
        "e": "%e1%b5%89",
        "f": "%e1%b6%a0",
        "g": "%e1%b5%8d",
        "h": "%ca%b0",
        "i": "%e1%b5%a2",
        "j": "%ca%b2",
        "k": "%e1%b5%8f",
        "l": "%cb%a1",
        "m": "%e1%b5%90",
        "n": "%e2%81%bf",
        "o": "%c2%ba",
        "p": "%e1%b5%96",
        "q": "%e2%93%a0",
        "r": "%ca%b3",
        "s": "%cb%a2",
        "t": "%e1%b5%97",
        "v": "%e1%b5%9b",
        "w": "%e1%b5%82",
        "x": "%cb%a3",
        "y": "%ca%b8",
        "z": "%e1%b6%bb",

        # Uppercase Letters  
        "A": "%e1%b4%ac",
        "B": "%e1%b4%ae",
        "C": "%e2%84%82",
        "D": "%e1%b4%b0",
        "E": "%e1%b4%b1",
        "F": "%e2%84%b1",
        "G": "%e1%b4%b3",
        "H": "%e1%b4%b4",
        "I": "%e1%b4%b5",
        "J": "%e1%b4%b6",
        "K": "%e1%b4%b7",
        "L": "%e1%b4%b8",
        "M": "%e1%b4%b9",
        "N": "%e1%b4%ba",
        "O": "%e1%b4%bc",
        "P": "%e1%b4%be",
        "Q": "%e2%84%9a",
        "R": "%e1%b4%bf",
        "S": "%e2%93%88",
        "T": "%e1%b5%80",
        "U": "%e1%b5%81",
        "V": "%e2%85%a4",
        "W": "%e1%b5%82",
        "X": "%e2%85%a9",
        "Y": "%e2%93%8e",
        "Z": "%e2%84%a4",

        # Numbers
        '0': "%ef%bc%90",
        '1': "%ef%bc%91",
        '2': "%ef%bc%92",
        '3': "%ef%bc%93",
        '4': "%ef%bc%94",
        '5': "%ef%bc%95",
        '6': "%ef%bc%96",
        '7': "%ef%bc%97",
        '8': "%ef%bc%98",
        '9': "%ef%bc%99"
    }
    return character_mapping

def special_characters_mapping():
    return {
        # Special Characters
        "<": "%ef%b9%a4",
        ">": "%ef%b9%a5",
        "'": "%ef%bc%87",
        '"': "%ef%bc%82",
        "`": "%ef%bd%80",
        "-": "%ef%b9%a3",
        "+": "%ef%b9%a2",
        "=": "%e2%81%bc",
        ":": "%ef%bc%9a",
        ".": "%ef%b9%92",
        ",": "%ef%b9%90",
        ";": "%ef%bc%9b",
        "{": "%ef%b9%9b",
        "}": "%ef%b9%9c",
        "(": "%ef%bc%88",
        ")": "%ef%bc%89",
        "[": "%ef%bc%bb",
        "]": "%ef%bc%bd",
        "?": "%ef%b9%96",
        "!": "%ef%b9%97",
        "*": "%ef%b9%a1",
        "%": "%ef%b9%aa",
        "/": "%ef%bc%8f",
        "#": "%ef%b9%9f",
        "$": "%ef%b9%a9",
        "\\": "%ef%b9%a8"
    }

def transform_input(input_text, only_special=False):
    if only_special:
        character_mapping = special_characters_mapping()
    else:
        character_mapping = {**unicode_mapping(), **special_characters_mapping()}

    transformed_text = []
    for char in input_text:
        if char in character_mapping:
            transformed_text.append(character_mapping[char])
        else:
            transformed_text.append(urllib.parse.quote(char))

    return "".join(transformed_text)

def print_ascii_art():
    ascii_art = """
██╗   ██╗███╗   ██╗██╗██╗  ██╗███████╗███████╗   ██████╗ ██╗   ██╗
██║   ██║████╗  ██║██║╚██╗██╔╝██╔════╝██╔════╝   ██╔══██╗╚██╗ ██╔╝
██║   ██║██╔██╗ ██║██║ ╚███╔╝ ███████╗███████╗   ██████╔╝ ╚████╔╝ 
██║   ██║██║╚██╗██║██║ ██╔██╗ ╚════██║╚════██║   ██╔═══╝   ╚██╔╝  
╚██████╔╝██║ ╚████║██║██╔╝ ██╗███████║███████║██╗██║        ██║   
 ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚══════╝╚══════╝╚═╝╚═╝╚═╝        ╚═╝   

github.com/alessio-romano/unixss
notes.sfoffo.com
-----------------------------------
    """
    print(ascii_art)

def print_character_table(input_text=None, only_special=False):
    if only_special:
        character_mapping = special_characters_mapping()
    else:
        character_mapping = {**unicode_mapping(), **special_characters_mapping()}

    if input_text:
        # Filter the character mapping to include only characters in the input_text
        filtered_mapping = {char: encoded for char, encoded in character_mapping.items() if char in input_text}
    else:
        filtered_mapping = character_mapping

    rows = []
    for char, encoded in filtered_mapping.items():
        rows.append([char, encoded])

    print(tabulate(rows, headers=["Character", "Encoded Value"], tablefmt="grid"))

if __name__ == "__main__":
    print_ascii_art()

    parser = argparse.ArgumentParser(description='Transform input text using Unicode mappings.')
    parser.add_argument('input_text', nargs='?', help='The text to be transformed')
    parser.add_argument('--table', action='store_true', help='Print the character mapping table')
    parser.add_argument('--only-special', action='store_true', help='Only process special characters')

    args = parser.parse_args()

    if args.table:
        print_character_table(args.input_text if args.input_text else None, only_special=args.only_special)
        if args.input_text:
            transformed_output = transform_input(args.input_text, only_special=args.only_special)
            print("\nTransformed output:")
            print(transformed_output)
        sys.exit(0)

    if not args.input_text:
        parser.print_help()
        sys.exit(1)

    transformed_output = transform_input(args.input_text, only_special=args.only_special)
    print("\nTransformed output:")
    print(transformed_output)
