import argparse
import pandas as pd
from statsmodels.stats import multitest

parser= argparse.ArgumentParser(description='add column with p values adjusted for FDR')

parser.add_argument(
    '-i',
    '--input',
    type=str,
    help='Path for the input file'
)

parser.add_argument(
    '-p',
    '--pColumn',
    type=str,
    help='Name of the column with p-values'
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    help='Path for the output file'
)

parser.add_argument(
    '-I',
    '--column_index',
    type=int,
    help='Column index to insert adjusted p-values'
)

args=parser.parse_args()

def adjustFdr(df, pCol, output):
    data=pd.read_csv(df)
    pVals=data[pCol].tolist()
    U1, p=multitest.fdrcorrection(pVals, alpha=0.05, method='indep', is_sorted=False)
    column_index=args.column_index if args.column_index else len(data.columns)
    data.insert(loc=column_index, column="pVal_FDR", value=p, allow_duplicates=True)
    data.to_csv(output, index=False)

input=args.input
pCol=args.pColumn
output= args.output if args.output else './adjustedTable.csv'



if __name__=='__main__':
    adjustFdr(df=input, pCol=pCol, output=output)