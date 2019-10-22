# coding=gbk
'''
author:Liyang
loc:CUG WuHan
origin version is programmed by DDC
date:20161204
description:ʹ��arcpy
            1�������ü�դ���ʸ��
            2��ͨ��arcgis����DateFrameģ��������ͼ
            3���������ΪJPEG
			4���ƶ��ļ��������ݷֱ��ƶ�������ļ��У����в��м���
               ԭ��Ϊ�ı�ͼ��Դ����·��
            ����������Ĺ��ܣ�
            1���ü�
            2���滻
            3����ͼ
            4���ָ�����
            5��ɾ���ļ����е�Ӣ�ĺ����ֱ��
            6�����м�����������
            7��������ɵ������Ƿ�����
            8���ϲ�����
            9���������ݣ������ɵĽ���ֱ�����ض����ļ��У�
            ע�⣺����·����ö��þ���·��
'''
import arcpy
import os
import time
import shutil
import re
from multiprocessing import Process
import logging
import winsound

files_to_be_clipped_zxhl = [
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_5y1_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_10y1_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_15y1_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_20y1_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_30y_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_50y_nowater_nodata_ex.tif",
           r"d:/project08/inundation_zxhl_tiff\zxhl_hbs_100y_nowater1_nodata_ex.tif",
           r'd:/project08/shuiti_shp\hbs_water.shp'#����ʡˮ��shp
           ]

files_to_be_clipped_shg=[
           r"d:/project08/inundation_shg_tiff\hebing_sh_5y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_10y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_15y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_20y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_30y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_50y_90m_nowater_pro.tif",
           r"d:/project08/inundation_shg_tiff\hebing_sh_100y_90m_nowater_pro.tif",
           r'd:/project08/shuiti_shp\hbs_water.shp'#����ʡˮ��shp
                        ]

files_to_be_clipped_dem=[r"d:/project08/DEM/hb-srtm-30m.tif"]#����ʡ��С����tif
shapefiles_zxhl=[r"d:/project08/zxhl_shp/������С�����������°汾1.shp"]#����ʡ��С����shp
shapefiles_shg=[r"d:/project08/shg_shp/ɽ��߽�-����-�޸�2.shp"]#����ʡɽ��shp

output_zxhl={
        "5��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_5y1_nowater_nodata_ex.tif"},
        "10��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_10y1_nowater_nodata_ex.tif"},
        "15��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_15y1_nowater_nodata_ex.tif"},
        "20��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_20y1_nowater_nodata_ex.tif"},
        "30��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_30y_nowater_nodata_ex.tif"},
        "50��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_50y_nowater_nodata_ex.tif"},
        "100��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_zxhl_hbs_100y_nowater1_nodata_ex.tif"}
            }

output_shg={
        "5��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_5y_90m_nowater_pro.tif"},
        "10��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_10y_90m_nowater_pro.tif"},
        "15��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_15y_90m_nowater_pro.tif"},
        "20��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_20y_90m_nowater_pro.tif"},
        "30��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_30y_90m_nowater_pro.tif"},
        "50��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_50y_90m_nowater_pro.tif"},
        "100��һ��������ˮ��û����ͼ.mxd":{"selected_border":"clip_lybj.shp",r"�߽�":"clip_lybj.shp","ˮ��":"clip_hbs_water.shp","��ûˮ��":"clip_hebing_sh_100y_90m_nowater_pro.tif"}
            }

