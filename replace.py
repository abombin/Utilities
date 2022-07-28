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

replace_with=args.replace_with
input=args.input
output=args.output if args.output else 'outputFile.txt'
replace=args.replace


def replaceWhole(input, output, replace, replace_with):
    inputFile=open(input, 'r')
    outputFile=open(output, 'w')
    for line in inputFile:
        if replace_with==r'\t':
            outArg='\t'
        else:
            outArg=replace_with
        if replace==r'\t':
            inArg='\t'
        else:
            inArg=replace
        outputLine=line.replace(inArg, outArg)
        outputFile.write(outputLine)
    inputFile.close()
    outputFile.close()



if __name__=='__main__':
    replaceWhole(input, output, replace, replace_with)
