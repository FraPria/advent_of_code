library(GenomicRanges)

setwd('~/Desktop/coding_shit/advent_of_code/2023/day_05/')
df = read.delim2('all.csv', sep = ',', header=T)[,2:7]
seeds = read.delim2('seeds.csv', sep = ',', header=T)[,2:3]


seeds_gr = GRanges(seqnames='1', ranges=IRanges(seeds$start, seeds$end))
# hits = findOverlaps(df_gr, seeds_gr)
# x = df[queryHits(hits),]
# y = seeds[subjectHits(hits),]
for (s in c('seed','soil','fertilizer','water','light','temperature','humidity')) {
  tmp_df = subset(df, source_label==s)
  df_gr = GRanges(seqnames='1', ranges=IRanges(tmp_df$source_start, tmp_df$source_end))
  
  # hits = findOverlaps(df_gr, seeds_gr)
  # queryHits(hits)
  common = intersect(df_gr, seeds_gr)
  hits = findOverlaps(df_gr, common)
  df[queryHits(hits),]
  not_found = setdiff(seeds_gr, common)
}
