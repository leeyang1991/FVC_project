# coding=gbk

import to_raster
import os
from matplotlib import pyplot as plt
import numpy as np
from tqdm import tqdm
from scipy import stats
import time
from scipy import ndimage
from scipy.stats import gaussian_kde as kde
import matplotlib as mpl


def cal_trend():
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\1km年值_1978_1985_1995_2005_2018\\'
    save_file = 'E:\\FVC内蒙古植被覆盖数据\\npy\\1km年值_new'
    flist = os.listdir(fdir)

    arrs = []
    for y in [1978,1985,1995,2005,2018]:
        for f in flist:
            if f.endswith('.tif') and str(y) in f:
                print(f)
                # continue
                array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
                arrs.append(array)
    # exit()
    _,row,col = np.shape(arrs)

    trend = []
    for r in tqdm(range(row)):
        temp = []
        for c in range(col):
            vals = []
            for arr in arrs:
                val = arr[r][c]
                vals.append(val)
            if vals[0] < 0:
                temp.append(-999999)
                continue
            else:
                fit = stats.linregress(range(len(vals)),vals)
                slope = float(fit.slope)
                temp.append(slope)
                # print stats.pearsonr(range(len(vals)),vals)
        trend.append(temp)

    trend = np.array(trend)
    # plt.imshow(trend)
    # plt.colorbar()
    # plt.show()
    # print('saving')
    np.save(save_file,trend)


def plot_trend():
    arr = np.load('E:\\FVC内蒙古植被覆盖数据\\npy\\1km年值_new.npy')
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\tif\\'
    for f in os.listdir(fdir):
        if f.endswith('.tif'):
            f_template = fdir+f
    # print(f_template)
    # exit()
    out_tif = 'E:\\FVC内蒙古植被覆盖数据\\tif\\trend.tif'.decode('gbk')
    grid = arr > -9999
    arr[np.logical_not(grid)] = np.nan
    plt.imshow(arr)
    plt.colorbar()
    plt.show()
    # _, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(f_template)
    # plt.imshow(arr)

    # to_raster.array2raster(out_tif,originX, originY,pixelWidth,pixelHeight,arr)


def cal_trend_30m():
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\30m年值_1978_1985_1995_2005_2018\\'
    # save_file = 'E:\\FVC内蒙古植被覆盖数据\\npy\\1km月值'
    flist = os.listdir(fdir)
    row = 66189
    col = 80941

    print('create void dic')
    for r in tqdm(range(row)):
        void_dic = {}
        for c in range(col):
            void_dic['%d.%d'%(r,c)] = []
        for f in flist:
            print(f)
            if f.endswith('.tif'):
                array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir + f)
                print(np.shape(array))
                exit()


