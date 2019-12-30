# coding=gbk

import arcpy
import os
import log_process
import time
from arcpy import sa
import multiprocessing

# this_root = os.getcwd()+'\\..\\'

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


# def cal_ndvi(tif=this_root+'AVHRR_clipped\\CDR_1981-07-01_1981-08-01.tif'):
#
#     pass


def kernel_do_clip_nongmu(params):

    sn,fdir,save_dir = params
    print('\n' + sn.decode('gbk'))
    in_template_dataset = r'D:\FVC\农牧交错带新\\' + sn + '.shp'
    flist = os.listdir(fdir)
    for f in flist:
        if not f.endswith('.tif'):
            continue
        in_raster = fdir + f
        out_raster = save_dir + f.split('.tif')[0] + '_' + sn + '.tif'
        nodata_value = -127
        arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)


def do_clip_nongmu():
    # fdir = r'E:\FVC内蒙古植被覆盖数据\1km年值_1978_1985_1995_2005_2018\\'
    # save_dir = r'E:\FVC内蒙古植被覆盖数据\1km年值_1978_1985_1995_2005_2018_nongmu_clipped\\'

    fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km\\'
    save_dir = r'D:\FVC\FVC_1km_new\nongmu\\'

    mk_dir(save_dir)
    shp_name = ['内蒙古草地','鄂尔多斯市','内蒙古农牧交错带']
    # {'草地分布图': '', '': '', '农牧交错带': ''}
    params = []
    for sn in shp_name:
        params.append([sn,fdir,save_dir])
    # for p in params:
    #     kernel_do_clip_nongmu(p)

    pool = multiprocessing.Pool()
    pool.map(kernel_do_clip_nongmu,params)
    pool.close()
    pool.join()

    pass


def kernel_do_clip_4quyu(params):
    sn,save_dir,fdir=params

    print('\n' + sn.decode('gbk'))
    in_template_dataset = r'D:\FVC\内蒙水土流失分区\\' + sn + '.shp'
    mk_dir(save_dir)
    flist = os.listdir(fdir)
    flag = 0

    for f in flist:
        if not f.endswith('.tif'):
            flag += 1
            continue
        in_raster = fdir + f
        out_raster = save_dir + f.split('.')[0] + '_' + sn + '.tif'
        nodata_value = -127
        arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)


def do_clip_4quyu():
    fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km\\'
    save_dir = r'D:\FVC\FVC_1km_new\FVC-year_1km\4fenqu\\'
    mk_dir(save_dir)
    shp_name = ['北方风沙区','北方土石山区','东北黑土区','西北黄土高原区']
    params = []
    for sn in shp_name:
        params.append([sn,save_dir,fdir])

    pool = multiprocessing.Pool()
    pool.map(kernel_do_clip_4quyu,params)
    pool.close()
    pool.join()


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




def kernel_clip_zhongdian(params):
    sn,save_dir,fdir=params

    print('\n' + sn.decode('gbk'))
    in_template_dataset = r'E:\FVC内蒙古植被覆盖数据\FVC_D\重点1\分区shp\重点县市区\\' + sn + '.shp'
    mk_dir(save_dir)
    flist = os.listdir(fdir)
    flag = 0

    for f in flist:
        if not f.endswith('.tif'):
            flag += 1
            continue
        in_raster = fdir + f
        out_raster = save_dir + f.split('.')[0] + '_' + sn + '.tif'
        # print(out_raster)
        # exit()
        nodata_value = -127
        arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)




def clip_zhongdian():
    # fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km_clipped\\'
    fdir = r'D:\FVC\30m_substract_int\\'
    # save_dir = r'D:\FVC\重点区域范围\1km_fenqu_clipped\\'
    save_dir = r'D:\FVC\重点区域范围\30m_fenqu_substract\\'
    mk_dir(save_dir)
    shp_name = ['太行山山地丘陵区', '宁蒙覆沙黄土丘陵区', '晋陕蒙丘陵沟壑区', '燕山及辽西山地丘陵区']
    params = []
    for sn in shp_name:
        params.append([sn, save_dir, fdir])

    pool = multiprocessing.Pool(4)
    pool.map(kernel_clip_zhongdian, params)
    pool.close()
    pool.join()


def kernel_clip_zhongdian1(params):
    sn,save_dir,fdir=params

    print('\n' + sn.decode('gbk'))
    in_template_dataset = r'D:\FVC\重点区域范围\shp\\' + sn + '.shp'
    mk_dir(save_dir)
    flist = os.listdir(fdir)
    flag = 0

    for f in flist:
        if not f.endswith('.tif'):
            flag += 1
            continue
        in_raster = fdir + f
        out_raster = save_dir + f.split('.')[0] + '_' + sn + '.tif'
        nodata_value = -127
        arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)



def clip_zhongdian1():
    fdir = r'E:\FVC内蒙古植被覆盖数据\FVC_D\30m_substract_int\\'
    save_dir = r'E:\FVC内蒙古植被覆盖数据\FVC_D\重点1\substract\\'
    mk_dir(save_dir)
    shp_name = ['赤峰市', '鄂尔多斯', '通辽市', '准格尔旗']
    params = []
    for sn in shp_name:
        params.append([sn, save_dir, fdir])
        kernel_clip_zhongdian([sn, save_dir, fdir])
    # kernel_clip_zhongdian(params[0])
    # pool = multiprocessing.Pool(4)
    # pool.map(kernel_clip_zhongdian, params)
    # pool.close()
    # pool.join()


def clip_tongliao():
    fdir = r'D:\FVC\30m年值_1978_1985_1995_2005_2018\\'
    save_dir = r'D:\\FVC\\tongliao\\clipped\\'
    mk_dir(save_dir)

    # sn, save_dir, fdir = params
    # sn = ''
    # print('\n' + sn.decode('gbk'))
    in_template_dataset = r'D:\FVC\tongliao\通辽\通辽市.shp'
    mk_dir(save_dir)
    flist = os.listdir(fdir)
    flag = 0

    for f in flist:
        if not f.endswith('.tif'):
            flag += 1
            continue
        in_raster = fdir + f
        out_raster = save_dir + f.split('.')[0].split('fvc')[1] + '_' + '通辽.tif'
        # print(out_raster)
        # exit()
        nodata_value = -127
        arcpy_clip(in_raster, out_raster, in_template_dataset, nodata_value)



def clip_geqi():
    # 内蒙古各旗矢量边界
    tif_dir = r'E:\FVC内蒙古植被覆盖数据\fusion\fusion_int\\'
    out_dir = r'D:\FVC\geqi\\'
    shp_name = ['赤峰', '鄂尔多斯', '通辽市', '准格尔旗']
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
    # do_clip_4quyu()
    clip_zhongdian1()
    # clip_tongliao()