def clip(dir,mode,dem=False):
    '''
    :param dir: �������Ŀ¼
    :return: None
    '''
    dir=dir+'_'+str(mode)
    if not os.path.exists(dir):
        os.mkdir(dir)
    if mode=='shg':
        shapefiles=shapefiles_shg
        basin=shapefiles[0]
        files_to_be_clipped=files_to_be_clipped_shg
        if dem==True:
            files_to_be_clipped=files_to_be_clipped_dem
    elif mode=='zxhl':
        shapefiles=shapefiles_zxhl
        basin=shapefiles[0]
        files_to_be_clipped=files_to_be_clipped_zxhl
        if dem==True:
            files_to_be_clipped=files_to_be_clipped_dem
    else:
        print 'mode error'
        basin=[]
        files_to_be_clipped=[]
        exit()

    if dem==True:
        dir=dir+'_dem'
    cur=arcpy.SearchCursor(basin)
    if mode=='zxhl':
        for row in cur:
            name=row.getValue('V_M_NAME')
            if name!='':
                print name
                geo=row.shape
                outdir = os.path.join(dir,name)
                print outdir
                if not os.path.exists(outdir):
                    os.mkdir(outdir)
                clip_lybj = os.path.join(outdir,'clip_lybj')
                #ʸ����ʸ��
                arcpy.Clip_analysis(basin,geo,clip_lybj)
                for file in files_to_be_clipped:
                    #������ļ���
                    basename = os.path.basename(file)
                    # print basename
                    #����ļ��ﶨ���������utf8��
                    # basename = basename.decode("utf-8")
                    newpath = "clip_" + basename
                    prefix = os.path.splitext(file)[1]
                    output = os.path.join(outdir,newpath)
                    print output
                    #����жϣ��ֱ����ü�shp��tif
                    if prefix == ".tif":
                        arcpy.Clip_management(file,"#",output,geo, "0", "ClippingGeometry")
                    if prefix == ".shp":
                        arcpy.Clip_analysis(file,geo,output)
    if mode=='shg':
        repeat_names=0
        for row in cur:
            name1=row.getValue('ʡ'.decode('gbk'))
            name=row.getValue('ɽ�鹵����'.decode('gbk'))
            if name1=='����'.decode('gbk'):
                # print name
                geo=row.shape
                outdir = os.path.join(dir,name)
                print outdir
                if not os.path.exists(outdir):
                    os.mkdir(outdir)

                #ʸ����ʸ��
                #��ֹ�����ظ��������֧��3��ͬ������
                try:
                    clip_lybj = os.path.join(outdir,"clip_lybj.shp")
                    arcpy.Clip_analysis(basin,geo,clip_lybj)
                except:
                    repeat_names+=1
                    print repeat_names,'error'
                    pass
                for file in files_to_be_clipped:
                    #������ļ���
                    basename = os.path.basename(file)
                    # print basename
                    #����ļ��ﶨ���������utf8��
                    # basename = basename.decode("utf-8")
                    newpath = "clip_" + basename
                    prefix = os.path.splitext(file)[1]
                    output = os.path.join(outdir,newpath)
                    print output
                    #����жϣ��ֱ����ü�shp��tif
                    if prefix == ".tif":
                        try:
                            arcpy.Clip_management(file,"#",output,geo, "0", "ClippingGeometry")
                        except:
                            print 'tiff error'
                            pass
                    if prefix == ".shp":
                        try:
                            arcpy.Clip_analysis(file,geo,output)
                        except:
                            print 'water shp error'
                            pass
        print repeat_names,'repeat'

