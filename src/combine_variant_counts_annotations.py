#!/usr/bin/env python3
import sys

import pandas as pd


def get_sequence(reference):
    """Code credit Cassidy Robinhold
    https://gitlab.com/LPCDRP/illumina-blindspots.pub
    input = fasta file
    This function is used to read the genome file and remove useless row in the beginning of the file
    that has a ">" with the length of the genome
    """
    seq_str = ""
    with open(reference) as f:
        for line in f:
            if not line.startswith(">"):
                line = line.strip()
                seq_str += line
    return seq_str


def translate(seq):
    """code taken from https://www.geeksforgeeks.org/dna-protein-python-3/"""
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W',
    }
    protein = ""
    if len(seq) % 3 == 0:
        for i in range(0, len(seq), 3):
            codon = seq[i:i + 3]
            protein += table[codon]
    return protein


def main():
    df = pd.read_csv(
        "/Users/maryam/Downloads/sample.tsv", sep="\t", index_col=False
    )
    variant_count = (
        df.groupby(["[P1]", "[SUB]", "[SUB].1"]).size().to_frame().reset_index()
    )
    variant_count = variant_count.rename(
        columns={"[P1]": "position", "[SUB]": "ref", "[SUB].1": "alt", 0: "samples"}
    )
    variant_count = variant_count.sort_values("samples", ascending=False)
    annotation = pd.read_csv(
        "/Users/maryam/Downloads/variant_effect_output_header_removed.txt",
        sep="\t",
        index_col=False,
    )
    # change location to be able to merge with the main variant counts file
    annotation["Location"] = annotation["Location"].str.split(":").str[-1]
    annotation["Location"] = annotation["Location"].astype(str)
    variant_count["position"] = variant_count["position"].astype(str)
    joined_frames = pd.merge(
        annotation, variant_count, left_on="Location", right_on="position"
    )
    joined_frames = joined_frames.sort_values("samples", ascending=False)
    fasta_file = get_sequence("/Users/maryam/Downloads/reference-covid-19.fna")
    gb_file = pd.read_csv("/Users/maryam/Downloads/ref_genome_hashtag_removed.gtf",sep = "\t")
    joined_frames_subset = joined_frames[["Feature", "Consequence", ""]]
    print(joined_frames_subset)


if __name__ == "__main__":
    sys.exit(main())
