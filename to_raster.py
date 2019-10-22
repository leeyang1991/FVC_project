# coding=utf-8

import osr, ogr
import gdal
import numpy as np
import os

this_root = os.path.dirname(__file__)

def raster2array(rasterfn):
    '''
    create array from raster
    Agrs:
        rasterfn: tiff file path
    Returns:
        array: tiff data, an 2D array
    '''
    raster = gdal.Open(rasterfn)
    geotransform = raster.GetGeoTransform()
    originX = geotransform[0]
    originY = geotransform[3]
    pixelWidth = geotransform[1]
    pixelHeight = geotransform[5]
    band = raster.GetRasterBand(1)
    array = band.ReadAsArray()
    array = np.asarray(array)
    del raster
    return array,originX,originY,pixelWidth,pixelHeight



def array2raster(newRasterfn,longitude_start,latitude_start,pixelWidth,pixelHeight,array):
    cols = array.shape[1]
    rows = array.shape[0]
    originX = longitude_start
    originY = latitude_start
    # open geotiff
    driver = gdal.GetDriverByName('GTiff')
    if os.path.exists(newRasterfn):
        os.remove(newRasterfn)
    outRaster = driver.Create(newRasterfn, cols, rows, 1, gdal.GDT_Float32)
    # Add Color Table
    # outRaster.GetRasterBand(1).SetRasterColorTable(ct)
    outRaster.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
    # Write Date to geotiff
    outband = outRaster.GetRasterBand(1)
    ndv = 255
    outband.SetNoDataValue(ndv)
    outband.WriteArray(array)
    # outRasterSRS = osr.SpatialReference()
    # outRasterSRS.ImportFromEPSG(4326)
    # outRaster.SetProjection(outRasterSRS.ExportToWkt())
    # Close Geotiff
    outband.FlushCache()
    del outRaster

if __name__ == '__main__':
    pass

