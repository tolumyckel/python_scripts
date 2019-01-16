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
    test_dms2dd()
def getEW(dmsRecord):
    f_dmsRecord= dmsRecord.strip("\n")
    fs_dmRecord = f_dmsRecord.split()
    return fs_dmRecord[3].upper()

def getNS(dmsRecord):
    f_dmsRecord= dmsRecord.strip("\n")
    fs_dmRecord = f_dmsRecord.split()
    return fs_dmRecord[-1].upper()

def dms2dd(dmsRecord):
    f_dmsRecord = dmsRecord.strip("\n").split()
    long_dd = int(f_dmsRecord[0])+float(f_dmsRecord[1])/60+float(f_dmsRecord[2])/3600
    if 180 >= int(f_dmsRecord[0]) >= 0 and 60 > float(f_dmsRecord[1]) >= 0 and 60 > float(f_dmsRecord[2]) >= 0 and long_dd <= 180:
        if getEW(dmsRecord) == 'W':
            long_dd = -long_dd
    else:
        return None
    lat_dd = int(f_dmsRecord[4])+float(f_dmsRecord[5])/60+float(f_dmsRecord[6])/3600
    if 90 >= int(f_dmsRecord[4]) >= 0 and 60 > float(f_dmsRecord[5]) >= 0 and 60 > float(f_dmsRecord[6]) >= 0 and lat_dd <= 90:
        if getNS(dmsRecord) == 'S':
            lat_dd = -lat_dd
    else:
        return None


    return long_dd, lat_dd

def test_dms2dd():
    # Test case 1
    expected = (-180.0, -80.99972222222222)
    actual = dms2dd("180 00 00 w 80 59 59 s\n")
    if expected == actual:
        print "dms2dd('180 00 00 w 80 59 59 s\n') passed"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...

if __name__ == '__main__':
    main()