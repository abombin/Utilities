# improvement make an option for partial match to replace a substring in the column
import argparse

parser=argparse.ArgumentParser(description='replace a string in the files')

parser.add_argument(
    '-i',
    '--input',
    type=str,
    help='Path for the input file'
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    help='Path for the output file'
)

parser.add_argument(
    '-r',
    '--replace',
    type=str,
    help='replace string'
)

parser.add_argument(
    '-w',
    '--replace_with',
    help='string to replace with'
)

args=parser.parse_args()

def replaceWhole(input, output, replace, replace_with):
    inputFile=open(input, 'r')
    outputFile=open(output, 'w')
    for line in inputFile:
        outputLine=line.replace(replace, replace_with)
        outputFile.write(outputLine)
    inputFile.close()
    outputFile.close()

input=args.input
output=args.output if args.output else 'outputFile.txt'
replace=args.replace
replace_with=args.w

if __name__=='__main__':
    replaceWhole(input, output, replace, replace_with)
