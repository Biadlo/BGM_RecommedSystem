from mpl_toolkits.mplot3d import Axes3D

from algorithm.DataLoader import DataLoader
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA


class DataHandler(object):
    def __init__(self, datafile):
        # 获取元数据,每次一类
        self.metaData = []
        for i in range(9):
            self.data_loader = DataLoader(datafile)
            self.metaData.append(self.data_loader.getMetaData()[i * 1500:(i + 1) * 1500, 2:12])

        # pca 主成分分析,0.95保存率下需要8维,降维为3维用于数据展示
        self.pca = PCA(n_components=3)

        # 降维结果集
        self.data_reduction = []
        for i in range(9):
            self.pca.fit(self.metaData[i])
            self.data_reduction.append(self.pca.transform(self.metaData[i]))
            # 每一个商品类型做聚类
            self.n_cluster = 3
            # 完成寻找质心
            cluster_show = KMeans(n_clusters=self.n_cluster, random_state=0).fit(self.data_reduction[i])
            # 数据根据质心分类
            self.pre = cluster_show.fit_predict(self.data_reduction[i])
            # 展示质心
            self.centroid_show = cluster_show.cluster_centers_

            color = ['red', 'blue', 'orange']
            axes3d = Axes3D(plt.figure())
            for j in range(self.n_cluster):
                axes3d.scatter3D(self.data_reduction[i][self.pre == j, 0], self.data_reduction[i][self.pre == j, 1],
                                 self.data_reduction[i][self.pre == j, 2],
                                 marker='o', s=8, c=color[j], zorder=1, alpha=0.6)
                axes3d.scatter3D(self.centroid_show[:, 0], self.centroid_show[:, 1], self.centroid_show[:, 2],
                                 marker='x', s=200,
                                 c='black',
                                 zorder=2, alpha=1)

            # 保存为多个文件
            plt.savefig('./output_data/fig' + str(i) + '.png', bbox_inches='tight')

    def getMusicType(self, index):
        # 根据质心确定音乐种类，重新使用聚类，不做数据可视化
        cluster = KMeans(n_clusters=self.n_cluster, random_state=0).fit(self.metaData[index])
        centroid = cluster.cluster_centers_

        # 确定音乐种类
        music_class = []
        music_types = ['metal', 'disco', 'classical', 'hiphop', 'jazz', 'country', 'pop', 'blues', 'reggae', 'rock']
        for j in range(3):
            music_class.append(music_types[int(np.argmax(centroid[j]))])
        return music_class
