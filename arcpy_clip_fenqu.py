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
    folder_name = '1km月值_1978_1985_1995_2005_2018'
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


def clip_nongmujiaocuodai():
    P = log_process
    folder_name = '1km年值_1978_1985_1995_2005_2018'
    fdir = this_root + folder_name + '\\'
    save_dir = this_root + folder_name + '_clipped_nongmu\\'
    shp_name = ['鄂尔多斯市边界线', '内蒙古草地分布图', '内蒙古农牧交错带']
    for sn in shp_name:
        print('\n' + sn.decode('gbk'))
        in_template_dataset = this_root + '\\农牧交错带\\内蒙古农牧交错带shp文件(1)\\内蒙古农牧交错带shp文件\\' + sn + '.shp'
        mk_dir(save_dir)
        flist = os.listdir(fdir)
        flag = 0

        time_init = time.time()
        for f in flist:
            start = time.time()
            if not f.endswith('.tif'):
                flag += 1
                continue
            in_raster = fdir + f
            out_raster = save_dir + f + '_' + sn + '.tif'
            # print(out_raster)

            nodata_value = 255

            arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)
            end = time.time()
            P.process_bar(flag, len(flist), time_init, start, end)
            flag += 1

    pass



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
    clip_nongmujiaocuodai()