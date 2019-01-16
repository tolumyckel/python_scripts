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
    test_getInitials()

def getInitials(fullName):
    initial = "."
    initial_list = []
    if fullName:
        name_list = fullName.split()
        for i in range(len(name_list)):
            initial_list.append(name_list[i][0])
        return "{} / {}.".format(fullName ,initial.join(initial_list))
    pass



def test_getInitials():
    # Test case 1
    expected = "John Samuel Wobbly / J.S.W."
    actual = getInitials("John Samuel Wobbly")
    if expected == actual:
        print "getInitials('John Samuel Wobbly') passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()