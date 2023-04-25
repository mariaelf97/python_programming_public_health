#!/usr/bin/env python3
import sys

import pandas as pd


def main():
    df = pd.read_csv(
        "/home/mahmedi/mnt/home_all/ahmadije/sample.tsv", sep="\t", index_col=False
    )
    variant_count = (
        df.groupby(["[P1]", "[SUB]", "[SUB].1"]).size().to_frame().reset_index()
    )
    variant_count = variant_count.rename(
        columns={"[P1]": "position", "[SUB]": "ref", "[SUB].1": "alt", 0: "samples"}
    )
    variant_count = variant_count.sort_values("samples", ascending=False)
    variant_count.to_csv("variant-counts.csv")


if __name__ == "__main__":
    sys.exit(main())