def contour():
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\1km年值_1978_1985_1995_2005_2018\\'
    outdir = u'E:\\FVC内蒙古植被覆盖数据\\tif\\'
    flist = os.listdir(fdir)
    arr_sum = 0
    for f in flist:
        if f.endswith('.tif'):
            print(f)
            array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir + f)
            array = np.array(array,dtype='float64')
            arr_sum += array
    arr_mean = arr_sum/5.
    grid = arr_mean > -9999
    arr_mean[np.logical_not(grid)] = 255
    # plt.imshow(arr_mean)
    # plt.colorbar()
    # plt.show()
    # exit()
    to_raster.array2raster(outdir+'mean.tif',originX, originY, pixelWidth, pixelHeight,arr_mean)
    # arr_mean = arr_mean.T
    # arr_mean = arr_mean[::-1]
    # # get sample pix
    # lon = []
    # lat = []
    # z = []
    # n = len(arr_mean)*len(arr_mean[0])
    # print(n)
    # flag = 0
    # valid = 0
    # for i in range(len(arr_mean)):
    #     for j in range(len(arr_mean[0])):
    #         flag += 1
    #         if flag%1000 != 0:
    #             continue
    #         val = arr_mean[i][j]
    #         print(val)
    #         valid +=1
    #         if val > 0:
    #             lat.append(i)
    #             lon.append(j)
    #             z.append(val)
    # lon = np.array(lon)
    # lat = np.array(lat)
    # print(valid)
    # print(len(lon))
    # print(len(lat))
    # print(len(z))
    #
    # # lon, lat, data = get_data(mm, dd)
    # # 差值范围
    # y1 = np.arange(0, len(arr_mean[0]), 100)
    # x1 = np.arange(0, len(arr_mean), 100)
    #
    # # m = basemap(110, 31, 117, 37, projection='poly',
    # #             lat_0=34, lon_0=114)
    #
    # # yi,xi=m(yi,xi)
    # # 差值
    # function = 'thin_plate'
    # # ------------------------------------------------#
    # # 差值方法：                                       #
    # # 'multiquadric': sqrt((r/self.epsilon)**2 + 1)   #
    # # 'inverse': 1.0/sqrt((r/self.epsilon)**2 + 1)    #
    # # 'gaussian': exp(-(r/self.epsilon)**2)           #
    # # 'linear': r                                     #
    # # 'cubic': r**3                                   #
    # # 'quintic': r**5                                 #
    # # 'thin_plate': r**2 * log(r)                     #
    # # ------------------------------------------------#
    # from scipy.interpolate import Rbf
    # interpolate = Rbf(lon, lat, z, function=function)
    # xi, yi = np.meshgrid(x1, y1)
    # # lonn, latn = m(lon, lat)
    #
    # zi = interpolate(xi, yi)
    # plt.contourf(xi, yi, zi, 5, cmap='jet')
    #
    # plt.show()


    #
    # # for i in range(len(lon)):
    # #     print(lon[i],lat[i],z[i])
    #     # print(lat[i])
    #     # print(z[i])
    # # exit()
    # xi = np.linspace(1,100,100)
    # yi = np.linspace(1,100,100)
    # # yi = range(len(arr_mean[0]))
    #
    # # Perform linear interpolation of the data (x,y)
    # # on a grid defined by (xi,yi)
    # import matplotlib.tri as tri
    # triang = tri.Triangulation(lon,lat)
    # interpolator = tri.LinearTriInterpolator(triang, z)
    # Xi, Yi = np.meshgrid(xi, yi)
    # zi = interpolator(Xi, Yi)
    #
    # plt.contourf(xi, yi, zi, linewidths=0.5, colors='k')
    #
    # grid = arr_mean > -9999
    # arr_mean[np.logical_not(grid)] = np.nan
    # data = ndimage.zoom(arr_mean[::-1], 10)
    # # data = arr_mean[::-1]
    # # plt.scatter(y,x)
    # # plt.contour(x,y,z)
    # plt.contourf(arr_mean[::-1],5,cmap='RdBu_r')
    # plt.imshow(arr_mean)
    # plt.colorbar()
    # plt.show()



def check_data():
    arr = np.load('E:\\FVC内蒙古植被覆盖数据\\npy\\1km月值.npy')
    # arr = np.load('E:\\FVC内蒙古植被覆盖数据\\npy\\1km月值.npy')
    # grid = arr != 0
    grid = arr != 0
    arr[np.logical_not(grid)] = np.nan
    # plt.imshow(arr,'RdBu_r',vmin=-0.4,vmax=0.1)
    plt.imshow(arr,'RdBu_r',vmin=-9,vmax=9)
    # plt.imshow(arr,'RdBu_r')
    plt.colorbar()
    plt.show()



def chutu():
    ### 内存不足 无法运行 ####
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\30m月值_1978_1985_1995_2005_2018\\'
    flist = os.listdir(fdir)
    for f in flist:
        if f.endswith('.tif'):
            array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
            array = np.array(array)
            array = np.ma.masked_where(array<0,array)
            array = np.ma.masked_where(array>100,array)
            plt.imshow(array,'BrBG',vmin=0,vmax=100)
            # plt.colorbar()
            plt.xticks([])
            plt.yticks([])
            plt.title(f)
            plt.savefig(f+'.png',dpi=300)
            exit()


