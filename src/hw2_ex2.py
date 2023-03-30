#!/usr/bin/env python3
import argparse
import csv
import sys

from Bio import SeqIO


def read_fasta_file(path_to_file):
    fasta_file = SeqIO.parse(path_to_file, "fasta")
    return fasta_file


def main():
    parser = argparse.ArgumentParser(
        description=""" program to print all gene names longer than
     2000 nucleotides in a multi-fasta file"""
    )
    parser.add_argument(
        "-i", "--input", required=True, help="input file in multi fasta format"
    )
    args = parser.parse_args()
    input_file = args.input
    fasta_file = read_fasta_file(input_file)
    # print all gene names
    gene_list = []
    for r in fasta_file:
        if len(r.seq) > 2000:
            gene_list.append(r.id)
    with open("genes_greater_than_2000_bps.csv", "w") as file:
        wr = csv.writer(file)
        wr.writerow(gene_list)


if __name__ == "__main__":
    sys.exit(main())
