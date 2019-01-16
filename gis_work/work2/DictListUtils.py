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
import types

def main():
   pass

def getMissingKeys(dictRef, dictToCompare):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""

    list_miskey = []
    for i in range(len(dictRef)):
        mis_key =  dictRef.keys()[i]
        if dictToCompare.has_key(mis_key):
            continue
        else:
            list_miskey.append(mis_key)
    return list_miskey


def getMissingKeysWithCount(dictRef, dictToCompare):
    list_miskey = getMissingKeys(dictRef, dictToCompare)
    count_miskey = len(list_miskey)
    return count_miskey,list_miskey

def getUnique(inList):
    new_list  = []
    for i in range(len(inList)):
        if inList[i] not in new_list:
            new_list.append(inList[i])
    return new_list

def flattenList(inList):
    new_list = []
    for inlst in inList:
        if type(inlst) is types.ListType or type(inlst) is types.TupleType:
            for lst in inlst:
                new_list.append(lst)
        else:
            new_list.append(inlst)
    return new_list





if __name__ == '__main__':
    main()