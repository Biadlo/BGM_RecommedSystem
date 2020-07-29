import matplotlib.pyplot as plt

from algorithm.DataLoader import DataLoader

dataLoader = DataLoader("../gui/input_data/origin_data.txt")
data = dataLoader.metadata
result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
music_types = ['metal', 'disco', 'classical', 'hiphop', 'jazz', 'country', 'pop', 'blues', 'reggae', 'rock']
for i in range(13500):
    for j in range(10):
        result[j] += data[i][j + 2]
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.bar(x=X, height=result, color='steelblue', tick_label=music_types)
for a, b in zip(X, result):
    plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=7)
plt.xticks(rotation=-20)
plt.title("所有BGM样本特征统计总和")
plt.savefig('../gui/output_data/sum1' + '.png', width=10)
