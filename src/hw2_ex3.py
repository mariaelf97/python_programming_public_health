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
        description=""" program to print all gene names that have MamC motif site"""
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
        if "CACGCAG" in r.seq:
            gene_list.append(r.id)

    with open("genes_with_mtases_motif.csv", "w") as file:
        wr = csv.writer(file)
        wr.writerow(gene_list)


if __name__ == "__main__":
    sys.exit(main())
