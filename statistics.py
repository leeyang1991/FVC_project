# coding=gbk
import to_raster
import os
from matplotlib import pyplot as plt
import time
from tqdm import tqdm
import seaborn as sns
import numpy as np
import matplotlib.colors as col
import matplotlib.cm as cm

this_root = os.getcwd()+'\\..\\'

plt.rcParams['font.sans-serif'] = 'SimHei'
def quanqu():
    fdir = this_root+'1km年值_1978_1985_1995_2005_2018\\'
    fdir = fdir.decode('gbk')
    flist = os.listdir(fdir)
    fw = open('quanqu.csv','w')
    for f in flist:
        if f.endswith('.tif'):
                    # a = a.decode('gbk')
            print(f)
            # print(a.decode('gbk'))
            # exit()
            array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
            # plt.imshow(array)
            # plt.colorbar()
            # plt.show()
            fenmu = 0.
            gao = 0.
            zhonggao = 0.
            zhong = 0.
            zhongdi = 0.
            di = 0.
            for i in range(len(array)):
                for j in range(len(array[0])):
                    val = array[i][j]
                    if 0<=val<=100:
                        fenmu += 1.
                        if 75<val<=100:
                            gao+=1.
                        elif 60<val<=75:
                            zhonggao+=1.
                        elif 45<val<=60:
                            zhong+=1.
                        elif 30<val<=45:
                            zhongdi+=1.
                        elif 0<=val<=30:
                            di+=1.
                        else:
                            print(val)
            gao_ratio = round(gao/fenmu,4)*100.
            zhonggao_ratio = round(zhonggao/fenmu,4)*100.
            zhong_ratio = round(zhong/fenmu,4)*100.
            zhongdi_ratio = round(zhongdi/fenmu,4)*100.
            di_ratio = round(di/fenmu,4)*100.

            a = '1978年内蒙古植被高覆盖区面积为{}平方千米，占全区总面积比例为{}%，\n' \
                '1978年内蒙古植被中高覆盖区面积为{}平方千米，占全区总面积比例为{}%，\n' \
                '1978年内蒙古植被中覆盖区面积为{}平方千米，占全区总面积比例为{}%，\n' \
                '1978年内蒙古植被中低覆盖区面积为{}平方千米，占全区总面积比例为{}%，\n' \
                '1978年内蒙古植被低覆盖区面积为{}平方千米，占全区总面积比例为{}%'\
                .format(gao,gao_ratio,
                        zhonggao,zhonggao_ratio,
                        zhong,zhong_ratio,
                        zhongdi,zhongdi_ratio,
                        di,di_ratio)
            b='{:.0f}\n'*5
            c=b.format(gao,zhonggao,zhong,zhongdi,di)
            print(c)
            # fw.write()
            # print(a.decode('gbk'))


