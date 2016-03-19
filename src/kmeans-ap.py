#coding:utf-8


import numpy as np
import matplotlib.pyplot as plt
import time
from sklearn.cluster import KMeans,AffinityPropagation
from sklearn.datasets.samples_generator import make_blobs

# 生成测试数据
np.random.seed(0)
centers = [[1, 1], [-1, -1], [1, -1]]
kmeans_time = []
ap_time = []
for n in [100,500,1000]:
    X, labels_true = make_blobs(n_samples=n, centers=centers, cluster_std=0.7)

    # 计算K-Means算法时间
    k_means = KMeans(init='k-means++', n_clusters=3, n_init=10)
    t0 = time.time()
    k_means.fit(X)
    kmeans_time.append([n,(time.time() - t0)])

    # 计算AP算法时间
    ap = AffinityPropagation()
    t0 = time.time()
    ap.fit(X)
    ap_time.append([n,(time.time() - t0)])

print ('K-Means time',kmeans_time[:10])
print ('AP time',ap_time[:10])
# 图形展示
km_mat = np.array(kmeans_time)
ap_mat = np.array(ap_time)
plt.figure()
plt.bar(np.arange(3), km_mat[:,1], width = 0.3, color = 'b', label = 'K-Means', log = 'True')
plt.bar(np.arange(3)+0.3, ap_mat[:,1], width = 0.3, color = 'g', label = 'AffinityPropagation', log = 'True')
plt.xlabel('Sample Number')
plt.ylabel('Computing time')
plt.title('K-Means and AffinityPropagation computing time ')
plt.legend(loc='upper center')
plt.show()