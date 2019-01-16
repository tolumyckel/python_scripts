#-------------------------------------------------------------------------------
# Name:        Module name
# Purpose:     Brief desciption of what module does
# Usage:       Module name and required/optional command-line parameters (if any)
# Author:      Your name(s)
#
# Created:     21/10/2016
#-------------------------------------------------------------------------------

fmt = "Expected: {}\tActual  : {}"
encoded_str = "Tx6op3"

def main():
     test_hasXcode()
     test_getXcodePosition()
     test_getPatternPosition()

def hasXcode(inText):
    if inText.find(encoded_str) != -1:
        return True
    else:
        return False

def getXcodePosition(inText):
    str_position = inText.find(encoded_str)
    if str_position != -1:
        return str_position+1
    else:
        return str_position

def test_getXcodePosition():
    # Test case 1
    expected = 1
    actual = getXcodePosition("Tx6op3dscnuviiueiubcsci")
    if expected == actual:
        print "getXcodePosition('Tx6op3dscnuviiueiubcsci') passed"
    else:
        print fmt.format(expected, actual)


def test_hasXcode():
    # Test case 1
    expected = True
    actual = hasXcode("thdTx6op3dschco45")
    if expected == actual:
        print "hasXcode('thdTx6op3dschco45') passed"
    else:
        print fmt.format(expected, actual)

def test_getPatternPosition():
    expected = 5
    actual = getPatternPosition("Tx6op3","thdTx6op3dschco45")
    if expected == actual:
        print "getPatternPosition('thdTx6op3dschco45') passed"
    else:
        print fmt.format(expected, actual)


def getPatternPosition(pattern,inText):
    str_position = inText.find(pattern)
    if str_position != -1:
        return str_position+1
    else:
        return str_position


    # Test case 2 ...


if __name__ == '__main__':
    main()