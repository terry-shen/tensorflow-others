############################################################################
# -*- coding:gbk -*-                                                      #
# created by Starry.Teng on 2017.5.19                                         #
# mail tengxing7452@163.com                                                #
# github github.com/tengxing                                               #
# description �ļ�������                                              #
############################################################################
import pandas as pd
import matplotlib.pyplot as plt

# read data
def readData(path):
    if path:
        return pd.read_csv(open(path))


#������ͼչʾdata
def showOnPlt(data):
    plt.figure()
    plt.plot(data)
    plt.show()

