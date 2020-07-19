# 数据加载模块，包含数据预处理函数
import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold


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

        self.preHandle()

    # 数据预处理
    def preHandle(self):
        # 缺省填补采用中位数填补策略
        imp_median = SimpleImputer(strategy='median')
        self.metadata = imp_median.fit_transform(self.metadata)

        # 方差过滤
        selector = VarianceThreshold()
        self.metadata = selector.fit_transform(self.metadata)

    def getData(self):
        return self.df

    def getMetaData(self):
        return self.metadata
