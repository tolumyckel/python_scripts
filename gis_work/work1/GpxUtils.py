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
    test_getCoordsFromGpx()

def getCoordsFromGpx(gpx):
    if 'trkpt' in gpx:
        f_gpx = gpx.strip('>')
        l_gpx = f_gpx.split()
        for i in l_gpx:
            if 'lat' in i:
                lat_val = i.split("=")
            if 'lon' in i:
                long_val = i.split("=")
        f_lat_val = float(lat_val[1].strip('"'))
        f_lon_val = float(long_val[1].strip('"'))
        return f_lon_val, f_lat_val
    else:
        return None


def test_getCoordsFromGpx():
    # Test case 1
    expected = (-75.7472631, 45.3888995)
    actual = getCoordsFromGpx('<trkpt lat="45.388995" lon="-75.7472631">')
    if expected == actual:
        print "getCoordsFromGpx('<trkpt lat='45.3888995' lon='-75.7472631'>')"
    else:
        print fmt.format(expected, actual)

    # Test case 2 ...


if __name__ == '__main__':
    main()