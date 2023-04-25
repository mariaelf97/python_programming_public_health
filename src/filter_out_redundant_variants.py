#!/usr/bin/env python3
import sys

import pandas as pd


def main():
    df = pd.read_csv(
        "/home/mahmedi/mnt/home_all/ahmadije/sample.tsv",
        sep="\t",
        index_col=False,
        names=[
            "[P1]",
            "[SUB]",
            "[SUB].1",
            "[P2]",
            "[BUFF]",
            "[DIST]",
            "[R]",
            "[Q]",
            "[FRM]",
            "[TAGS]",
            "project_id",
            "sample_id",
        ],
    )
    df = df.iloc[1:, :]
    df = df.drop_duplicates(subset=["[P1]", "[SUB]", "[SUB].1"])
    df.to_csv("duplicates_removed.tsv", sep="\t", index=False)


if __name__ == "__main__":
    sys.exit(main())
