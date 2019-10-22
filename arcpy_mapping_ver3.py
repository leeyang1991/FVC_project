# coding=gbk
import os
import arcpy
import time
import codecs

this_root = os.getcwd()+'\\..\\'


def mk_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def mapping(current_dir,tif,outjpeg,title,mxd_file=this_root+u'出图1.mxd'.encode('gbk')):

    mxd = arcpy.mapping.MapDocument(mxd_file)
    df0 = arcpy.mapping.ListDataFrames(mxd)[0]

    workplace = "RASTER_WORKSPACE"

    lyr = arcpy.mapping.ListLayers(mxd, 'tif', df0)[0]
    lyr.replaceDataSource(current_dir,workplace,tif)

    for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if textElement.name == 'title':
            textElement.text = (title)

    # dir = dir.encode('gbk')
    # print 'saving mxd to',(current_dir+'\\mxd.mxd').decode('gbk')

    arcpy.mapping.ExportToJPEG(mxd,outjpeg,data_frame='PAGE_LAYOUT',df_export_width=mxd.pageSize.width,df_export_height=mxd.pageSize.height,color_mode='24-BIT_TRUE_COLOR',resolution=300,jpeg_quality=100)



def mapping_annual():
    fdir = 'E:\\FVC内蒙古植被覆盖数据\\30m年值_1978_1985_1995_2005_2018\\'.decode('gbk')
    outdir = 'E:\\FVC内蒙古植被覆盖数据\\jpg\\30m年值_new\\'.decode('gbk')
    mk_dir(outdir)
    flist = os.listdir(fdir)
    for f in flist:
        # if f.endswith('.tif') and not '_2005-' in f:
        if f.endswith('.tif'):
            year = f.split('_')[1].split('.')[0]
            print(year)
            title = '{}年内蒙古自治区植被覆盖度分布图'.format(year)
            # # print(title.decode('gbk'))
            # # exit()
            # # title = ''
            tif = f
            outjpeg = outdir + title.decode('gbk')
            mxd = 'C:\\Users\\ly\\OneDrive\\北师大\\雷添杰\\水土流失与保持\\190823\\出图1.mxd'
            mapping(fdir, tif, outjpeg, title, mxd_file=mxd)



def main():

    # dir = this_root+'190509\\民权线路cad\\dwg_to_shp\\10kV鲁10Ⅱ鲁西线\\'
    # current_dir, tif, outjpeg = 'E:\\FVC内蒙古植被覆盖数据\\1km年值_1978_1985_1995_2005_2018\\'.decode('gbk'),'CDR_1978.tif','E:\\FVC内蒙古植被覆盖数据\\jpg\\CDR_1978.tif'.decode('gbk')
    fdir = 'E:\\FVC内蒙古植被覆盖数据\\1km年值_1978_1985_1995_2005_2018\\'.decode('gbk')
    outdir = 'E:\\FVC内蒙古植被覆盖数据\\jpg\\1km年值_new\\'.decode('gbk')
    mk_dir(outdir)
    flist = os.listdir(fdir)
    for f in flist:
        # if f.endswith('.tif') and not '_2005-' in f:
        if f.endswith('.tif'):
            print(f)
            try:
                date = f.split('_')[2]
                year = date.split('-')[0]
                month = '%01d'%int(date.split('-')[1])
                # print(year,month)
                # exit()

                title = '{}年{}月内蒙古自治区植被覆盖度分布图'.format(year,month)
                # # print(title.decode('gbk'))
                # # exit()
                # # title = ''
                tif = f
                outjpeg = outdir+title.decode('gbk')
                mxd = 'C:\\Users\\ly\\OneDrive\\北师大\\雷添杰\\水土流失与保持\\190823\\出图1.mxd'
                mapping(fdir,tif,outjpeg,title,mxd_file=mxd)
            except:
                date = f.split('_')[4]
                year = date.split('-')[0]
                month = '%01d' % int(date.split('-')[1])
                # print(year,month)
                # exit()

                title = '{}年{}月内蒙古自治区植被覆盖度分布图'.format(year, month)
                # # print(title.decode('gbk'))
                # # exit()
                # # title = ''
                tif = f
                outjpeg = outdir + title.decode('gbk')
                mxd = 'C:\\Users\\ly\\OneDrive\\北师大\\雷添杰\\水土流失与保持\\190823\\出图1.mxd'
                mapping(fdir, tif, outjpeg, title, mxd_file=mxd)
            # exit()
    pass


if __name__ == '__main__':
    mapping_annual()