def out_put(dir,mode):
    '''
    :param dir: ����·�����ü����Ŀ¼
    :return: None
    '''
    if mode=='shg':
        output=output_shg
    elif mode=='zxhl':
        output=output_zxhl
    else:
        output={}
        print 'mode error'
        exit()

    #��Ҫ����·��
    if mode=='zxhl':
        mxdfile='d:\project08\database\sample.mxd'#ģ���ļ�
    if mode=='shg':
        mxdfile='d:\project08\database\sample1.mxd'#ģ���ļ�
    else:
        mxdfile=''
        print 'mode eorror'
        exit()
    count=0
    listdir=os.listdir(dir)
    total=len(listdir)
    starttime=time.time()
    # print 'ޭ'
    # for i in listdir:
    #     print i.decode('gbk')
    #     print len(i)

    # logging.basicConfig(level=logging.DEBUG,
    #             format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #             datefmt='%a, %d %b %Y %H:%M:%S',
    #             filename=dir+'/loggggggg.log',
    #             filemode='w')
    for folders in os.listdir(dir):
        print folders.decode('gbk')
        count+=1
        currentdir=os.path.join(dir,folders)
        # isfile_flag=0
        # for key in output:
        #     if os.path.isfile(currentdir+'/'+key):
        #         isfile_flag+=1
        #         # print folders.decode('gbk'),'/',key.decode('gbk')[:-4],'\t file already exists'
        #     else:
        #         isfile_flag+=0
        # print isfile_flag
        # if isfile_flag!=7:
        if 1:
            mxd = arcpy.mapping.MapDocument (mxdfile)
            df0 = arcpy.mapping.ListDataFrames(mxd)[0]#��ͼ���
            df1 = arcpy.mapping.ListDataFrames(mxd)[1]#��ͼ���
            # print u'���ڴ���',folders.decode('gbk')
            #�޸ı���
            for key in output:
                starttime1=time.time()
                for textElement in arcpy.mapping.ListLayoutElements(mxd,"TEXT_ELEMENT"):
                    if textElement.name=='title':
                        if mode=='zxhl':
                            textElement.text=(folders+'������ˮ��û����ͼ')
                        elif mode=='shg':
                            textElement.text=(folders+'ɽ�鹵��ˮ��û����ͼ')
                    if textElement.name=='times':
                        #����ƥ��ʶ������
                        year=re.findall(r"[0-9]",key)
                        year_text=''
                        for figure in year:
                            year_text=year_text+figure
                        textElement.text=('��'+year_text+'��һ����')
                mxds=output[key]
                break_flag=0
                for layer in mxds:
                    #����դ���ʸ���ֱ�Ĺ�����
                    if '.tif' in output[key][layer]:
                        workplace="RASTER_WORKSPACE"
                    else:
                        workplace="SHAPEFILE_WORKSPACE"
                    #�滻��ͼͼ��
                    if layer != 'selected_border':
                        try:
                            lyr1=arcpy.mapping.ListLayers(mxd,layer,df1)[0]
                            lyr1.replaceDataSource(currentdir,workplace,output[key][layer][:-4])
                        except Exception as error:
                            # logging.warning(' main layer error. '+str(error)+' '+folders)
                            break_flag=1
                            pass
                    #�滻��ͼͼ��
                    else:
                        try:
                            lyr2=arcpy.mapping.ListLayers(mxd,layer,df0)[0]
                            lyr2.replaceDataSource(currentdir,workplace,output[key][layer][:-4])
                        except Exception as error:
                            # logging.warning(' sub_layer error. '+str(error)+' '+folders)
                            break_flag=1
                            pass
                #��ͼ����м�
                if break_flag==1:
                    break
                lyr_to_be_moved=arcpy.mapping.ListLayers(mxd,'��ûˮ��',df1)[0]
                df1.extent=lyr_to_be_moved.getSelectedExtent()

                mxd.saveACopy(currentdir+'/'+key,'9.2')

                arcpy.mapping.ExportToJPEG(mxd,currentdir+'/'+key,
                                           data_frame='PAGE_LAYOUT',
                                           df_export_width=mxd.pageSize.width,
                                           df_export_height=mxd.pageSize.height,
                                           resolution=500,jpeg_quality=100)
                print u'�����ɣ�',key.decode('gbk')[:-4]
                t=time.time()-starttime1
                print u'����'+folders.decode('gbk'),u'\t\t\t���ȣ�'+str(count)+'/'+str(total),u'\t\t\t�����:'+str(round(float(count)/total,4)*100)+'%'
                endtime=time.time()
                time_elapse=endtime-starttime
                total_time=t*total*7
                left_time=total_time+starttime-time.time()
                # print u'�ļ���  '+folders.decode('gbk'),'  '+str(count)+'/'+str(total),u' �����'+str(round(float(count)/total,4)*100)+'%'
                print u'������ʱ��',round(total_time/60,0),'min\t\t\t',u'����',round(time_elapse,0),'s\t\t\t',u'����ʣ��ʱ��',round(left_time/60,0),'min'
    # logging.info('done')
            # del mxd
        #�滻��ͼͼ��
        # for key in output_secondary:
        #     mxds=output_secondary[key]
        #     for layer in mxds:
        #         # print output_secondary[key][layer][:-4]
        #         lyr2=arcpy.mapping.ListLayers(mxd,layer,df0)[0]
        #         # # print lyr2.name
        #         # workplace="SHAPEFILE_WORKSPACE"
        #         # # print layer.decode('utf8')
        #         # # print (dir+folders).decode('gb18030')
        #         lyr2.replaceDataSource(currentdir.decode('gb18030'),workplace,output_secondary[key][layer][:-4])


