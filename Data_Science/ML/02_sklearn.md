# 02 sklearn

- scikit-learn
  - 파이썬 머신러닝 라이브러리
  - 파이썬스러운 API
  - 검증되었고, 많은 환경에서 사용되는 라이브러리

- 지도학습(Supervised learning)

  - 주어진 데이터 세트를 학습한 뒤 예측하는 것
  - 각각의 입력(x)에 대해 레이블(y)을 달아놓은 데이터를 컴퓨터에 주면 컴퓨터가 그것을 학습하는 것
  - Classification
    - 레이블 y가 이산적(Discrete)인 경우 즉, y가 가질 수 있는 값이 [0,1,2 ..]와 같이 유한한 경우 분류, 혹은 인식 문제라고 부른다.
  - Regression
    - 레이블 y가 실수인 경우 회귀문제라고 부른다.
    - 데이터들을 쭉 뿌려놓고 이것을 가장 잘 설명하는 직선 하나 혹은 이차함수 곡선 하나를 그리고 싶을 때 회귀사용.

- 비지도학습(Unsupervised Learning)

  - 컴퓨터가 스스로 레이블 되어 있지 않은 데이터에 대해 학습하는 것. 즉 y없이 x만 이용해서 학습하는 것이다. 정답이 없는 문제를 푸는 것이므로 학습이 맞게 됐는지 확인할 길은 없음.
  - Clustering
  - 분포 추정

- dataset을 학습용과 테스트용으로 분리

  - train_test_split()

- 레이블(Label)

  - 학습 데이터의 속성을 무엇을 분석할 지에 따라 정의되는 데이터

  - ```python
    # 예시
    ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
    [5, 4, 3, 3] # 인 꽃의 품종은 0번 품종이다. (feature)
    # 레이블 : 0 (target)
    # 이러한 데이터들을 여러 개 학습시키고, 새로운 데이터의 품종을 예측한다.
    ```

- sklearn에서

  - Classification 알고리즘을 구현한 class
    - Classifier
  - Regression 알고리즘을 구현한 class
    - Regressor
  - 둘을 합쳐서 Estimator class
    - 학습 method : fit()
    - 예측 method : predict()
    - 내부에서 구현하고 있음.

---

## Estimator, fit(), predict()

- 비지도학습에서 fit(), transform()
  - 지도학습의 fit()에서와 같이 학습을 의미하는 것이 아님
  - 입력 데이터의 형태에 맞춰 데이터를 변환하기 위한 사전 구조를 맞추는 작업
  - fit()으로 변환을 위한 사전 구조를 맞춘 이후
  - 입력 데이터의 차원 변환, 클러스터링, 피처 추출 등의 실제 작업은 transform()으로 수행

---

- 머신러닝 모델을 구축하는 주요 프로세스
  - feature 가공, 변경, 추출
  - ML 알고리즘 학습/예측 수행
  - 모델 평가
  - 반복

---

## 기본적인 ML process & train_test_split()

- parameters

  - test_size
  - shuffle
  - random_state

- return value

  - (학습 피처 data, 테스트 피처 data, 학습 레이블 data, 테스트 레이블 data)
  - tuple

- ```python
  X_train, X_test, y_train, y_test = train_test_split(iris_data, iris_label, 
                                                      test_size=0.2, random_state=11)
  # DecisionTreeClassifier 객체 생성 
  dt_clf = DecisionTreeClassifier(random_state=11)
  
  # 학습 수행
  dt_clf.fit(X_train, y_train)
  
  # 학습이 완료된 DecisionTreeClassifier 객체에서 테스트 데이터 세트로 예측 수행. 
  pred = dt_clf.predict(X_test)
  
  # 예측 정확도 출력
  from sklearn.metrics import accuracy_score
  print('예측 정확도: {0:.4f}'.format(accuracy_score(y_test,pred)))
  ```

- ML process summary

  - train_test_split()
  - create classifier instance
  - fit()
  - predict()
  - accuracy_score()

---

## 교차 검증

- Cross Validation

