#-------------------------------------------------------------------------------
# Name:        fix_haiti_file.py
# Purpose:     Fix admin_codes in Haiti data files.
#
# Author:      David Viljoen
#
# Created:     02/10/2018
#-------------------------------------------------------------------------------

import csv,sys,os

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
    if len(sys.argv) == 3:
        path = os.path.dirname(os.path.abspath(__file__))
        foldername = os.path.join(path,sys.argv[1])
        global in_csv
        global out_csv
        if os.path.exists(foldername):
            try:
                with open(sys.argv[1]) as in_csv, \
                open(sys.argv[2], 'w') as out_csv:

                    reader = csv.reader(in_csv)
                    count = 0
                    writer = csv.writer(out_csv)
                    for read in reader:
                        if count == 0:
                            writer.writerow(read)
                        else:
                            #print list(read[0]).remove()
                            read[admin_code_column_index] = _fix_code(read[admin_code_column_index])
                            writer.writerow(read)

                        count +=1
            except:
                print "Invalid path {}".format(foldername)
        else:
            print "{} does not exist in the file path: {}".format(sys.argv[1],path)
    else:
        print "Usage: fix_haiti_file_with_args.py in_file fixed_file"




def _fix_code(admin_code):
    """Returns code with 5th character removed.  For example,
       given HT12345-01, return "HT1245-01"""

    fix = admin_code[:4]+admin_code[5:]
    return fix

def main():
    process_file()
    #print len(sys.argv)
    #print sys.argv[2]

if __name__ == '__main__':
    main()

























