# coding=gbk

import arcpy
import os
import log_process
import time


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
    fdir = r'D:\FVC\FVC_1km_new\1km_30m_cubic\\'
    outdir = r'D:\FVC\FVC_1km_new\1km_30m_cubic_int\\'
    mk_dir(outdir)
    for f in os.listdir(fdir):
        if f.endswith('.tif'):
            print(f)
            arcpy.CopyRaster_management(fdir+f, outdir+f, "DEFAULTS", "", "255", "", "","8_BIT_UNSIGNED")



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


def clip_neimeng_quanqu():
    shp = r'D:\FVC\nmjx\vector\nmsj1.shp'
    fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km\\'
    out_dir = r'D:\FVC\FVC_1km_new\FVC-year_1km_clipped\\'
    mk_dir(out_dir)
    for f in os.listdir(fdir):
        if f.endswith('.tif'):
            in_raster = fdir+f
            out_raster = out_dir+f
            in_template_dataset = shp
            nodata_value = -127
            arcpy_clip(in_raster,out_raster,in_template_dataset,nodata_value)
    pass







    pass

if __name__ == '__main__':
    # build_pyramids()
    # arcpy_con()
    # arcpy_con()
    pass