def fenqu():
    fdir = 'E:\\FVC内蒙古植被覆盖数据\\1km年值_1978_1985_1995_2005_2018_clipped\\'.decode('gbk')
    shp_name = ['北方风沙区', '北方土石山区', '东北黑土区', '西北黄土高原区']
    flist = os.listdir(fdir)
    fw = open(this_root+'result.csv','w')
    for f in flist:
        if f.endswith('.tif'):
            # print(f.decode('gbk'))

            zone = f.split('_')[-1].split('.')[0].encode('gbk')
            year = f.split('_')[1].split('.')[0]
            # print(year)
            # exit()
            # print(zone)
            array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir + f)
            # plt.imshow(array)
            # plt.colorbar()
            # plt.show()
            fenmu = 0.
            gao = 0.
            zhonggao = 0.
            zhong = 0.
            zhongdi = 0.
            di = 0.
            for i in range(len(array)):
                for j in range(len(array[0])):
                    val = array[i][j]
                    if 0 <= val <= 100:
                        fenmu += 1.
                        if 75 < val <= 100:
                            gao += 1.
                        elif 60 < val <= 75:
                            zhonggao += 1.
                        elif 45 < val <= 60:
                            zhong += 1.
                        elif 30 < val <= 45:
                            zhongdi += 1.
                        elif 0 <= val <= 30:
                            di += 1.
                        else:
                            print(val)
            gao_ratio = round(gao / fenmu, 4) * 100.
            zhonggao_ratio = round(zhonggao / fenmu, 4) * 100.
            zhong_ratio = round(zhong / fenmu, 4) * 100.
            zhongdi_ratio = round(zhongdi / fenmu, 4) * 100.
            di_ratio = round(di / fenmu, 4) * 100.

            gao = int(gao)
            zhonggao = int(zhonggao)
            zhong = int(zhong)
            zhongdi = int(zhongdi)
            di = int(di)


            a = '{}年内蒙古{}植被高覆盖区面积为{}平方千米，占全区总面积比例为{}%；' \
                '植被中高覆盖区面积为{}平方千米，占全区总面积比例为{}%；' \
                '植被中覆盖区面积为{}平方千米，占全区总面积比例为{}%；' \
                '植被中低覆盖区面积为{}平方千米，占全区总面积比例为{}%；' \
                '植被低覆盖区面积为{}平方千米，占全区总面积比例为{}%。' \
                .format(year,zone,gao, gao_ratio,
                        zhonggao, zhonggao_ratio,
                        zhong, zhong_ratio,
                        zhongdi, zhongdi_ratio,
                        di, di_ratio)
            b = '{},'*12
            c = b.format(year,zone,gao, gao_ratio,
                        zhonggao, zhonggao_ratio,
                        zhong, zhong_ratio,
                        zhongdi, zhongdi_ratio,
                        di, di_ratio)
            print(a.decode('gbk'))
            fw.write(','.join(c.split(',')[2:])+'\n')
            # print('\n')

def plot_year_hist():
    fdir = this_root + '1km月值_1978_1985_1995_2005_2018\\'
    fdir = fdir.decode('gbk')
    flist = os.listdir(fdir)
    flag = 0
    # plt.figure(figsize=(5,25))
    flag = 0
    for f in flist:

        if f.endswith('.tif'):
            # flag+=1
            if not '-08-01_' in f:
                continue
            flag += 1
            # a = a.decode('gbk')
            print(f)
            year = f.split('_')[1].split('.')[0]
            array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir + f)
            hist = []
            for i in range(len(array)):
                for j in range(len(array[0])):
                    val = array[i][j]
                    if 0 <= val <= 100:
                        hist.append(val)
            plt.subplot(1,5,flag)
            plt.hist(hist,bins=40,normed=1)
            plt.title(year)
            if flag == 5:
                break
            # plt.xticks([])
            # plt.yticks([]
    plt.show()
    # plt.savefig(this_root+'year_hist.png',dpi=300)


def plot_month_hist():
    fdir = this_root + '1km月值_1978_1985_1995_2005_2018\\'
    fdir = fdir.decode('gbk')
    flist = os.listdir(fdir)
    for year in ['1978','1985','1995','2005','2018']:
        plt.figure(figsize=(3*4, 4*4))
        flag = 0
        for f in flist:
            if year in f:
                if f.endswith('.tif'):
                    print(f)
                    # flag += 1
                    # a = a.decode('gbk')
                    if not '2005' in f:
                        mon = f.split('_')[-3]
                        # print(mon)
                    else:
                        mon = f.split('_')[-2]
                        # print(mon)
                    array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir + f)
                    hist = []
                    for i in range(len(array)):
                        for j in range(len(array[0])):
                            val = array[i][j]
                            if 0 <= val <= 100:
                                hist.append(val)
                    flag+=1
                    plt.subplot(4,3,flag)
                    plt.hist(hist,bins=40,normed=1)
                    plt.title(mon)
        plt.savefig(this_root+year+'.png',dpi=300)


