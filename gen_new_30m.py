# coding=gbk

import os
import arcpy
from arcpy.sa import *
import multiprocessing

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


def kernel_one_year_change(params):
    fdir,first_raster_list,second_raster_list,out_dir,i = params
    raster1 = fdir + first_raster_list[i]
    raster2 = fdir + second_raster_list[i]
    out_raster = out_dir + str(i + 1) + '.tif'

    print(raster1.decode('gbk'))
    print(raster2.decode('gbk'))
    print(out_raster.decode('gbk'))
    print('****')

    raster3 = Raster(raster2) - Raster(raster1)
    raster3.save(out_raster)



def one_year_change():
    # 两两相减
    # this_root =
    fdir = r'D:\FVC\30m年值_1978_1985_1995_2005_2018\\'
    out_dir = r'D:\FVC\30m_substract\\'
    mkdir(out_dir)
    first_raster_list = []
    second_raster_list = []
    raster_list = []
    for i,f in enumerate(os.listdir(fdir)):
        if f.endswith('.tif'):
            raster_list.append(f)

    for i,f in enumerate(raster_list):
        if i+1 == len(raster_list):
            break
        first_raster_list.append(raster_list[i])
        second_raster_list.append(raster_list[i+1])

    pamams = []
    for i in range(len(first_raster_list)):
        pamams.append([fdir,first_raster_list,second_raster_list,out_dir,i])

    # for p in pamams:
    #     kernel_one_year_change(p)

    pool = multiprocessing.Pool()
    pool.map(kernel_one_year_change,pamams)
    pool.close()
    pool.join()

    pass


def main():
    one_year_change()

if __name__ == '__main__':
    main()