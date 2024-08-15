# 07 Clustering

개요

- K-평균 알고리즘
  - Clustering에서 가장 general하게 사용되는 알고리즘
  - 군집 중심점(centroid)라는 특정한 임의의 지점을 선택하여, 해당 중심에 가장 가까운 포인트들을 선택하는 군집화 기법
- K-평균 알고리즘의 Process
  - 각 데이터들이 가장 가까운 중심점에 소속 됨
  - 중심점이 소속 된 포인트들의 평균 지점으로 이동
  - 반복적으로 수행 (이 과정에서 데이터들의 소속이 바뀜)
  - 중심점의 이동이 없을 때, 군집화
- K-means 장점
  - 알고리즘의 쉽고 간결
- K-means 단점
  - 거리 기반 알고리즘으로 속성이 매우 많을 경우 군집화 정확도가 떨어짐
  - Process 반복 횟수가 많을 경우 수행 시간이 느려짐
  - cluster의 개수를 설정하는데 있어서 가이드가 어렵다.

---

- sklearn

  - KMeans

    - ```python
      class sklearn.cluster.KMeans(
          n_clusters = 8, # 군집 중심점의 개수
      	init = 'k-means++', # 군집 중심점의 좌표
      	n_init = 10,
      	max_iter = 300, # 최대 반복 횟수
      	tol = 0.0001,
          precompute_distances = 'auto',
          verbose = 0,
          random_state = None,
          copy_x = True,
          n_jobs = 1,
          algorithm = 'auto'
      )
      ```

- dataset을 가져와서 DF로 변환한다.

- ```python
  from sklearn.preprocessing import scale
  from sklearn.cluster import KMeans
  import matplotlib.pyplot as plt
  import numpy as np
  import pandas as pd
  %matplotlib inline
  
  kmeans = KMeans(n_clusters=3, init='k-means++', max_iter=300,random_state=0)
  kmeans.fit(irisDF)
  
  print(kmeans.labels_)
  # 군집화 된 내용 출력
  ```

- 2차원 평면에서의 시각화를 위해서는 속성을 2개로 차원 축소 해야함.

- ```python
  from sklearn.decomposition import PCA
  
  pca = PCA(n_components=2)
  pca_transformed = pca.fit_transform(iris.data)
  
  irisDF['pca_x'] = pca_transformed[:,0]
  irisDF['pca_y'] = pca_transformed[:,1]
  irisDF
  ```

- ```python
  # 시각화
  # 군집 값이 0, 1, 2인 경우마다 별도의 인덱스로 추출
  marker0_ind = irisDF[irisDF['cluster']==0].index
  marker1_ind = irisDF[irisDF['cluster']==1].index
  marker2_ind = irisDF[irisDF['cluster']==2].index
  
  # 군집 값 0, 1, 2에 해당하는 인덱스로 각 군집 레벨의 pca_x, pca_y 값 추출. o, s, ^ 로 마커 표시
  plt.scatter(x=irisDF.loc[marker0_ind, 'pca_x'], y=irisDF.loc[marker0_ind, 'pca_y'], marker='o')
  plt.scatter(x=irisDF.loc[marker1_ind, 'pca_x'], y=irisDF.loc[marker1_ind, 'pca_y'], marker='s')
  plt.scatter(x=irisDF.loc[marker2_ind, 'pca_x'], y=irisDF.loc[marker2_ind, 'pca_y'], marker='^')
  
  plt.xlabel('PCA 1')
  plt.ylabel('PCA 2')
  plt.title('3 Clusters Visualization by 2 PCA Components')
  plt.show()
  ```

- 군집화 평가 방법은 어렵다.

  - 뭐가 잘 된건지 어케암
  - 그래도 실루엣 분석 방법이 있음
  - 얼마나 효율적으로 분리되어 있는지...

- 