def classify_arr(arr):
    # 按照值的范围分级
    classified = []
    for i in arr:
        temp = []
        for j in i:
            if 0<=j<30:
                temp.append(1)
            elif 30<=j<45:
                temp.append(2)
            elif 45<=j<60:
                temp.append(3)
            elif 60<=j<75:
                temp.append(4)
            elif 75<=j<=100:
                temp.append(5)
            else:
                temp.append(np.nan)
        classified.append(temp)
    classified = np.array(classified)
    return classified
    # plt.imshow(classified)
    # plt.colorbar()
    # plt.show()
    pass


def plot_fenqu():
    fdir = 'E:\\FVC内蒙古植被覆盖数据\\30m年值_1978_1985_1995_2005_2018_clipped\\'.decode('gbk')
    outdir = this_root+'png\\'
    if not os.path.isdir(outdir):
        os.makedirs(outdir)
    shp_name = ['北方风沙区', '北方土石山区', '东北黑土区', '西北黄土高原区']

    flist = os.listdir(fdir)


    for y in ['1978','1985','1995','2005','2018']:
        arrs = []
        names = []
        for z in shp_name:
            for f in flist:
                if f.endswith('.tif'):
                    zone = f.split('_')[-1].split('.')[0].encode('gbk')
                    year = f.split('_')[1].split('.')[0]
                    if zone == z and y == year:
                        array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
                        arrs.append(array)
                        names.append(z.decode('gbk'))

        fig, axs = plt.subplots(2, 2, figsize=(9,7))

        images = []
        flag = 0
        for i in range(2):
            for j in range(2):
                arr = arrs[flag]
                # classified = classify_arr(arr)
                # exit()
                arr = np.ma.masked_where(arr>120,arr)
                # sns.
                # plt.imshow()
                cmap = ["#734e00", "#a87001", "#effa91", "#b1cc63", "#5d8c22"]
                cmap_ = col.LinearSegmentedColormap.from_list('mycol',cmap)
                cm.register_cmap(cmap=cmap_)
                images.append(axs[i,j].imshow(arr, cmap='mycol',vmin=0,vmax=100))
                # images.append(axs[i, j].imshow(arr,'jet'))
                axs[i, j].set_title(names[flag])
                axs[i,j].set_xticks([])
                axs[i,j].set_yticks([])
                # fig.yticks([])
                # fig.yticks([])
                flag += 1
        fig.suptitle(y+'年内蒙古4大区域植被盖度(%)'.decode('gbk'))
        fig.colorbar(images[0], ax=axs, orientation='horizontal', shrink=0.7, pad=0.05)
        plt.show()
        # plt.savefig(outdir+y+'.png',dpi=300)
    pass


def plot_quanqu_bar():
    import pandas as pd
    a= '''297059	296596	327189	265034	283585
148351	161112	165875	168986	186943
180850	159202	178877	176705	165491
133059	174936	179605	165993	158746
386778	354251	294551	369379	351332'''
    a = a.split('\n')
    data = []
    for i in a:
        i=i.split('\t')
        # data.append(int(i))
        temp = []
        for d in i:
            temp.append(int(d))
        data.append(temp)
    df = pd.DataFrame(data)
    print(df)
    # sns.color_palette()
    # cmap = ["#734e00", "#a87001", "#effa91", "#b1cc63", "#5d8c22"]
    cmap = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
    colors = ["windows blue", "amber", "greyish", "faded green", "dusty purple"]
    flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    labels = ['1978','1985','1995','2005','2018']
    cmap = sns.color_palette('RdBu_r', 5)
    # cmap = cmap*5
    # cmap = sns.xkcd_palette(colors)
    width = 0.15
    for i in df:
        plt.bar(np.array(range(len(df[i])))+width*i, df[i],width=width,color=cmap[-(i+1)],label=labels[i])
    plt.legend()
    # plt.figure()
    # for i in df:
    #     print(df[i])
    #     plt.bar(np.array(range(len(df[i])))+i+8,df[i])
    # plt.show()
    # df.plot()
    plt.show()
    # print(df)


