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

args=parser.parse_args()


def adjustFdr(df, pCol, output):
    data=pd.read_csv(df)
    pVals=data[pCol].tolist()
    U1, p=multitest.fdrcorrection(pVals, alpha=0.05, method='indep', is_sorted=False)
    data.insert(loc=2, column="pVal_FDR", value=p, allow_duplicates=True)
    data.to_csv(output)

input=args.input
pCol=args.pColumn
output=args.output


if __name__=='__main__':
    adjustFdr(df=input, pCol=pCol, output=output)