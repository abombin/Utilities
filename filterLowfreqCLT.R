
# supposed to install required packages if they are not present, needs testing
list.of.packages <- c('readr', 'optparse')
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages)

library(readr)
library(optparse)

# make options
options_list=list(
  make_option(c('-i', '--input'), type='character', default = NULL, help='path to input file'),
  make_option(c('-r', '--reference'), type='character', default = NULL, help='path to a reference table'),
  make_option(c('-o','--output'), type = 'character', default = 'filtered.csv', help='path to output file'),
  make_option(c('-f','--filter'), type = 'character', default = NULL, help= 'filter resullts to include relative variant position higher or equal to INT')
  
)

# parse options
opt_parser = OptionParser(option_list=options_list)
opt = parse_args(opt_parser)

# main function
refDf = read_delim(opt$reference, delim = "\t", escape_double = FALSE, trim_ws = TRUE)

resDf = read_delim(opt$input, delim = "\t", escape_double = FALSE, trim_ws = TRUE)

resDf$Ref_Al_RelPos<-NA
resDf$Var_Al_RelPos<-NA
for ( i in 1:nrow(resDf)){
  refAl<-resDf$`REF-NT`[i]
  varAl<-resDf$`VAR-NT`[i]
  # find real position of a variant nucleotide
  if (nchar(refAl) > nchar(varAl)) {
    alPos<- resDf$POSITION[i] +1
  } else {
    alPos<- resDf$POSITION[i]
  }
  # select reference position
  refSub<-refDf[(refDf$POS == alPos),]
  
  # find target relative position
  
  # handle deletion
  if (nchar(refAl) > nchar(varAl)) {
    varTargCol<- "INDEL1-POS"
    refTargCol<- paste0(varAl, '-POS') # wrong temporary method
    # handle insertion
  } else if (nchar(refAl) < nchar(varAl)) {
    varTargCol <- "INDEL1-POS"
    refTargCol<- paste0(refAl, '-POS') 
    # handle substitution
  } else if (nchar(refAl) == nchar(varAl)) {
    varTargCol<- paste0(varAl, '-POS')
    refTargCol<- paste0(refAl, '-POS')
  }
  # assign relative positions from reference
  resDf$Ref_Al_RelPos[i]<-as.numeric(refSub[1, c(refTargCol)])
  resDf$Var_Al_RelPos[i]<-as.numeric(refSub[1, c(varTargCol)])
  
}

# filter 
if (is.null(opt$filter) == T) {
  finalDf<- resDf
} else {
  filtNa<-resDf[!(is.na(resDf$Var_Al_RelPos)),]
  finalDf<- filtNa[(filtNa$Var_Al_RelPos >= opt$filter),]
}


write.csv(finalDf, file = opt$output, row.names = F)