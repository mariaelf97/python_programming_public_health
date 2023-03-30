#!/usr/bin/env python3
import argparse
import sys

from Bio import SeqIO


def read_fasta_file(path_to_file):
    fasta_file = SeqIO.parse(path_to_file, "fasta")
    return fasta_file


def main():
    parser = argparse.ArgumentParser(
        description=""" program to print all gene names in a multi-fasta file"""
    )
    parser.add_argument(
        "-i", "--input", required=True, help="input file in multi fasta format"
    )
    args = parser.parse_args()
    input_file = args.input
    fasta_file = read_fasta_file(input_file)
    # print all gene names
    for r in fasta_file:
        print(r.id)


if __name__ == "__main__":
    sys.exit(main())
