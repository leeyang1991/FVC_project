# coding=gbk
import os
import arcpy
import time
import codecs

this_root = os.getcwd()+'\\..\\'


def mk_dir(dir):
    if not os.path.isdir(dir):
        os.makedirs(dir)


def mapping(current_dir,tif,outjpeg,title,mxd_file):

    mxd = arcpy.mapping.MapDocument(mxd_file)
    df0 = arcpy.mapping.ListDataFrames(mxd)[0]

    workplace = "RASTER_WORKSPACE"

    lyr = arcpy.mapping.ListLayers(mxd, 'tif', df0)[0]
    lyr.replaceDataSource(current_dir,workplace,tif)

    for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if textElement.name == 'title':
            textElement.text = (title)

    arcpy.mapping.ExportToJPEG(mxd,outjpeg,data_frame='PAGE_LAYOUT',df_export_width=mxd.pageSize.width,df_export_height=mxd.pageSize.height,color_mode='24-BIT_TRUE_COLOR',resolution=300,jpeg_quality=100)



def mapping_annual():
    fdir = r'D:\FVC\FVC_1km_new\fusion_int_0-100\\'
    outdir = r'D:\FVC\图报告\30m_年_fusion\\'
    mk_dir(outdir)
    mxd = r'C:\Users\ly\OneDrive\北师大\雷添杰\水土流失与保持\190823\内蒙古制图模板.mxd'

    mk_dir(outdir)
    flist = os.listdir(fdir)

    # name_dic = {'1.tif':'1978-1985','2.tif':'1985-1995','3.tif':'1995-2005','4.tif':'2005-2018'}
    for f in flist:
        # if f.endswith('.tif') and not '_2005-' in f:

        if f.endswith('.tif'):
            print(f)
            # year = name_dic[f]
            # year = f.split('.')[0].split('fvc')[1]
            year = f.split('.')[0]
            # exit()
            # year = f.split('_')[1].split('.')[0]
            # print(year)
            title = '{}年内蒙古自治区植被覆盖度图'.format(year)
            print(title.decode('gbk'))
            # exit()
            # title = ''
            tif = f
            outjpeg = outdir.decode('gbk') + title.decode('gbk')

            mapping(fdir, tif, outjpeg, title, mxd_file=mxd)


def mapping_fenqu4(year,title_year):
    fdir = r'E:\FVC内蒙古植被覆盖数据\30m月值出图\\'.decode('gbk')
    outdir = r'D:\FVC\图图集\4分区\\'.decode('gbk')
    mk_dir(outdir)
    mxd = r'C:\Users\ly\OneDrive\北师大\雷添杰\水土流失与保持\190823\分区出图.mxd'

    mxd = arcpy.mapping.MapDocument(mxd)
    df = [0,1,2,3]
    shp_name = ['北方风沙区', '北方土石山区', '东北黑土区', '西北黄土高原区']
    # fname_pre = ['1.tif_','2.tif_','3.tif_','4.tif_']
    fname_pre = year
    # print(fname_pre)

    # title_year = ['1978-1985','1985-1995','1995-2005','2005-2018']
    title = '{}年内蒙古自治区植被覆盖变化'.format(title_year)
    for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if textElement.name == 'title':
            textElement.text = (title)

    outjpeg = outdir + title.decode('gbk') + '.jpg'

    for i in df:
        # print(i)
        df0 = arcpy.mapping.ListDataFrames(mxd)[i]
        tif = fname_pre+shp_name[i]+'.tif'
        print(tif.decode('gbk'))
        workplace = "RASTER_WORKSPACE"


        lyr = arcpy.mapping.ListLayers(mxd, 'tif', df0)[0]
        print(fdir)
        # print(workplace)
        print(tif.decode('gbk'))
        lyr.replaceDataSource(fdir, workplace, tif)

    # mxd.saveACopy(outdir + '\\mxd.mxd', '9.2')
    arcpy.mapping.ExportToJPEG(mxd, outjpeg, data_frame='PAGE_LAYOUT', df_export_width=mxd.pageSize.width,
                               df_export_height=mxd.pageSize.height, color_mode='24-BIT_TRUE_COLOR', resolution=300,
                               jpeg_quality=100)



