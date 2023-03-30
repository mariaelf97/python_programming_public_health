#!/usr/bin/env python3
import argparse
import sys

import pandas as pd


def get_vcf_names(vcf_path):
    """function to read the merged vcf file
    code credit: https://www.biostars.org/p/416324/ """
    with open(vcf_path, "rt") as ifile:
        for line in ifile:
            if line.startswith("#CHROM"):
                vcf_names = [x for x in line.split('\t')]
                break
    ifile.close()
    return vcf_names


def main():
    parser = argparse.ArgumentParser(description="""program to get sensitivity, specificity, and PPV""")
    parser.add_argument(
        "-vcf", "--variant", required=True, help="variant file in vcf format"
    )
    parser.add_argument(
        "-i", "--dst", required=True, help="DST file"
    )
    args = parser.parse_args()
    vcf_files = args.variant
    dst_file = args.dst

    names = get_vcf_names(vcf_files)
    vcf = pd.read_csv(vcf_files, comment='#',
                      chunksize=59, delim_whitespace=True, header= None, names=names)
    df = vcf.get_chunk(59)
    df = df.replace('./.:.:.:.:.:.:.:.:.:.:.:.:.:.', None)
    df = df.rename(columns={'C00018804\n': 'C00018804'})
    df =df.set_index("POS")
    # read DST_df dataset
    DST_df = pd.read_csv(dst_file, sep="\t", names=["isolate","DST"])
    DST_S_isolates = DST_df[DST_df['DST'] == "S"]
    DST_R_isolates = DST_df[DST_df['DST'] == "R"]
    sus_df = df[DST_S_isolates["isolate"]]
    res_df = df[DST_R_isolates["isolate"]]
    sus_df["sus_isolates_count"] = sus_df.count(axis=1)
    res_df["res_isolates_count"] = res_df.count(axis=1)
    result_df = pd.merge(sus_df["sus_isolates_count"],res_df["res_isolates_count"],left_index=True, right_index=True)
    result_df["sus_no_variant"] = len(DST_S_isolates) - result_df["sus_isolates_count"]
    result_df["res_no_variant"] = len(DST_R_isolates) - result_df["res_isolates_count"]
    result_df["sensitivity"] = result_df["res_isolates_count"] / \
                               (result_df["res_isolates_count"] + result_df["sus_no_variant"])
    result_df["specificity"] = result_df["sus_no_variant"] / \
                               (result_df["sus_no_variant"] + result_df["sus_isolates_count"])
    result_df["PPV"] = result_df["res_isolates_count"] /\
                       (result_df["res_isolates_count"] + result_df["sus_isolates_count"])
    result_df = result_df.sort_values("PPV", ascending=False)
    result_df.to_csv("amk-gwa-variants.csv")


if __name__ == "__main__":
    sys.exit(main())
