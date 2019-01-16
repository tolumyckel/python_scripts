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

def main():
    pass

def getFileContent(fileName):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    try:
        myfile = open(fileName)
        return myfile.read()
        myfile.close()
    except:
        message = "{} does not exist.".format(fileName)
        return message


def writeToFile(fileName,content):
    try:
        myfile = open(fileName,'w')
        myfile.write(content)
        myfile.close()
    except:
        message = "Cannot write {} into {}".format(content,fileName)

if __name__ == '__main__':
    main()