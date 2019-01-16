#-------------------------------------------------------------------------------
# Name:        MyGIS.py
# Purpose:
#
# Author:      Tolu Olowonyo
#
# Created:     03-12-2018
# Copyright:   (c) Tolu Olowonyo 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

class Map(object):
    def __init__(self):
        self.__layers = []
        self.name = ''

    @property
    def layers(self):
        return self.__layers


    def addLayer(self,layer):
        self.__layers.append(layer)

    def removeLayer(self,layer):
        for lyr in self.__layers:
            if lyr.name == layer:
                self.__layers.remove(lyr)



class Layer(object):
    def __init__(self):
        self.name = ''
        self.__dataSource = ''

    #@property
    #def name(self):
    #    return self.name

    #@name.setter
    #def name(self,name):
     #   self.name = name

    @property
    def dataSource(self):
        return self.__dataSource

    @dataSource.setter
    def dataSource(self,dataSource):
        self.__dataSource = dataSource
        self._setMetadata()


class RasterLayer(Layer):
    def __init__(self):
        self.__rows = 0
        self.__cols = 0
        super(RasterLayer, self).__init__()

    @property
    def rows(self):
        return self.__rows

    @property
    def cols(self):
        return self.__cols

    def _setMetadata(self):
        with open(self.dataSource) as ref_file:
            data = ref_file.read(3)
            self.__rows = int(data[0])
            self.__cols = int(data[2])


class FeatureLayer(Layer):
    def __init__(self):
        self.__featureType = ''
        self.__featureCount = 0
        super(FeatureLayer, self).__init__()

    @property
    def featureType(self):
        return self.__featureType

    @property
    def featureCount(self):
        return self.__featureCount

    def _setMetadata(self):
        with open(self.dataSource) as ref_file:
            data = ref_file.readline()
            data = data.split(' ')
            self.__featureType = data[0]
            self.__featureCount = int(data[1])


if __name__ == '__main__':
    main()