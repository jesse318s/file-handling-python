from glob import glob
import os
import re
import csv

def writeLine(outputFile, line):
    patterns = [r'<label>(.*?)<\/label>', r'<label2>(.*?)<\/label2>']

    for pattern in patterns:

        for match in re.finditer(pattern, line):
            csv.writer(outputFile).writerows([[match.group(1)]])

def main():
    with open('output.csv', 'w', newline='') as outputFile:
        inputFiles = glob(os.path.join(os.getcwd(), '*.txt'))

        for inputFilePath in inputFiles:
            with open(inputFilePath, 'r') as inputFile:
                
                for line in inputFile:
                    writeLine(outputFile, line)

main()