- 학습된 모델에 대해 다양한 데이터를 기반으로 예측 성능을 평하게 보는 것이 중요

- 과적합 (Overfitting)

  - 고정된 테스트 dataset을 통해 성능을 검증하고 수정하는 과정을 반복하게 되면, 해당 테스트 dataset에만 잘 동작하는 모델이 된다.
    - 모델이 해당 test dataset에 과적합
  - 학습데이터에 대해서는 오차가 감소하지만 실제 데이터에 대해서는 오차가 증가하게 되는 현상.

- 다양한 학습과 평가 필요

- 기존 (학습 dataset, 테스트 dataset) 에서

  - (학습 dataset + 검증 dataset, 테스트 dataset) 으로 나눈다.

- K 폴드

  -  KFold
  - dataset 을 K개로 쪼갠 뒤, 그 중 하나를 검증 세트로 두고, 학습과 검증을 진행.
  - 이런 방식으로 K번 진행 후 평균

- ndarray.shape

  - 배열의 형상
  - (가로줄 개수, 세로줄 개수) return

- Stratified K 폴드

  - imbalanced 한 분포도를 가진 레이블 데이터 집합을 위한 K 폴드 방식

  - 특정 레이블 값이 특이하게 많거나 매우 적은 경우

  - 예를들어 대출 사기 여부 레이블이 있다고 할 때, (사기 : 1, 정상 : 0)

  - 레이블 1은 드물지만 중요한 데이터셋이다.

  - 원본 데이터 집합의 레이블 분포를 학습 및 테스트 세트에 제대로 분배하지 못하는 겨웅의 문제를 해결해 줌

  - 원본 데이터의 레이블 분포를 먼저 고려한 뒤, 이 분포와 동일하게 데이터를 분배해준다.

  - 분포도를 알기위해 parameter로 피처 뿐 아니라 레이블 데이터 세트도 넘겨준다.

  - ```
    skfold.split(features, label)
    ```

  - Classification에서의 교차 검증은 Stratified KFold로 분할되어야 한다.

  - Regression에서는 회귀의 결정값이 descrete 하지 않고 연속적이기 때문에 skf 적용 불가.

- cross_val_score()

  - 교차 검증을 보다 간편하게

  - 교차 검증 과정

    - k개의 fold set 설정
    - for 문으로 학습, 예측 반복
    - 코드를 다 짜야함

  - 위 과정을 한꺼번에 수행해주는 API

  - ```python
    cross_val_score(
    	estimator, # classifier 또는 regressor
    	X, # feature dataset
    	y = None, # label dataset
    	scoring = None, # 예측 성능 평가 지표
    	cv = None, # 교차 검증 폴드 수
    	n_jobs = 1,
    	verbose = 0,
    	fit_params = None,
    	pre_dispatch = '2*n_jobs'
    	)
    ```

  - return value

    - scoring 파라미터로 지정된 성능 지표 측정값을 배열 형태로 반환

  - ```python
    iris_data = load_iris()
    dt_clf = DecisionTreeClassifier(random_state=156)
    
    data = iris_data.data
    label = iris_data.target
    
    # 성능 지표는 정확도(accuracy) , 교차 검증 세트는 3개 
    scores = cross_val_score(dt_clf , data , label , scoring='accuracy',cv=3)
    print('교차 검증별 정확도:',np.round(scores, 4))
    print('평균 검증 정확도:', np.round(np.mean(scores), 4))
    
    # 교차 검증별 정확도: [0.98 0.94 0.98]
    # 평균 검증 정확도: 0.9667
    ```

---

## 데이터 전처리

- Data preprocessing

- ML은 data 기반이기 때문에 전처리가 중요하다.

  - garbage in, garbage out

- NaN, Null 값 불허

  - 경우에 따라 대체값의 처리 방법이 다름
  - 피처의 평균값 넣거나, 그냥 해당 feature를 drop 등등

