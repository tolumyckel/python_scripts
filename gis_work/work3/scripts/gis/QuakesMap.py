#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Tolu Olowonyo
#
# Created:     19-11-2018
# Copyright:   (c) Tolu Olowonyo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import zipfile

def main():
    exportToKmz("../../data/quakes2000.kml")

def exportToKmz(outKml):
    with zipfile.ZipFile("../../data/quakes2000.kmz",mode="w") as kmz:

        kmz.write(outKml, compress_type = zipfile.ZIP_DEFLATED)

if __name__ == '__main__':
    main()