#���м���
#�����и�
def distribute_folders(dir,dir_moved,num,if_copy):
    '''
    :param dir: ����Ŀ¼
    :param dir_moved: �����ƶ�������Ŀ¼
    :param num: �ָ���
    :return:
    '''
    #�����ļ�
    
    if if_copy==1:
        print 'copying files...'
        shutil.copytree(dir,dir+'_copy')
        print 'copy complete'
    #������ʱ�ļ���
    if not os.path.isdir(dir_moved):
        os.mkdir(dir_moved)
    else:
        print dir_moved,'is already exists, program exit :-)'
        exit()
    for i in range(num):
        temp_folders=os.path.join(dir_moved,'temp_path_'+str(i+1))
        if not os.path.isdir(temp_folders):
            os.mkdir(temp_folders)

    #��ʱ�ļ����б�
    temp_folders_list=os.listdir(dir_moved)
    folders_list=os.listdir(dir)
    folders_num=len(folders_list)
    folders_to_be_moved_times=int(round(folders_num/num,0))
    for i in range(num):
        folders_list=os.listdir(dir)
        for j in range(folders_to_be_moved_times):
            shutil.move(dir+'/'+folders_list[j],dir_moved+'/'+temp_folders_list[i])

    #�ƶ�ʣ�µ��ļ���
    rest_folders=os.listdir(dir)
    if len(rest_folders)>0:
        os.mkdir(dir_moved+'/'+'temp_path_'+str(num+1))
        folders_list=os.listdir(dir)
        folders_num=len(folders_list)
        for i in range(folders_num):
            shutil.move(dir+'/'+folders_list[i],dir_moved+'/'+'temp_path_'+str(num+1))
    os.rmdir(dir)

#���ɲ����ļ���
def make_dir(dir,num):
    if not os.path.isdir(dir):
        os.mkdir(dir)
    for i in range(num):
        temp_folders=os.path.join(dir,'temp_path_'+str(i+1))
        if not os.path.isdir(temp_folders):
            os.mkdir(temp_folders)

def re_name(dir):
    '''
    �������ļ��У�ɾ���ļ����е�Ӣ��
    :param dir: ����Ŀ¼
    :return:
    '''
    folder_list=os.listdir(dir)
    k=0
    for folder in folder_list:
        # print folder
        #����ƥ�人��
        name_list=re.findall(r'[\x80-\xff]',folder)
        new_name=''
        for i in name_list:
            new_name=new_name+i
        # print '*'*30
        try:
            os.rename(os.path.join(dir,folder),os.path.join(dir,new_name))
            pass
        except:
            k+=1
            os.rename(os.path.join(dir,folder),os.path.join(dir,new_name+str(k)))

def examine():
    '''
    �����ʱ�ļ��С�temp_distribute���е��ļ��Ƿ񶼳ɹ���ͼ
    :param dir_temp_list:
    :return:
    '''
    temp_lists=os.listdir('d:/project08/temp_distribute')
    for i in temp_lists:
        temp_list=os.listdir('d:/project08/temp_distribute'+'/'+i)
        for j in temp_list:
            li=os.listdir('d:/project08/temp_distribute'+'/'+i+'/'+j)
            if len(li)!=75:
                print i+'\t'+j.decode('gbk')
                shutil.move('d:/project08/temp_distribute/'+i+'/'+j,'d:/project08/error')

def delete_temp_path(path='d:/project08/temp_distribute',destination_folder='d:/project08/temp_distribute/product'):
    '''
    ��temp_distribute�е��ļ��л��ܵ�һ���ļ���
    :param path:
    :param destination_folder:
    :return:
    '''
    temp_path=os.listdir(path)
    print temp_path
    if not os.path.isdir(os.path.join(path,destination_folder)):
        os.mkdir(os.path.join(path,destination_folder))
    for temp_list in temp_path:
        # print folder
        temp=os.listdir(os.path.join(path,temp_list))
        # print temp
        print temp_list
        for folders in temp:
            print folders
            shutil.move(os.path.join(path,temp_list,folders),os.path.join(path,'product'))
            print os.path.join(path,temp_list,folders)


