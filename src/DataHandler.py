from DataLoader import DataLoader
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d.axes3d import Axes3D

# 获取元数据,每次一类
metaData = []
for i in range(9):
    data_loader = DataLoader('origin_data.txt')
    metaData.append(data_loader.getMetaData()[i * 1500:(i + 1) * 1500, 2:12])

# pca 主成分分析,0.95保存率下需要8维,降维为3维用于数据展示
pca = PCA(n_components=3)
# 降维结果集
data_reduction = []
for i in range(9):
    pca.fit(metaData[i])
    data_reduction.append(pca.transform(metaData[i]))

# 每一个商品类型做聚类
n_cluster = 3
for i in range(9):
    n_cluster = 3
    # 完成寻找质心
    cluster_show = KMeans(n_clusters=n_cluster, random_state=0).fit(data_reduction[i])
    # 数据根据质心分类
    pre = cluster_show.fit_predict(data_reduction[i])
    # 展示质心
    centroid_show = cluster_show.cluster_centers_
    # 数据可视化
    color = ['red', 'blue', 'orange']
    axes3d = Axes3D(plt.figure())
    for j in range(n_cluster):
        axes3d.scatter3D(data_reduction[i][pre == j, 0], data_reduction[i][pre == j, 1], data_reduction[i][pre == j, 2],
                         marker='o', s=8, c=color[j], zorder=1, alpha=0.6)
        axes3d.scatter3D(centroid_show[:, 0], centroid_show[:, 1], centroid_show[:, 2], marker='x', s=200, c='black',
                         zorder=2, alpha=1)

    # 保存为多个文件
    plt.savefig('fig' + str(i) + '.png', bbox_inches='tight')

    # 根据质心确定音乐种类，重新使用聚类，不做数据可视化
    cluster = KMeans(n_clusters=n_cluster, random_state=0).fit(metaData[i])
    pre = cluster.fit_predict(metaData[i])
    centroid = cluster.cluster_centers_

    # 确定音乐种类
    music_class = []
    for j in range(3):
        music_class.append(np.argmax(centroid[j]))

    max_music = 0
    for j in range(10):
        temp = music_class.count(j)
        if temp > max_music:
            max_music = j

    # 分辨出是哪种音乐种类
    music_types = ['metal', 'disco', 'classical', 'hiphop', 'jazz', 'country', 'pop', 'blues', 'reggae', 'rock']
    music_type = music_types[max_music]
    print(music_type)
