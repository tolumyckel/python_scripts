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

    test_getFeatureTypeFromName()

def getFeatureTypeFromName(fcName):
    f_fcName = fcName.split('_')

    if  len(f_fcName) > 1:
        if f_fcName[1].upper() == 'PLY':
            return 'Polygon'
        elif f_fcName[1].upper() == 'LIN':
            return 'Line'
        elif f_fcName[1].upper() == 'PNT':
            return 'Point'
        else:
            return 'Unknown'
    else:
        return 'Unknown'


def test_getFeatureTypeFromName():
    # Test case 1
    expected = "Unknown"
    actual = getFeatureTypeFromName("Byline_.pLY")
    if expected == actual:
        print "getFeatureTypeFromName('Byline..pLY') passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...
    expected = "Unknown"
    actual = getFeatureTypeFromName("Byline_lin")
    if expected == actual:
        print "getFeatureTypeFromName('Byline_lin') passed"
    else:
        print fmt.format(expected, actual)

    #Test case 3
    expected = "Point"
    actual = getFeatureTypeFromName("Byline_PNT")
    if expected == actual:
        print "getFeatureTypeFromName('Byline_lin') passed"
    else:
        print fmt.format(expected, actual)


if __name__ == '__main__':
    main()