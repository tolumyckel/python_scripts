# -*- coding: UTF-8 -*-
# ------------------------------------------------------------------------------
# Name:        exercise_template.py
#
# Purpose:     Brief desciption of what module does
#
# Usage:       Module name and required/optional command-line parameters (if any)
#
# Author:      Your name(s)
#
# Created:     dd/mm/yyyy
# ------------------------------------------------------------------------------
import os,sys

def main():
    dumpFileList("TestFolder","dumpfile.txt")

def dumpFileList(folder, dumpFile):
    path = os.path.dirname(os.path.abspath(__file__))
    foldername = os.path.join(path,folder)
    if os.path.exists(foldername):
        names = os.listdir(foldername)
        fn_ls = []
        with open(dumpFile,'w') as dumpfile_w:
            for name in names:
                if os.path.isfile(os.path.join(foldername,name)):
                    dumpfile_w.write("{}\n".format(name))
                    fn_ls.append(name)
        return fn_ls
    else:
        print "Sorry, Invalid Path"
        sys.exit()

if __name__ == '__main__':
    main()