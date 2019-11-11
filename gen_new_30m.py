# coding=gbk

import os
import arcpy
from arcpy.sa import *
import multiprocessing
from arcpy import sa


arcpy.CheckOutExtension("Spatial")
this_root = r'D:\FVC\\'

def mkdir(fdir):
    if not os.path.isdir(fdir):
        os.makedirs(fdir)


def resample30m():
    fvc_1km_dir = this_root+'FVC_1km_new\\FVC-year_1km_clipped_0_100\\'
    # fvc_30m_dir = this_root+'30m年值_1978_1985_1995_2005_2018\\'
    # fvc_30m_tif = this_root+'30m年值_1978_1985_1995_2005_2018\\LC08_2018.tif'
    out_dir = this_root+'FVC_1km_new\\1km_30m_cubic\\'
    mkdir(out_dir)
    for f in os.listdir(fvc_1km_dir):
        if f.endswith('.tif'):
            print(f)
            arcpy.Resample_management(fvc_1km_dir+f,out_dir+f,"27.0427354","CUBIC")


def raster_cal(raster1,raster2,outf):

    # fusion 30 and 1km
    # raster1 = this_root+'1km_30m_cubic\\MCD43A4_2018.tif'
    # raster2 = this_root+'30m年值_1978_1985_1995_2005_2018\\LC08_2018.tif'
    # outf = this_root+'cal_raster2018.tif'
    print(outf)
    # raster3 = (Raster(raster2) + Raster(raster1))/2
    raster3 = Raster(raster1)*0.3 + Raster(raster2)*0.7
    # Don't forget to save eg:
    raster3.save(outf)


def raster_0_100():
    fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km_clipped\\'
    outdir = r'D:\FVC\FVC_1km_new\FVC-year_1km_clipped_0_100\\'
    mkdir(outdir)
    for f in os.listdir(fdir):
        if f.endswith('.tif'):
            print(f)
            raster_in = Raster(fdir+f)
            raster_out = raster_in*100
            raster_out.save(outdir+f)
            pass


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

    for year in [1978,1985,1995,2005,2018]:
        for i,f in enumerate(os.listdir(fdir)):
            if f.endswith('.tif') and str(year) in f:
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
    #     for i in p:
    #         print(i)
    #     print('****')
        # kernel_one_year_change(p)

    pool = multiprocessing.Pool()
    pool.map(kernel_one_year_change,pamams)
    pool.close()
    pool.join()

    pass


def kernel_float_to_int(params):
    f,fdir,out_dir = params
    if f.endswith('.tif'):
        print(f)
        arcpy.CopyRaster_management(fdir + f, out_dir + f, "DEFAULTS", "", "-128", "", "", "8_BIT_SIGNED")


def float_to_int():
    # arcpy.CheckOutExtension('Spatial')
    # arcpy.env.workspace = 'E:\\FVC内蒙古植被覆盖数据\\fusion\\'
    # rasters = arcpy.ListRasters('*.tif*')
    # for raster in rasters:
    #     print(raster)
    #     outInt = arcpy.sa.Int(raster)
    #     outInt.save(u'E:\\FVC内蒙古植被覆盖数据\\fusion\\int_'+raster)
    fdir = r'D:\FVC\FVC_1km_new\fusion1\\'
    out_dir = r'D:\FVC\FVC_1km_new\fusion_int1\\'
    mkdir(out_dir)
    params = []
    for f in os.listdir(fdir):
        param = [f,fdir,out_dir]
        kernel_float_to_int(param)
    # pool = multiprocessing.Pool()
    # pool.map(kernel_float_to_int,params)
    # pool.close()
    # pool.close()

def fusion():
    dir_1km = r'D:\FVC\FVC_1km_new\1km_30m_cubic\\'
    dir_30m = r'D:\FVC\30m年值_1978_1985_1995_2005_2018\\'
    out_dir = r'D:\FVC\FVC_1km_new\fusion1\\'
    mkdir(out_dir)
    year_list = ['1978','1985','1995','2005','2018']

    # for f in
    list_1km = []
    list_30m = []

    for y in year_list:
        for f in os.listdir(dir_1km):
            if y in f and f.endswith('.tif'):
                list_1km.append(dir_1km+f)

    for y in year_list:
        for f in os.listdir(dir_30m):
            if y in f and f.endswith('.tif'):
                list_30m.append(dir_30m+f)

    for i in range(len(list_30m)):
        raster1 = list_30m[i]
        raster2 = list_1km[i]
        outraster = out_dir+year_list[i]+'.tif'
        raster_cal(raster1,raster2,outraster)

def arcpy_con():
    # arcpy condition
    # 0-100
    arcpy.CheckOutExtension('Spatial')
    arcpy.env.workspace = r'D:\FVC\FVC_1km_new\fusion_int1\\'
    out_dir = r'D:\FVC\FVC_1km_new\fusion_int_0-100_1\\'
    mkdir(out_dir)
    rasters = arcpy.ListRasters('*.tif*')
    for raster in rasters:
        # Save temp raster to disk with new name
        print(raster)
        ras = sa.Raster(raster)
        # arcpy.CalculateStatistics_management(ras)
        fvc = ras
        fvc = sa.Con(fvc, 0, fvc, "VALUE < 0")
        fvc = sa.Con(fvc, 100, fvc, "VALUE > 100")
        fvc.save(out_dir+raster)


def main():
    # one_year_change()
    # float_to_int()
    # raster_cal()
    # resample30m()
    # fusion()
    # float_to_int()
    arcpy_con()
    pass
if __name__ == '__main__':
    main()