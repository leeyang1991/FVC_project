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

# this_root = os.getcwd()+'\\..\\'

plt.rcParams['font.sans-serif'] = 'SimHei'
def quanqu():
    fdir = r'D:\FVC\FVC_1km_new\FVC-year_1km_clipped\\'
    # fdir = fdir.decode('gbk')
    flist = os.listdir(fdir)
    fw = open(fdir+'quanqu.csv','w')
    for f in flist:
        if f.endswith('.tif'):
            # print(f)
            year = f.split('.')[0].split('fvc')[1]

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
                    val = array[i][j]*100
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

            a = '{}年内蒙古植被高覆盖区面积为{}平方千米，占全区总面积比例为{}%，' \
                '植被中高覆盖区面积为{}平方千米，占全区总面积比例为{}%，' \
                '植被中覆盖区面积为{}平方千米，占全区总面积比例为{}%，' \
                '植被中低覆盖区面积为{}平方千米，占全区总面积比例为{}%，' \
                '植被低覆盖区面积为{}平方千米，占全区总面积比例为{}%'\
                .format(year,gao,gao_ratio,
                        zhonggao,zhonggao_ratio,
                        zhong,zhong_ratio,
                        zhongdi,zhongdi_ratio,
                        di,di_ratio)
            b='{},'*5
            c=b.format(gao,zhonggao,zhong,zhongdi,di)
            # print(c)
            print(a.decode('gbk'))
            fw.write(','.join(c.split(',')) + '\n')
            # fw.write()
            # print(a.decode('gbk'))


def fenqu():
    # fdir = r'D:\FVC\FVC_1km_new\4fenqu\\'.decode('gbk')
    # fdir = r'D:\FVC\重点区域范围\1km_fenqu_clipped\\'.decode('gbk')
    fdir = r'E:\FVC内蒙古植被覆盖数据\FVC_D\重点1\1km_clipped\\'.decode('gbk')
    # shp_name = ['北方风沙区', '北方土石山区', '东北黑土区', '西北黄土高原区']
    # shp_name = ['太行山山地丘陵区', '宁蒙覆沙黄土丘陵区', '晋陕蒙丘陵沟壑区', '燕山及辽西山地丘陵区']
    # shp_name = ['内蒙古草地', '鄂尔多斯市', '内蒙古农牧交错带']
    shp_name = ['赤峰市', '鄂尔多斯', '通辽市', '准格尔旗']
    flist = os.listdir(fdir)
    fw = open(fdir+'result_.csv','w')
    for f in flist:
        if f.endswith('.tif'):
            # print(f.decode('gbk'))

            zone = f.split('_')[-1].split('.')[0].encode('gbk')
            # year = f.split('_')[0].split('fvc')[1]
            year = f.split('_')[0]
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
            # plt.imshow(array)
            # plt.show()
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
    a= '''263484	104980	162749	135401	479571
252464	101426	161515	127550	503230
284295	105873	143990	134244	477783
356737	144824	107264	90986	446374
424672	147886	133204	128560	311863'''
    a = a.split('\n')
    data = []
    for i in a:
        i=i.split('\t')
        # data.append(int(i))
        temp = []
        for d in i:
            temp.append(int(d))
        data.append(temp)
    df = pd.DataFrame(data).T
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
    a= '''263484	252464	284295	356737	424672
104980	101426	105873	144824	147886
162749	161515	143990	107264	133204
135401	127550	134244	90986	128560
479571	503230	477783	446374	311863'''
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
    df = pd.DataFrame(data).T
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
    plt.ylabel('面积（万km2）'.decode('gbk'))
    plt.xticks(range(5),['1978','1985','1995','2005','2018'])
    # plt.yticks([0,100000,200000,300000,400000],['0','10','20','30','40'])
    plt.legend()
    plt.title(title)
    for i in df.T:
        plt.scatter(range(len(df.T)),df.T[i]/10000,c=cmap[i])

    plt.show()
    # print(df)


def plot_zone3_zone4():
    a3 = ['''72010	62025	90331	43014	6184
    64350	63734	88263	49017	8200
    87557	67502	75775	36904	5826
    118301	84139	49597	16207	5320
    162759	64760	32368	10192	3485
    ''', '''68996	46844	76821	96316	220393
    61730	44079	77649	83497	242415
    73247	42489	72721	101588	219325
    114954	64248	63116	77343	189709
    141128	86422	104853	113133	63834
    ''', '''0	26	733	7968	77446
    0	2	700	6146	79325
    176	315	1397	13779	70506
    280	1053	6496	26826	51518
    1808	6242	23045	34607	20471
    ''']

    a4 = ['''241010	55658	52245	23652	14977
    235734	59306	65676	23657	3169
    254440	50383	48536	25311	8872
    295924	54161	26759	7328	3370
    317426	41750	19618	5263	3485
    ''', '''8066	16888	32657	17559	4080
    7975	17375	32501	17576	3823
    14706	24113	27368	9633	3430
    21416	33966	17285	4131	2452
    39943	24766	8879	3354	2308
    ''', '''12984	26983	58325	68586	372670
    7978	21172	44973	60685	404740
    13645	22602	48273	70426	384602
    36242	38733	41489	43846	379238
    50503	59177	69590	78704	281574
    ''', '''1433	5462	19535	25618	87854
    783	3582	18384	25645	91508
    1513	8786	19832	28883	80888
    3163	17989	21740	35688	61322
    16828	22207	35125	41242	24500
    ''']

    shp_name4 = ['北方风沙区', '北方土石山区', '东北黑土区', '西北黄土高原区']
    shp_name3 = ['内蒙古草地', '鄂尔多斯市', '内蒙古农牧交错带']
    plot_fenqu_line(a4[3], shp_name4[3].decode('gbk'))
    # for i in range(len(shp_name3)):

def main():
    a=['''21002	25447	35894	4463	90
20944	34231	28212	3301	208
27140	34093	21589	3528	546
11542	35809	27453	9081	3011
16087	38689	22155	7358	2607
''','''0	0	194	17592	69083
17	20	1403	36427	49002
0	855	4556	53495	27963
325	1764	13260	41314	30206
387	2256	18059	42104	24063
''','''13595	20326	26421	1737	0
16325	25541	18221	1979	13
19656	22196	18057	2102	68
17254	29432	11997	2831	565
21270	27556	10404	2367	482
''','''0	0	33	5390	2128
0	0	78	5776	1697
0	21	429	6880	221
4	142	4626	2616	163
4	282	5509	1646	110'''


    ]

    titles = ['赤峰市', '鄂尔多斯', '通辽市', '准格尔旗']
    # title = '太行山山地丘陵区'.decode('gbk')
    for i in range(4):
        plot_fenqu_line(a[i],titles[i].decode('gbk'))
    pass



if __name__ == '__main__':

    #     plot_fenqu_line(a4[i],shp_name4[i].decode('gbk'))

    # plot_fenqu_line()

    # fenqu()
    main()
    pass