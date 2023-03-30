#!/usr/bin/env python3
import argparse
import csv
import re
import sys

from Bio import SeqIO


def read_gb_file(path_to_file):
    gb_file = SeqIO.parse(path_to_file, "genbank")
    return gb_file


def find_regulatory_regions(record):
    gene_list = []
    for r in record.features:
        if r.type == "CDS" and r.location.strand == 1:
            if r.qualifiers["locus_tag"][0] == "Rv0001":
                header = "Rv0001"
                promoter_start = 4410929 - 300
                promoter_end = 4410929
                promoter_seq = str(record.seq[promoter_start:promoter_end])
                if re.findall("TG[AGCT]{3}G[AGCT]{2}G", promoter_seq):
                    gene_list.append(header)
            else:
                header = r.qualifiers["locus_tag"][0]
                promoter_start = r.location.start - 300
                promoter_end = r.location.start
                promoter_seq = str(record.seq[promoter_start:promoter_end])
                if re.findall("TG[AGCT]{3}G[AGCT]{2}G", promoter_seq):
                    gene_list.append(header)
        elif r.type == "CDS" and r.location.strand == -1:
            header = r.qualifiers["locus_tag"][0]
            promoter_start = r.location.end
            promoter_end = r.location.end + 300
            promoter_seq = str(
                record.seq[promoter_start:promoter_end].reverse_complement()
            )
            if re.findall("TG[AGCT]{3}G[AGCT]{2}G", promoter_seq):
                gene_list.append(header)
    return gene_list


def main():
    parser = argparse.ArgumentParser(
        description=""" program to extract the regulatory sequence of each gene,
                     defined as the first 200 bp upstream of the start codon of the gene"""
    )
    parser.add_argument(
        "-i", "--input", required=True, help="input file in multi gb format"
    )
    args = parser.parse_args()
    input_file = args.input
    gb_file = read_gb_file(input_file)

    all_records = []
    for r in gb_file:
        records = find_regulatory_regions(r)
        all_records.append(records)
    with open("H37Rv_sigmafactor_binding_genes.csv", "w") as file:
        wr = csv.writer(file)
        wr.writerow(all_records)


if __name__ == "__main__":
    sys.exit(main())

