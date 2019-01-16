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
import os
def main():
    exportToKml("../../data/quakes2000.txt","../../data/quakes2000.kml")

def exportToKml(inFile,outKml):
    """Function documentation:
       - What does function do?
       - What is/are expected parameter value(s)?
       - What does function return, if anything
       - Example usage"""
    #os.chdir("../../data")

    with open(inFile) as txt, \
    open(outKml, 'w') as kml:
        kml.write(getKmlHeader())
        texts = txt.readlines()
        count = 0
        for text in texts:
            if count > 1:
                doc = text.rstrip()
                f_doc = doc.split(",")
                kml.write(getKmlPlacemark(f_doc[2],f_doc[1],f_doc[3],f_doc[4]))
            count +=1
        kml.write(getKmlFooter())




def getKmlHeader():
    return """<kml>
<Document>\n"""
def getKmlPlacemark(longitude,latitude, depth, magnitude):
    return """\t<Placemark>
\t\t<name>{magnitude_v}</name>
\t\t<description>Mag={magnitude_v}, Depth={depth_v} km</description>
\t\t<Point>
\t\t\t<coordinates>{longitude_v},{latitude_v},0</coordinates>
\t\t</Point>
\t</Placemark>\n""".format(magnitude_v = magnitude,depth_v=depth,longitude_v=longitude,latitude_v=latitude)

def getKmlFooter():
    return """</Document>
</kml>"""


if __name__ == '__main__':
    main()