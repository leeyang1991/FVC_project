# coding=gbk

import arcpy
import os
import log_process
import time
from arcpy import sa

this_root = os.getcwd()+'\\..\\'

def mk_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)

def arcpy_clip(in_raster,out_raster,in_template_dataset,nodata_value):
    # in_raster = this_root+'MRT_resample\\2000_257.txt_mosaic.hdf.FVC.tif'
    # out_raster = this_root+'test.tif'
    # in_template_dataset = this_root+'shp\\neimeng.shp'
    # nodata_value = 255
    clipping_geometry = True
    # print 'clipping'

    arcpy.Clip_management(
    in_raster=in_raster, rectangle=None, out_raster=out_raster,
        in_template_dataset=in_template_dataset, nodata_value=nodata_value,
        clipping_geometry=clipping_geometry, maintain_clipping_extent=None)


def cal_ndvi(tif=this_root+'AVHRR_clipped\\CDR_1981-07-01_1981-08-01.tif'):

    pass


def do_clip():
    P = log_process
    folder_name = '30m月值_1978_1985_1995_2005_2018'
    fdir = this_root+folder_name+'\\'
    save_dir = this_root+folder_name+'_clipped\\'
    shp_name = ['北方风沙区','北方土石山区','东北黑土区','西北黄土高原区']
    for sn in shp_name:
        print('\n'+sn.decode('gbk'))
        in_template_dataset = this_root + '内蒙水土流失分区\\'+sn+'.shp'
        mk_dir(save_dir)
        flist = os.listdir(fdir)
        flag = 0

        time_init = time.time()
        for f in flist:
            start = time.time()
            if not f.endswith('.tif'):
                flag += 1
                continue
            in_raster = fdir+f
            out_raster = save_dir+f+'_'+sn+'.tif'
            # print(out_raster)

            nodata_value = 255

            arcpy_clip(in_raster,out_raster,in_template_dataset,nodata_value)
            end = time.time()
            P.process_bar(flag, len(flist),time_init,start,end)
            flag += 1
            # exit()


    pass



def float_to_int():
    # arcpy.CheckOutExtension('Spatial')
    # arcpy.env.workspace = 'E:\\FVC内蒙古植被覆盖数据\\fusion\\'
    # rasters = arcpy.ListRasters('*.tif*')
    # for raster in rasters:
    #     print(raster)
    #     outInt = arcpy.sa.Int(raster)
    #     outInt.save(u'E:\\FVC内蒙古植被覆盖数据\\fusion\\int_'+raster)
    fdir = 'E:\\FVC内蒙古植被覆盖数据\\fusion\\'
    for f in os.listdir(fdir):
        if f.endswith('.tif'):
            print(f)
            arcpy.CopyRaster_management("E:\\FVC内蒙古植被覆盖数据\\fusion\\"+f, "E:\\FVC内蒙古植被覆盖数据\\fusion\\test\\int_"+f, "DEFAULTS", "", "255", "", "","8_BIT_UNSIGNED")



def build_pyramids():
    f = 'E:\\FVC内蒙古植被覆盖数据\\fusion\\fusion_int\\2018.tif'
    arcpy.env.workspace = "C:/Workspace"
    inws = "folder"
    includedir = "INCLUDE_SUBDIRECTORIES"
    buildpy = "BUILD_PYRAMIDS"
    calcstats = "CALCULATE_STATISTICS"
    buildsource = "NONE"
    blockfield = "#"
    estimatemd = "#"
    skipx = "4"
    skipy = "6"
    ignoreval = "0;255"
    pylevel = "3"
    skipfirst = "NONE"
    resample = "BILINEAR"
    compress = "JPEG"
    quality = "80"
    skipexist = "SKIP_EXISTING"
    # arcpy.BuildPyramidsAndStatistics_management()
    print('building '+f)
    arcpy.BuildPyramids_management(f)
    # arcpy.BuildPyramidsAndStatistics_management(
    #     inws, includedir, buildpy, calcstats, buildsource, blockfield,
    #     estimatemd, skipx, skipy, ignoreval, pylevel, skipfirst,
    #     resample, compress, quality, skipexist)


def main():
    arcpy.CheckOutExtension('Spatial')
    arcpy.env.workspace = this_root+'\\AVHRR_clipped\\'
    rasters = arcpy.ListRasters('*.tif*')
    # print(rasters)
    time_init = time.time()
    flag = 0
    for raster in rasters:
        # Save temp raster to disk with new name
        start = time.time()
        ras = sa.Raster(raster)
        arcpy.CalculateStatistics_management(ras)
        max = ras.maximum
        fvc = ras/8000.
        fvc = sa.Con(fvc, 0, fvc, "VALUE < 0")
        fvc = sa.Con(fvc, 1, fvc, "VALUE > 1")
        fvc.save(this_root+'AVHRR_fvc\\'+raster)
        end = time.time()
        logger.process_bar(flag,len(rasters),time_init,start,end,raster)
        flag += 1
        # break

    pass

if __name__ == '__main__':
    build_pyramids()