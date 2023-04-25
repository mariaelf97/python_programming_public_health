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
    annotation = pd.read_csv(
        "/home/mahmedi/mnt/home_all/ahmadije/variant_effect_output_header_removed.txt",
        sep="\t",
        index_col=False,
    )
    # change location to be able to merge with the main variant counts file
    annotation["Location"] = annotation["Location"].str.split(":").str[-1]
    variant_count.to_csv("variant-counts.csv")
    annotation["Location"] = annotation["Location"].astype(str)
    variant_count["position"] = variant_count["position"].astype(str)
    joined_frames = pd.merge(
        annotation, variant_count, left_on="Location", right_on="position"
    )
    joined_frames = joined_frames.sort_values("samples", ascending=False)
    joined_frames_subset = joined_frames[["Feature", "Consequence", ""]]
    print(joined_frames_subset)


if __name__ == "__main__":
    sys.exit(main())
