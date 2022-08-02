library(optparse)
library(ape)
# make options
options_list=list(
  make_option(c('-i', '--input'), type='character', default = NULL, help='path to input file'),
  make_option(c('-t', '--taxa'), type='character', default = NULL, help='outgroup to root at'),
  make_option(c('-o','--output'), type = 'character', default = 'rooted.tree', help='path to output file')
)

# parse options
opt_parser = OptionParser(option_list=options_list)
opt = parse_args(opt_parser)

# main function
tree<-ape::read.tree(opt$input)

rootTree<-ape::root(tree, outgroup=opt$taxa, resolve.root = TRUE)

ape::write.tree(phy=rootTree, file=opt$output)