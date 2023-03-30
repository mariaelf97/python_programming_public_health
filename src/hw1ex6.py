#!/usr/bin/env python3
import argparse
import sys


def read_file(file_path):
    """function to read a text file and return unique words alphabetically sorted
    input = text file, space delimited
    output = alphabetically sorted unique words in list format"""
    with open(file_path, "r") as file:
        lines = file.readlines()
        words = []
        for line in lines:
            line = line.strip("\n")
            line_list = line.split(" ")
            words.append(line_list)
            flat_list = []
            for sublist in words:
                for item in sublist:
                    if item not in flat_list:
                        flat_list.append(item)
    flat_list.sort()
    return flat_list


def write_file(list_to_write, output_name):
    """function to write list to text format
    input : a list
    output : text file one line per unique text"""

    with open(output_name + ".txt", "w") as file:
        for item in list_to_write:
            file.write(item + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="""input a text file and get a
     sorted and alphabetically arranged output as a text file """
    )
    parser.add_argument(
        "-i",
        "--input",
        required=False,
        help="input file in text format, space delimited",
        default="romeo.txt",
    )
    parser.add_argument(
        "-o",
        "--output",
        required=False,
        help="define output file name",
        default="romeo-unique-words",
    )
    args = parser.parse_args()
    input_file = args.input

    file_to_list = read_file(input_file)
    write_file(file_to_list, args.output)


if __name__ == "__main__":
    sys.exit(main())
