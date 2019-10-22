# coding=gbk

import os
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")
this_root = 'E:\\FVC内蒙古植被覆盖数据\\'

def mkdir(fdir):
    if not os.path.isdir(fdir):
        os.makedirs(fdir)


def resample30m():
    fvc_1km_dir = this_root+'1km年值_1978_1985_1995_2005_2018\\'
    # fvc_30m_dir = this_root+'30m年值_1978_1985_1995_2005_2018\\'
    fvc_30m_tif = this_root+'30m年值_1978_1985_1995_2005_2018\\LC08_2018.tif'
    out_dir = this_root+'1km_30m_cubic\\'
    mkdir(out_dir)
    for f in os.listdir(fvc_1km_dir):
        if f.endswith('.tif'):
            print(f)
            arcpy.Resample_management(fvc_1km_dir+f,out_dir+f,"27.0427354","CUBIC")

def raster_cal():


    raster1 = this_root+'1km_30m_cubic\\MCD43A4_2018.tif'
    raster2 = this_root+'30m年值_1978_1985_1995_2005_2018\\LC08_2018.tif'
    outf = this_root+'cal_raster2018.tif'
    print(outf)
    raster3 = (Raster(raster2) + Raster(raster1))/2
    # Don't forget to save eg:
    raster3.save(outf)


def main():
    raster_cal()

if __name__ == '__main__':
    main()