def move_tif_to_folders(dir):
    '''
    ��5,10,15,20.������tif�ֱ��ƶ��������ļ�����
    :param dir:
    :return:
    '''
    dir_list=os.listdir(dir)
    for folder in dir_list:
        file_list=os.listdir(os.path.join(dir,folder))
        # print file_list
        for file in file_list:
            if '100y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'100')):
                    os.mkdir(os.path.join(dir,folder,'100'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'100'))
            elif '50y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'50')):
                    # print os.path.join(dir,folder,'50')
                    os.mkdir(os.path.join(dir,folder,'50'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'50'))
            elif '30y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'30')):
                    # print os.path.join(dir,folder,'30')
                    os.mkdir(os.path.join(dir,folder,'30'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'30'))
            elif '20y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'20')):
                    # print os.path.join(dir,folder,'20')
                    os.mkdir(os.path.join(dir,folder,'20'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'20'))
            elif '15y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'15')):
                    # print os.path.join(dir,folder,'15')
                    os.mkdir(os.path.join(dir,folder,'15'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'15'))
            elif '10y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'10')):
                    # print os.path.join(dir,folder,'10')
                    os.mkdir(os.path.join(dir,folder,'10'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'10'))
            elif '5y' in file:
                if not os.path.isdir(os.path.join(dir,folder,'5')):
                    # print os.path.join(dir,folder,'5')
                    os.mkdir(os.path.join(dir,folder,'5'))
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'5'))
            elif file == "5��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'5')):
                    os.mkdir(os.path.join(dir,folder,'5'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'5'))
            elif file == "10��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'10')):
                    os.mkdir(os.path.join(dir,folder,'10'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'10'))
            elif file == "15��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'15')):
                    os.mkdir(os.path.join(dir,folder,'15'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'15'))
            elif file == "20��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'20')):
                    os.mkdir(os.path.join(dir,folder,'20'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'20'))
            elif file == "30��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'30')):
                    os.mkdir(os.path.join(dir,folder,'30'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'30'))
            elif file == "50��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'50')):
                    os.mkdir(os.path.join(dir,folder,'50'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'50'))
            elif file == "100��һ��������ˮ��û����ͼ.jpg":
                if not os.path.isdir(os.path.join(dir,folder,'100')):
                    os.mkdir(os.path.join(dir,folder,'100'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'100'))
            elif "lybj" in file:
                if not os.path.isdir(os.path.join(dir,folder,'��������')):
                    os.mkdir(os.path.join(dir,folder,'��������'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'��������'))
            elif "water" in file:
                if not os.path.isdir(os.path.join(dir,folder,'��������')):
                    os.mkdir(os.path.join(dir,folder,'��������'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'��������'))
            elif ".mxd" in file:
                if not os.path.isdir(os.path.join(dir,folder,'��������')):
                    os.mkdir(os.path.join(dir,folder,'��������'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'��������'))
            elif "30m" in file:
                if not os.path.isdir(os.path.join(dir,folder,'��������')):
                    os.mkdir(os.path.join(dir,folder,'��������'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'��������'))
            elif "DEM" in file:
                if not os.path.isdir(os.path.join(dir,folder,'��������')):
                    os.mkdir(os.path.join(dir,folder,'��������'))
                # print file.decode('gbk')
                shutil.move(os.path.join(dir,folder,file),os.path.join(dir,folder,'��������'))

#���м���
def concurrent_run(mode):
    temp_folder_list=os.listdir('d:/project08/temp_distribute/')
    for i in temp_folder_list:
        print i
        p=Process(target=out_put,args=('d:/project08/temp_distribute/'+i,mode,))
        p.start()

if __name__ == '__main__':
    clip('d:/project08/clipped','zxhl',dem=False)
    #re_name('d:/project08/test2')
    #distribute_folders('d:/project08/clipped_shg','d:/project08/temp_distribute',13,1)
    #winsound.Beep(2000,1000)
    #concurrent_run('shg')
    #examine()
    #winsound.Beep(2000,1000)
    #delete_temp_path()
    #move_tif_to_folders('d:/project08/product_zxhl')
