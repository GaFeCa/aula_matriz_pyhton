"""Modulo csv para manejo de archivos"""

import csv 


def lines_count(path):
    with open(path, 'r') as csvfile:
        reader_obj = csv.reader (csvfile, delimiter='|')

        total_lines = 0

        for line in reader_obj:
            print(line)
            total_lines == 1

    return total_lines

print(__name__)

if __name__ =='__main__':
    print('Bandera de main')
    print(lines_count('para_manejo_files.txt'))
    