- sklearn의 ML 알고리즘은 String 불허

  - 모두 숫자 형으로 변환해야함.
  - 카테고리형 feature를 코드 값으로 대체한다던지 등
  - data raw 식별 용도로 주로 사용되는 문자열 feature는 drop하는게 좋다

- 레이블 인코딩

  - 카테고리 피처를 코드형 숫자 값으로 변환하는 것

  - ```python
    items=['TV','냉장고','전자레인지','컴퓨터','선풍기','선풍기','믹서','믹서']
    
    # LabelEncoder를 객체로 생성한 후 , fit( ) 과 transform( ) 으로 label 인코딩 수행. 
    
    encoder = LabelEncoder()
    encoder.fit(items)
    labels = encoder.transform(items)
    print('인코딩 변환값:',labels)
    # 인코딩 변환값: [0 1 4 5 3 3 2 2]
    
    print('인코딩 클래스:',encoder.classes_)
    # 인코딩 클래스: ['TV' '냉장고' '믹서' '선풍기' '전자레인지' '컴퓨터']
    
    print('디코딩 원본 값:',encoder.inverse_transform([4, 5, 2, 0, 1, 1, 3, 3]))
    # 디코딩 원본 값: ['전자레인지' '컴퓨터' '믹서' 'TV' '냉장고' '냉장고' '선풍기' '선풍기']
    ```

  - 레이블 인코딩 시, 숫자는 오직 분류를 위한 것이며, 순서나 중요도와는 관련이 없는 것이므로, 선형회귀와 같은 알고리즘에서는 적용하지 말아야한다.

- 원-핫 인코딩

  - One-Hot

  - 카테고리 항목 별로 새로운 피처를 추가하고, 해당하는 피처 column에만 1을 표시, 나머지에는 0 표시.

  - ```python
    # 원-핫 인코딩 데이터
    # [티비, 냉장고, 믹서, 선풍기, 전자레인지, 컴퓨터] (컬럼명)
    [[1. 0. 0. 0. 0. 0.] # 티비
     [0. 1. 0. 0. 0. 0.] # 냉장고
     [0. 0. 0. 0. 1. 0.] # 전자레인지
     [0. 0. 0. 0. 0. 1.] # 컴퓨터
     [0. 0. 0. 1. 0. 0.] # 선풍기
     [0. 0. 0. 1. 0. 0.] # 선풍기
     [0. 0. 1. 0. 0. 0.] # 믹서
     [0. 0. 1. 0. 0. 0.]] # 믹서
    # 원-핫 인코딩 데이터 차원
    (8, 6)
    
    import pandas as pd
    
    df = pd.DataFrame({'item':['TV','냉장고','전자레인지','컴퓨터','선풍기','선풍기','믹서','믹서'] })
    pd.get_dummies(df)
    ```

- 피처 스케일링과 정규화
  - 피처 스케일링
    - 서로 다른 피처의 값 범위를 일정하게 맞춰주는 것
    - 거리와 금액 feature가 있을 때, 거리는 0~100km, 금액은 0~100000000000000원
    - 이 범위를 일정한 수준으로 맞춰준다.
  - 표준화 (Standardization)
    - 평균 0, 분산 1 인 정규 분포로 변환
    - Z = (X - m) / stdev(X)
  - 정규화 (Normalization)
    - 모두 0 ~ 1 사이 값으로 변환.
    - (x - min(x)) / (max(x) - min(x)) 를 새로운 값으로 잡으면 됨.
    - sklearn의 전처리에서 제공하는 정규화 모듈은 선형대수에서의 정규화 개념이 적용된다. (벡터 정규화)
- StandardScaler
  - 표준화 지원 클래스
  - SVM, Linear Regression, Logistic Regression 등을 적용할 때 중요
- MinMaxScaler
  - 데이터 값을 0과 1사이 값으로 바꿔준다.
  - 데이터의 분포가 정규분포를 따르지 않을 때 적용해볼 수 있다.
- 스케일링 기준이 학습데이터와 테스트데이터가 서로 다르면 안된다.
- 그냥 데이터셋 분리 전에 스케일링을 하셈;



