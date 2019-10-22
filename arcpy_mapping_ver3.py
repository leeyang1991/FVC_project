# coding=gbk
import os
import arcpy
import time
import codecs

this_root = os.getcwd()+'\\..\\'


def mk_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def mapping(current_dir,tif,outjpeg,title,mxd_file=this_root+u'��ͼ1.mxd'.encode('gbk')):

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
    fdir = 'E:\\FVC���ɹ�ֲ����������\\30m��ֵ_1978_1985_1995_2005_2018\\'.decode('gbk')
    outdir = 'E:\\FVC���ɹ�ֲ����������\\jpg\\30m��ֵ_new\\'.decode('gbk')
    mk_dir(outdir)
    flist = os.listdir(fdir)
    for f in flist:
        # if f.endswith('.tif') and not '_2005-' in f:
        if f.endswith('.tif'):
            year = f.split('_')[1].split('.')[0]
            print(year)
            title = '{}�����ɹ�������ֲ�����Ƕȷֲ�ͼ'.format(year)
            # # print(title.decode('gbk'))
            # # exit()
            # # title = ''
            tif = f
            outjpeg = outdir + title.decode('gbk')
            mxd = 'C:\\Users\\ly\\OneDrive\\��ʦ��\\�����\\ˮ����ʧ�뱣��\\190823\\��ͼ1.mxd'
            mapping(fdir, tif, outjpeg, title, mxd_file=mxd)



def main():

    # dir = this_root+'190509\\��Ȩ��·cad\\dwg_to_shp\\10kV³10��³����\\'
    # current_dir, tif, outjpeg = 'E:\\FVC���ɹ�ֲ����������\\1km��ֵ_1978_1985_1995_2005_2018\\'.decode('gbk'),'CDR_1978.tif','E:\\FVC���ɹ�ֲ����������\\jpg\\CDR_1978.tif'.decode('gbk')
    fdir = 'E:\\FVC���ɹ�ֲ����������\\1km��ֵ_1978_1985_1995_2005_2018\\'.decode('gbk')
    outdir = 'E:\\FVC���ɹ�ֲ����������\\jpg\\1km��ֵ_new\\'.decode('gbk')
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

                title = '{}��{}�����ɹ�������ֲ�����Ƕȷֲ�ͼ'.format(year,month)
                # # print(title.decode('gbk'))
                # # exit()
                # # title = ''
                tif = f
                outjpeg = outdir+title.decode('gbk')
                mxd = 'C:\\Users\\ly\\OneDrive\\��ʦ��\\�����\\ˮ����ʧ�뱣��\\190823\\��ͼ1.mxd'
                mapping(fdir,tif,outjpeg,title,mxd_file=mxd)
            except:
                date = f.split('_')[4]
                year = date.split('-')[0]
                month = '%01d' % int(date.split('-')[1])
                # print(year,month)
                # exit()

                title = '{}��{}�����ɹ�������ֲ�����Ƕȷֲ�ͼ'.format(year, month)
                # # print(title.decode('gbk'))
                # # exit()
                # # title = ''
                tif = f
                outjpeg = outdir + title.decode('gbk')
                mxd = 'C:\\Users\\ly\\OneDrive\\��ʦ��\\�����\\ˮ����ʧ�뱣��\\190823\\��ͼ1.mxd'
                mapping(fdir, tif, outjpeg, title, mxd_file=mxd)
            # exit()
    pass


if __name__ == '__main__':
    mapping_annual()


