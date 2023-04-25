
#remove headers in .snps input
grep -v "/" covid19-snps.tsv | grep -v "NUCMER" > covid-snps-header-removed.tsv
# remove the blank line in .snps output
sed -i '/./,$!d' covid-snps-header-removed.tsv
#remove duplicated rows, to make the vcf conversion process faster
./remove-duplicates.py
#change .snps output to a vcf file
tools/all2vcf/src/mummer --snps covid-snps-duplicates-removed.tsv --reference /ocean/projects/bio230002p/afif/shared/input/final-project/reference-covid-19.fna --input-header > covid-snps.vcf
# download reference annotation gff file
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz
#convert reference annotation to gtf format
agat_convert_sp_gff2gtf.pl --gff GCF_009858895.2_ASM985889v3_genomic.gff.gz -o ref_genome.gtf
# remove headers in the gtf format file
grep -v "#" ref_genome.gtf > ref_genome_hashtag_removed.gtf
# sort the gtf file
sort -k1,1 -k4,4n -k5,5n -t$'\t' ref_genome_hashtag_removed.gtf | bgzip -c > ref_genome_hashtag_removed.gtf.gz
# index the file
tabix -p gff  ref_genome_hashtag_removed.gtf.gz
# zip the reference genome file
bgzip reference-covid-19.fna
# annotate variants
vep -i sample_vcf.vcf --gtf ref_genome_hashtag_removed.gtf.gz --fasta reference-covid-19.fna.gz