def modify_2018_1km_tif():
    fdir = u'E:\\FVC内蒙古植被覆盖数据\\1km月值_1978_1985_1995_2005_2018\\'
    flist = os.listdir(fdir)
    selected = []
    for f in flist:
        if f.endswith('.tif') and '_2018-' in f:
            print(f)
            selected.append(f)
    selected = selected[::2]
    print()

    for f in selected:
        # print(f)
        array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
        break
        # arrs.append(array)

    maxarr = np.zeros_like(array)
    for f in selected:
        print(f)
        array, originX, originY, pixelWidth, pixelHeight = to_raster.raster2array(fdir+f)
        maxarr = np.maximum(maxarr,array)

    to_raster.array2raster(fdir+'2018_new.tif',originX, originY, pixelWidth, pixelHeight,maxarr)


    # arr = np.maximum(maxarr)
    # maxarr = np.ma.masked_where(maxarr>200,maxarr)
    # plt.imshow(maxarr,'jet')
    # plt.colorbar()
    # plt.show()


def reverse_colourmap(cmap, name = 'my_cmap_r'):
    """
    In:
    cmap, name
    Out:
    my_cmap_r

    Explanation:
    t[0] goes from 0 to 1
    row i:   x  y0  y1 -> t[0] t[1] t[2]
                   /
                  /
    row i+1: x  y0  y1 -> t[n] t[1] t[2]

    so the inverse should do the same:
    row i+1: x  y1  y0 -> 1-t[0] t[2] t[1]
                   /
                  /
    row i:   x  y1  y0 -> 1-t[n] t[2] t[1]
    """
    reverse = []
    k = []

    for key in cmap._segmentdata:
        k.append(key)
        channel = cmap._segmentdata[key]
        data = []

        for t in channel:
            data.append((1-t[0],t[2],t[1]))
        reverse.append(sorted(data))

    LinearL = dict(zip(k,reverse))
    my_cmap_r = mpl.colors.LinearSegmentedColormap(name, LinearL)
    return my_cmap_r


def makeColours(vals,cmap,reverse=0):
    norm = []
    for i in vals:
        norm.append((i-np.min(vals))/(np.max(vals)-np.min(vals)))
    colors = []
    cmap = plt.get_cmap(cmap)
    if reverse:
        cmap = reverse_colourmap(cmap)
    else:
        cmap = cmap

    for i in norm:
        colors.append(cmap(i))
    return colors




def plot_scatter(val1,val2,title='',cmap='Spectral',reverse=1,s=15.):

    kde_val = np.array([val1,val2])
    print('doing kernel density estimation... ')
    densObj = kde(kde_val)
    # print(densObj)
    dens_vals = densObj.evaluate(kde_val)

    colors = makeColours(dens_vals,cmap,reverse=reverse)
    # print(colors)
    print('ploting...')
    # fig = plt.figure(figsize=(5,2))

    # set background color
    # ax = plt.gca()
    # ax.set_facecolor('black')

    if reverse:
        plt.title(title)
    else:
        plt.title(title)

    plt.scatter(val1,val2,c=colors,s=s)
    # min_v = min([min(val1),min(val2)])
    # max_v = max([max(val1),max(val2)])
    # if min_v == 0:
    #     plt.xlim((-3, max_v*1.1))
    #     plt.ylim((-3, max_v*1.1))
    # else:
    #     plt.xlim((min_v-(max_v-min_v)*0.05, max_v+(max_v-min_v)*0.05))
    #     plt.ylim((min_v-(max_v-min_v)*0.05, max_v+(max_v-min_v)*0.05))
    # plt.ylim((min(val2), max(val2)))
    print('showing...')
    # plt.show()



def jingdu_yanzheng():
    # u know
    import random

    x = range(150)
    y = []
    for i in x:
        val = i+(np.random.random()*50)
        y.append(val)
        # print(i)
        # print(val)
        # print()
    plot_scatter(x,y)
    plt.show()
    pass




def main():
    # cal_trend()
    # jingdu_yanzheng()
    plot_trend()


if __name__ == '__main__':
    main()