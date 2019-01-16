#-------------------------------------------------------------------------------
# Name:        Module name
# Purpose:     Brief desciption of what module does
# Usage:       Module name and required/optional command-line parameters (if any)
# Author:      Your name(s)
#
# Created:     21/10/2016
#-------------------------------------------------------------------------------

fmt = "Expected: {}\tActual  : {}"

def main():
    test_isValidPhoneNumber()
    test_phoneNumberHasLetters()

def isValidPhoneNumber(phoneNumber):
    s_phoneNumber = phoneNumber.split("-")
    f_phoneNumber = phoneNumber.replace("-","")
    if len(phoneNumber) == 12 and len(s_phoneNumber[0]) == 3 and len(s_phoneNumber[1]) == 3 and len(s_phoneNumber[2]) == 4 and f_phoneNumber.isdigit():
        return True
    else:
        return False

def phoneNumberHasLetters(phoneNumber):
    s_phoneNumber = phoneNumber.split("-")
    f_phoneNumber = phoneNumber.replace("-","")
    #print f_phoneNumber.isalnum()
    if len(phoneNumber) == 12 and len(s_phoneNumber[0]) == 3 and len(s_phoneNumber[1]) == 3 and len(s_phoneNumber[2]) == 4 and f_phoneNumber[0:3].isdigit() and f_phoneNumber.upper().isupper():
        return True
    else:
        return False

def test_isValidPhoneNumber():
    # Test case 1
    expected = True
    actual = isValidPhoneNumber('705-718-6105')
    if expected == actual:
        print "isValidPhoneNumber('705-718-605') passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...
    expected = True
    actual = isValidPhoneNumber('70a-71E-6B05')
    if expected == actual:
        print "isValidPhoneNumber('705-71E-6B05') passed"
    else:
        print fmt.format(expected, actual)

def test_phoneNumberHasLetters():
    # Test case 1
    expected = True
    actual = phoneNumberHasLetters('705-718-6105')
    if expected == actual:
        print "isValidPhoneNumber('705-718-605') passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...
    expected = True
    actual = phoneNumberHasLetters('A06-71E-6B05')
    if expected == actual:
        print "isValidPhoneNumber('705-71E-6B05') passed"
    else:
        print fmt.format(expected, actual)

if __name__ == '__main__':
    main()