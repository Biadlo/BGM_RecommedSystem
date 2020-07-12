# 数据加载模块
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


class DataLoader(object):
    def __init__(self, data_text):
        # 显示所有列
        pd.set_option('display.max_columns', None)
        # 显示所有行
        pd.set_option('display.max_rows', None)
        # 若想不以科学计数显示:
        np.set_printoptions(suppress=True)

        data = np.genfromtxt(data_text, delimiter=',', encoding='UTF-8')

        columnList = ['商品类型', '销量', 'metal', 'disco', 'classical', 'hiphop', 'jazz', 'country', 'pop', 'blues',
                      'reggae',
                      'rock', '观看数', '点赞数']
        self.df = pd.DataFrame(data, columns=columnList)
        self.metadata = data

    def getData(self):
        return self.df

    def getMetaData(self):
        return self.metadata

