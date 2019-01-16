#This file was originally generated by PyScripter's unit test wizard

import unittest
import MyGIS

reload(MyGIS)

class TestMap(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test__init__(self):
        pass

    def testname(self):
        pass

    def testname(self):
        pass

    def testaddLayer(self):
        #ARRANGE
        raster = MyGIS.RasterLayer()
        raster.name = 'Raster'

        map_class = MyGIS.Map()
        map_class.name = 'Map'
        map_class.addLayer(raster)
        layer = map_class.layers[0]
        expected = ('Raster','./data/Image.ras')

        #ACT
        raster.dataSource = './data/Image.ras'
        actual = (layer.name,layer.dataSource)

        #ASSERT
        self.assertEqual(expected,actual)


    def testremoveLayer(self):
        #ARRANGE
        raster = MyGIS.RasterLayer()
        raster.name = 'Raster'

        map_class = MyGIS.Map()
        map_class.name = 'Map'
        map_class.addLayer(raster)
        map_class.removeLayer(raster.name)

        expected = []

        #ACT
        raster.dataSource = './data/Image.ras'
        actual = map_class.layers

        #ASSERT
        self.assertEqual(expected,actual)



class TestRasterLayer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testrows(self):
        #ARRANGE
        raster = MyGIS.RasterLayer()
        raster.name = "Image"

        expected = 6

        #ACT
        raster.dataSource = "./data/Image.ras"

        actual = raster.rows

        #ASSERT
        self.assertEqual(expected,actual)


    def testcols(self):
        #ARRANGE
        raster = MyGIS.RasterLayer()
        raster.name = "Image"
        #raster.cols = 4
        expected = 4

        #ACT
        raster.dataSource = "./data/Image.ras"
        #raster.cols = 6
        actual = raster.cols

        #ASSERT
        self.assertEqual(expected,actual)


class TestFeatureLayer(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testfeatureType(self):
        #ARRANGE
        feature = MyGIS.FeatureLayer()
        feature.name = "Feature"
        #raster.rows = 6
        expected = "POINT"

        #ACT
        feature.dataSource = "./data/Cities.pnt"
        #raster.rows = 6
        actual = feature.featureType

        #ASSERT
        self.assertEqual(expected,actual)

    def testfeatureCount(self):
        #ARRANGE
        feature = MyGIS.FeatureLayer()
        feature.name = "Feature"
        #raster.rows = 6
        expected = 16

        #ACT
        feature.dataSource = "./data/Cities.pnt"
        #raster.rows = 6
        actual = feature.featureCount

        #ASSERT
        self.assertEqual(expected,actual)

class TestGlobalFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testmain(self):
        pass

if __name__ == '__main__':
    unittest.main()