def mapping_nongmu(tif_list,title):
    fdir = r'D:\FVC\nongmu\clipped\\'
    outdir = r'D:\FVC\图图集\农牧交错带\\'
    mk_dir(outdir)
    mxd = r'C:\Users\ly\OneDrive\北师大\雷添杰\水土流失与保持\190823\分区出图_nongmu.mxd'

    mxd = arcpy.mapping.MapDocument(mxd)
    df = [0,1,2]
    shp_name = ['内蒙古草地', '鄂尔多斯市', '内蒙古农牧交错带']
    # fname_pre = ['1.tif_','2.tif_','3.tif_','4.tif_']
    # fname_pre = year
    # print(fname_pre)

    # title_year = ['1978-1985','1985-1995','1995-2005','2005-2018']
    # title = '{}年内蒙古自治区植被覆盖分布'.format(year)
    # title = '{}年内蒙古自治区植被覆盖变化'.format(year)
    for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if textElement.name == 'title':
            textElement.text = (title)

    outjpeg = outdir + title + '.jpg'

    for i in df:
        # print(i)
        df0 = arcpy.mapping.ListDataFrames(mxd)[i]
        # tif = fname_pre+shp_name[i]+'.tif'
        tif = tif_list[i]
        workplace = "RASTER_WORKSPACE"


        lyr = arcpy.mapping.ListLayers(mxd, 'tif', df0)[0]
        print(fdir)
        # print(workplace)
        print(tif.decode('gbk'))
        lyr.replaceDataSource(fdir, workplace, tif)

    # mxd.saveACopy(outdir + '\\mxd.mxd', '9.2')
    arcpy.mapping.ExportToJPEG(mxd, outjpeg, data_frame='PAGE_LAYOUT', df_export_width=mxd.pageSize.width,
                               df_export_height=mxd.pageSize.height, color_mode='24-BIT_TRUE_COLOR', resolution=300,
                               jpeg_quality=100)




def rename():
    fdir = r'D:\FVC\nongmu\30m_substractclipped\\'
    for f in os.listdir(fdir):
        pre = f.split('_')[-2]
        replace_pre = pre.replace('.tif','')
        new = replace_pre+'_'+f.split('_')[-1]
        print(new.decode('gbk'))
        os.rename(fdir+f,fdir+new)



def mapping_zhongdian(year,title_year):
    fdir = r'D:\FVC\重点区域范围\30m_fenqu_clipped\\'
    outdir = r'D:\FVC\图图集\重点\\'
    mk_dir(outdir)
    mxd = r'C:\Users\ly\OneDrive\北师大\雷添杰\水土流失与保持\190823\分区出图_zhongdian.mxd'

    mxd = arcpy.mapping.MapDocument(mxd)
    df = [0,1,2,3]
    shp_name = ['太行山山地丘陵区', '宁蒙覆沙黄土丘陵区', '晋陕蒙丘陵沟壑区', '燕山及辽西山地丘陵区']
    # fname_pre = ['1.tif_','2.tif_','3.tif_','4.tif_']
    fname_pre = year+'_'
    print(fname_pre)

    # title_year = ['1978-1985','1985-1995','1995-2005','2005-2018']
    title = title_year
    for textElement in arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT"):
        if textElement.name == 'title':
            textElement.text = (title)

    outjpeg = outdir + title + '.jpg'

    for i in df:
        # print(i)
        df0 = arcpy.mapping.ListDataFrames(mxd)[i]
        tif = fname_pre+shp_name[i]+'.tif'
        workplace = "RASTER_WORKSPACE"


        lyr = arcpy.mapping.ListLayers(mxd, 'tif', df0)[0]
        print(fdir)
        # print(workplace)
        print(tif.decode('gbk'))
        lyr.replaceDataSource(fdir, workplace, tif)

    # mxd.saveACopy(outdir + '\\mxd.mxd', '9.2')
    arcpy.mapping.ExportToJPEG(mxd, outjpeg, data_frame='PAGE_LAYOUT', df_export_width=mxd.pageSize.width,
                               df_export_height=mxd.pageSize.height, color_mode='24-BIT_TRUE_COLOR', resolution=300,
                               jpeg_quality=100)



