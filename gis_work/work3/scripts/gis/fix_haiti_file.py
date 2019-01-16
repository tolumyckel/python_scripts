#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#-------------------------------------------------------------------------------

import csv

in_csv = None
out_csv = None
admin_code_column_index = 0

def process_file():
    """in_csv = file where a column contains a admin_code that needs fixing.
                That is, the 5th character in admin_code needs to be removed.
       out_csv = file with same contents as in_csv with fixed admin_code
       admin_code_column_index = 0-based index of column containing the
                                 admin_code
    """
    with open('Haiti_Admin_Names.csv') as in_csv, \
    open('haiti_admin_names_fixed.csv', 'w') as out_csv:
        reader = csv.reader(in_csv)
        count = 0
        writer = csv.writer(out_csv)
        for read in reader:
            if count == 0:
                writer.writerow(read)
            else:
                #print list(read[0]).remove()
                read[0] = _fix_code(read[0])
                writer.writerow(read)
            count +=1




def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""

    fix = admin_code[:4]+admin_code[5:]
    return fix

def main():
    process_file()

if __name__ == '__main__':
    main()

























