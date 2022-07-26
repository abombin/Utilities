
# check if the required packages can be found
import sys
import subprocess
import pkg_resources

required = {'pandas', 'argparse'}
installed = {pkg.key for pkg in pkg_resources.working_set}
missing = required - installed

if missing:
    python = sys.executable
    subprocess.check_call([python, '-m', 'pip', 'install', *missing], stdout=subprocess.DEVNULL)
    

### main program

import pandas as pd
import argparse

parser=argparse.ArgumentParser(description='format metadata for Nextrain')

# add arguments

parser.add_argument(
  "-i",
  "--input_path",
  type=str,
  help="Path to the input file, required"
)

parser.add_argument(
  "-s",
  "--separator",
  type=str,
  nargs="?",
  default='\t',
  help="Columns separator, default = tab"
)

parser.add_argument(
  "-r",
  "--replace_with",
  type=str,
  nargs="?",
  default="NotMls",
  help="Replace NaN/empty cells with provided string, default = NotMls"
)

parser.add_argument(
  "-c",
  "--column",
  type=str,
  nargs="?",
  default="location",
  help="Column in which to fill NaN/'empy cells', default = location"
)

parser.add_argument(
  "-o",
  "--output_path",
  type=str,
  nargs="?",
  default="formatedTable.tsv",
  help="Path to the output file, default = formatedTable.tsv"
)

# parse arguments
args=parser.parse_args()

df=args.input_path
separator=args.separator
replacement=args.replace_with
column=args.column
output=args.output_path

# main function
def fromatData(dat, sep, rep, col, out):
  meta=pd.read_csv(filepath_or_buffer=dat, sep=sep)
  meta[col]=meta[col].str.replace(' ', rep)
  meta[[col]]=meta[[col]].fillna(rep)
  meta['date'] = pd.to_datetime(meta.date)
  meta['date'] = meta['date'].dt.strftime("%Y-%m-%d")
  meta[['date_submitted']]=meta[['date']]
  metaFilt=meta[meta['date'].notna()]
  metaFilt.to_csv(path_or_buf=out, sep='\t', index=False)
  
# Run the main function

if __name__=='__main__':
  fromatData(dat=df, sep=separator, rep=replacement, col=column, out=output)
  