def plot_quanqu_line():
    import pandas as pd
    a= '''297059	296596	327189	265034	283585
148351	161112	165875	168986	186943
180850	159202	178877	176705	165491
133059	174936	179605	165993	158746
386778	354251	294551	369379	351332'''
    a = a.split('\n')
    data = []
    for i in a:
        i=i.split('\t')
        # data.append(int(i))
        temp = []
        for d in i:
            temp.append(int(d))
        data.append(temp)
    df = pd.DataFrame(data)
    # print(df)
    # colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    cmap = sns.color_palette('dark', 5)
    # plt.plot(df.T,c = colors)
    for i in df.T:
        # print(df.T)
        print(cmap[i])
        plt.plot(df.T[i],c=cmap[i])
        plt.scatter(range(len(df.T)),df.T[i],c=cmap[i])
    plt.show()
    # print(df)



def cal_quanqu_bar(a):
    import pandas as pd
#     a = '''259648	267767	277325	245180	255787
# 74339	85311	54733	80296	78527
# 51455	32174	42929	40458	37221
# 796	636	10809	17935	12792
# 1214	1564	1656	3583	3125'''
    a = a.split('\n')
    data = []
    for i in a:
        i = i.split('\t')
        # data.append(int(i))
        temp = []
        for d in i:
            temp.append(int(d))
        data.append(temp)
    df = pd.DataFrame(data).T
    year_list = [1978,1985,1995,2005,2018]
    for i in df:
        vals = df[i]
        print_val = []
        for v in range(len(vals)):
            if v+1 == 5:
                print_val.append(str(round((vals[4]-vals[0])/float(vals[v])*100,2)))
                break
            # print(year_list[v],year_list[v+1])
            print_val.append(str(round((vals[v+1]-vals[v])/float(vals[v])*100,2)))
        # exit()
        print('\t'.join(print_val))
        # print('********')

    # print(df)


def plot_fenqu_line(a,title):
    import pandas as pd
#     a = '''259648	267767	277325	245180	255787
# 74339	85311	54733	80296	78527
# 51455	32174	42929	40458	37221
# 796	636	10809	17935	12792
# 1214	1564	1656	3583	3125
#
# '''
    a = a.split('\n')
    print(a)
    data = []
    for i in a:
        i=i.split('\t')
        temp = []
        # print(i)
        if len(i) < 5:
            continue
        for d in i:
            # print(d)
            temp.append(int(d))
        data.append(temp)
    df = pd.DataFrame(data)
    print(df)
    # exit()
    # colors = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
    cmap = sns.color_palette('dark', 5)
    zone = ['高植被覆盖区'.decode('gbk'),
            '中高植被覆盖区'.decode('gbk'),
            '中植被覆盖区'.decode('gbk'),
            '中低植被覆盖区'.decode('gbk'),
            '低被覆盖区'.decode('gbk')
            ]
    # plt.plot(df.T,c = colors)
    # axs = []
    for i in df.T:
        # print(df.T)
        # print(cmap[i])
        plt.plot(df.T[i]/10000,c=cmap[i],label=zone[i])
        # axs.append(ax)
        # plt.scatter(range(len(df.T)),df.T[i],c=cmap[i])
    plt.ylabel('面积（km2）'.decode('gbk'))
    plt.xticks(range(5),['1978','1985','1995','2005','2018'])
    # plt.yticks([0,100000,200000,300000,400000],['0','10','20','30','40'])
    plt.legend()
    plt.title(title)
    for i in df.T:
        plt.scatter(range(len(df.T)),df.T[i]/10000,c=cmap[i])

    plt.show()
    # print(df)


if __name__ == '__main__':
    a='''940	1186	2284	2816	3555
5009	6295	15621	17611	20693
20137	27319	29397	30305	33606
39051	52719	62176	52383	51881
74747	52365	30406	36769	30149'''
    cal_quanqu_bar(a)

    pass