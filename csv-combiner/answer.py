'''
This program is to combine the csv files into a larger csv file with an additional column filename
Challenge link: https://github.com/AgencyPMG/ProgrammingChallenges/tree/master/csv-combiner
'''

import sys
import os
import pandas as pd


class CSVCombiner:

    @staticmethod
    def validate_filenames(argv):
        '''
        check if there are path input and if all the files exist & are non-empty
        ---------
        Return: if all the arguments are valid

        '''
        if len(argv) <= 1:
            print("Please enter input as the following format \n" +
                  "python3 ./answer.py ./fixtures/accessories.csv ./fixtures/clothing.csv > combined.csv")
            return False

        files = argv[1:]
        
        ret = True
        for file in files:
            if not os.path.exists(file):
                print("File" + file + "do not exist")
                ret = False
            if os.stat(file).st_size == 0:
                print("File" + file + "is empty")
                ret = False
        return ret

    def combine_files(self, argv, chunksize=10**5):
        '''
        combine all rows in files and print to a file
        -----------
        Return:
        '''
        contents = []
        if self.validate_filenames(argv):
            files = argv[1:]
            for file in files:
                for content in pd.read_csv(file, chunksize=chunksize):
                    filename = os.path.basename(file)
                    content["filename"] = filename
                    contents.append(content)
            header = True
            
            for content in contents:
                print(content.to_csv(index=False,header=header, line_terminator='\n', chunksize=chunksize), end='')
                header = False
        else:
            return 


def main():
    combiner = CSVCombiner()
    combiner.combine_files(sys.argv)

if __name__ == '__main__':
    main()






