library(data.table)
library(tidyverse)

df = fread("/home/mahmedi/mnt/home_all/ahmadije/OUT.Assemblytics_structural_variants.bed")

df %>% ggplot(aes(x=ref_start,y=ref_stop))+geom_point(aes(size=size, color=type)) +theme_classic()
df %>% ggplot(aes(x=size))+geom_histogram(aes(fill=type))+theme_classic()