def do_mapping_monthly():

    fdir = 'E:\\FVC内蒙古植被覆盖数据\\30m月值_1978_1985_1995_2005_2018\\'.decode('gbk')
    outdir = 'D:\\FVC\\图集\\30m_月\\'.decode('gbk')
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
                mxd = 'C:\\Users\\ly\\OneDrive\\北师大\\雷添杰\\水土流失与保持\\190823\\出图2.mxd'
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
                mxd = 'C:\\Users\\ly\\OneDrive\\北师大\\雷添杰\\水土流失与保持\\190823\\出图2.mxd'
                mapping(fdir, tif, outjpeg, title, mxd_file=mxd)
            # exit()
    pass


def mapping_substract_nongmu():

    tif_list = []
    shp_name = ['内蒙古草地', '鄂尔多斯市', '内蒙古农牧交错带']
    title_year = ['1978-1985', '1985-1995', '1995-2005', '2005-2018']
    year_list = [1,2,3,4]
    for year in year_list:
        one_year = []
        for sn in shp_name:
            fname = str(year)+'_'+sn+'.tif'
            # print(fname.decode('gbk'))
            one_year.append(fname)
        tif_list.append(one_year)
    for i in range(len(tif_list)):
        mapping_nongmu(tif_list[i],'{}年内蒙古自治区植被覆盖变化'.format(title_year[i]))


def do_mapping_zhongdian():
    tif_list = []
    shp_name = ['太行山山地丘陵区', '宁蒙覆沙黄土丘陵区', '晋陕蒙丘陵沟壑区', '燕山及辽西山地丘陵区']

    year_list = ['1978','1985','1995','2005','2018']
    # year_list = ['1','2','3','4']
    # title_list = ['1978-1985', '1985-1995', '1995-2005', '2005-2018']
    for year in year_list:
        one_year = []
        for sn in shp_name:
            fname = str(year) + '_' + sn + '.tif'
            # print(fname.decode('gbk'))
            one_year.append(fname)
        tif_list.append(one_year)
    # print(tif_list)
    # for i in tif_list:
    #     for j in i:
    #         print(j.decode('gbk'))
    for i in range(len(tif_list)):
        # mapping_zhongdian(year_list[i],'{}年内蒙古自治区植被覆盖变化'.format(year_list[i]))
        mapping_zhongdian(year_list[i],'{}年内蒙古自治区植被覆盖分布图'.format(year_list[i]))

def do_mapping_nongmu():
    year = ['1978', '1985', '1995', '2005', '2018']
    shp = ['内蒙古草地', '鄂尔多斯市', '内蒙古农牧交错带']

    for y in year:
        tif_list = []
        for s in shp:
            tif = y + '_' + s + '.tif'
            tif_list.append(tif)
        title = '{}年内蒙古自治区植被覆盖分布图'.format(y)
        mapping_nongmu(tif_list, title)

def do_mapping_4fenqu():
    year = ['1978', '1985', '1995', '2005', '2018']
    for y in year:

        mapping_fenqu4(y, y)


if __name__ == '__main__':
    mapping_annual()
    # fname_pre = ['1_','2_','3_','4_']
    # title_year = ['1978-1985','1985-1995','1995-2005','2005-2018']
    # for i in range(len(fname_pre)):
    #     mapping_fenqu4(fname_pre[i],title_year[i])
    #     # break
    # do_mapping_zhongdian()
    # mapping_annual()
    # do_mapping_monthly()
    # year = '2018'
    # title_year = year

    # do_mapping_zhongdian()
    # do_mapping_nongmu()
    # do_mapping_4fenqu()
    pass