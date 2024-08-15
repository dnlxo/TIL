## 04_Classification

- 지도학습

  - 레이블 : 명시적인 정답
  - 이 있는 데이터가 주어진 상태에서 학습하는 머신러닝 방식

- 학습 데이터로 주어진 데이터의 feature와 label을 머신러닝 알고리즘으로 학습하여 모델을 생성

- 생성된 모델에 새로운 데이터 값이 주어졌을 때, 레이블 값을 예측

- 분류는 다양한 머신러닝 알고리즘으로 구현할 수 있다.

  - 베이즈 통계와 생성 모델에 기반한 나이브 베이즈
  - 로지스틱 회귀
  - 결정 트리
  - 서포트 벡터 머신
  - 최소 근접 알고리즘
  - 신경망
  - 앙상블
    - 서로 다른(또는 같은) 머신러닝 알고리즘을 결합
    - 대부분 동일한 알고리즘 결합
    - 기본 알고리즘으로 일반적으로 사용하는 것은 Decision Tree

- 앙상블 방법

  - Ensemble Method는 분류에서 가장 각광을 받는 방법 중 하나.
  - 이미지, 영상, 음성, NLP 영역에서는 신경망 기반 딥러닝이 선도하지만
  - 이를 제외한 정형 데이터의 예측 분석 영역에서는 앙상블 방법이 매우 높은 예측 성능으로 인해 애용되고 있다.

  - Bagging
    - Random Forest
      - 상대적 빠른 수행 시간, 유연성 등으로 애용
  - Boosting
    - 근래의 앙상블 방법은 부스팅 방식으로 지속해서 발전 중
    - Gradient Boosting
      - 수행 시간이 너무 오래 걸리는 단점으로 인해 최적화 모델 튜닝이 어렵
      - XgBoost, LightGBM 등 기존 그래디언트 부스팅의 예측 성능을 발전시키면서도, 수행 시간을 단축시킨 알고리즘이 계속 등장하면서, 정형 데이터의 분류 영역에서 가장 활용도가 높은 알고리즘으로 자리 잡았다.

- 즉, 분류의 여러가지 알고리즘 중 대세인 앙상블 방법, 그 중에서도 Boosting 계열 방법이 대세다.

- 앙상블은 매우 많은 여러개의 약한 학습기(예측 성능이 떨어지는)를 결합하여 계속 업데이트하면서 예측 성능을 향상시키는데, 결정 트리 알고리즘이 좋은 약한 학습기가 된다.

## Decision Tree

- 결정 트리는 ML 알고리즘 중 직관적으로 이해하기 쉬운 알고리즘
- 규칙을 학습하여, 트리 기반의 분류 규칙을 만든다.
- 데이터의 어떤 기준을 바탕으로 규칙을 만들어야 효율적인 분류가 될 것인가
  - 이것이 알고리즘의 성능을 크게 좌우한다.
  - 트리를 어떻게 분할할 것인가
- 정보 균일도가 높은 데이터 셋을 먼저 선택할 수 있도록 규칙 조건을 만든다.
  - 예를 들어 노란색 동그라미, 파란색 동그라미 세모 네모, 빨간색 동그라미 세모 네모
  - 색깔이 노란색이냐 아니냐를 기준으로 먼저 나누는게 이득.
- 이러한 정보의 균일도를 측정하는 대표적인 방법
  - 엔트로피를 이용한 정보 이득 지수
  - 지니 계수 (0으로 갈수록 평등)
- 사이킷런에서 구현한 DecisionTreeClassifier는 기본적으로 지니 계수를 이용하여 분할한다.
- 결정 트리 모델의 간단한 알고리즘 순서
  - 데이터 집합의 모든 item들이 같은 분류에 속하는가?
    - Leaf 노드로 만들어서 분류를 결정 
    - 또는
    - 데이터를 분할하는 데 가장 좋은 속성과 분할 기준을 찾는다.
      - 데이터를 분할하여 Branch 노드를 생성
  - 반복

- 결정 트리의 장점
  - 균일도라는 룰을 기반으로 하고 있기 때문에 알고리즘이 쉽고 직관적
  - 시각화로 표현 가능
  - 정보의 균일도만 신경 쓰면 되므로 각 피처의 스케일링, 정규화 같은 전처리 작업이 필요 없다.
- 결정 트리의 단점
  - 과적합으로 정확도가 떨어진다.
  - 서브 트리를 계속 계속 만들다 보면 피처가 많을수록 트리의 깊이가 커지고 복잡해진다.
  - 완벽한 규칙을 만들기 힘들기 때문에 트리의 깊이는 계속 깊어질 수 밖에 없다.
  - 이렇게 되면 실제 상황에 유연한게 대처할 수 없어서 예측 성능이 떨어진다.
  - 따라서 트리의 깊이를 사전에 제한하는 것이 성능 튜닝에 도움이 된다.

## Sklearn의 DecisionTreeClassifier

- 파라미터

  - min_samples_split
    - 노드를 분할하기 위한 최소한의 샘플 데이터 수
  - min_samples_leaf
    - 리프노드가 되기 위한 최소한의 샘플 데이터 수
    - ex) 샘플이 총 3개 이하면 리프로 설정
  - max_features
    - 분할 할 때 고려할 최대 feature 개수
  - max_depth
    - 트리의 최대 깊이
  - max_leaf_nodes
    - 리프노드의 최대 개수

- ```python
  # 결정 트리 기본적인 실행방법
  from sklearn.tree import DecisionTreeClassifier
  from sklearn.datasets import load_iris
  from sklearn.model_selection import train_test_split
  from sklearn.tree import export_graphviz
  import graphviz
  import pandas as pd
  import warnings
  
  warnings.filterwarnings('ignore')
  
  # DecisionTree Classifier 생성
  dt_clf = DecisionTreeClassifier(random_state=156)
  
  # 붓꽃 데이터를 로딩하고, 학습과 테스트 데이터 셋으로 분리
  # train_test_split() 사용
  iris_data = load_iris()
  X_train , X_test , y_train , y_test = train_test_split(iris_data.data, iris_data.target, test_size=0.2, random_state=11)
  
  # DecisionTreeClassifer 학습시키기
  dt_clf.fit(X_train, y_train)
  
  # export_graphviz()의 호출 결과로 out_file로 지정된 tree.dot 파일을 생성함. 
  export_graphviz(
      dt_clf,
      out_file="tree.dot",
      class_names=iris_data.target_names,
      feature_names = iris_data.feature_names,
      impurity=True,
      filled=True
  	)
  
  df = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)
  df['label'] = iris_data.target
  df['labels'] = df.label.apply(lambda x : iris_data.target_names[x])
  df.loc[30:80,:]
  
  # 위에서 생성된 tree.dot 파일을 Graphviz 읽어서 Jupyter Notebook상에서 시각화 
  with open("tree.dot") as f:
      dot_graph = f.read()
  graphviz.Source(dot_graph)
  
  import seaborn as sns
  import numpy as np
  %matplotlib inline
  
  # feature importance 추출 
  print("Feature importances:\n{0}".format(np.round(dt_clf.feature_importances_, 3)))
  
  # feature별 importance 매핑
  for name, value in zip(iris_data.feature_names , dt_clf.feature_importances_):
      print('{0} : {1:.3f}'.format(name, value))
  
  # feature importance를 column 별로 시각화 하기 
  sns.barplot(x=dt_clf.feature_importances_ , y=iris_data.feature_names)
  ```

- 결정 트리 규칙 시각화 Graphviz
  - DecisionTreeClassifier는 feature의 중요 역할 지표를 제공한다.
    - feature_importances_

- 하이퍼 파라미터 설정을 잘 해줘야한다.

- ```python
  # 생성된 모델의 예측 정확도 측정하기
  from sklearn.metrics import accuracy_score
  
  dt_clf.fit(X_train, y_train)
  pred = dt_clf.predict(X_test)
  print(accuracy_score(y_test, pred))
  ```

- ```python
  # DecisionTreeClassifier 기본 하이퍼 파라미터
  {
      'ccp_alpha': 0.0, 
      'class_weight': None, 
      'criterion': 'gini', 
      'max_depth': None, 
      'max_features': None, 
      'max_leaf_nodes': None, 
      'min_impurity_decrease': 0.0, 
      'min_samples_leaf': 1, 
      'min_samples_split': 2, 
      'min_weight_fraction_leaf': 0.0, 
      'random_state': 156, 
      'splitter': 'best'
  }
  # 보통 depth, samples, max_features, max_leaf_nodes 건든다.
  ```

- 위 파라미터를 잘 설정해 줘야 괜찮은 모델이 나온다.

- 파라미터 설정에 따라서 모델의 예측 정확도가 많이 달라지므로 여러가지 파라미터로 모델을 생성해보고 제일 예측도가 높도록 하는 파라미터를 사용하면 된다.

- 이를 도와주는 것이 GridSearchCV 이다.

## GridSearchCV

- ```python
  from sklearn.model_selection import GridSearchCV
  
  params = { # 여기에 실험해보고 싶은 파라미터들을 리스트 형식으로 넣으면 된다.
      'max_depth' : [ 6, 8 ,10, 12, 16 ,20, 24]
  }
  
  grid_cv = GridSearchCV(
      dt_clf, 
      param_grid=params, 
      scoring='accuracy', 
      cv=5, # 교차검증을 위한 fold 횟수
      verbose=1 
  	)
  
  grid_cv.fit(X_train , y_train)
  print('GridSearchCV 최고 평균 정확도 수치:{0:.4f}'.format(grid_cv.best_score_))
  print('GridSearchCV 최적 하이퍼 파라미터:', grid_cv.best_params_)
  
  # GridSearchCV객체의 cv_results_ 속성을 DataFrame으로 생성. 
  cv_results_df = pd.DataFrame(grid_cv.cv_results_)
  
  # max_depth 파라미터 값과 그때의 테스트(Evaluation)셋, 학습 데이터 셋의 정확도 수치 추출
  cv_results_df[['param_max_depth', 'mean_test_score']]
  ```

---

## 앙상블 학습

- 여러개의 분류기를 생성하고 그 예측을 결합함으로써 더 정확한 최종 예측을 도출하는 기법
- 앙상블 알고리즘의 대표
  - 랜덤 포레스트
  - 그래디언트 부스팅
- 부스팅 계열의 앙상블 알고리즘의 강세로 XGboost, LightGBM 같은 더 좋은 앙상블 알고리즘이 탄생 됨
- 쉽고 편하고 강력한 성능
- 앙상블 학습의 유형
  - Voting
    - 여러 개의 분류기가 투표를 통해 최종 예측 결과를 결정
    - 서로 다른 알고리즘 분류기
    - Hard Voting
      - 다수결 원칙
    - Soft Voting
      - 레이블 값 결정 확률을 모두 더하고 평균해서 이들 중 가장 높은 레이블 값 선정
      - 각 분류기마다 답으로 결정내린 결과값 확률들의 평균한다는 말임
      - 일반적인 voting 방법
  - Bagging
    - 여러 개의 분류기가 투표를 통해 최종 예측 결과를 결정
    - 서로 동일한 알고리즘 분류기
    - but 데이터 샘플링을 서로 다르게 가져감
    - 배깅 방식의 대표
      - Random Forest
  - Boosting
    - 여러 개의 분류기가 순차적으로 학습
    - 앞에서 학습한 분류기가 예측이 틀린 데이터에 대해서 올바르게 예측할 수 있도록 다음 분류기에는 가중치를 boosting 하면서 학습
    - 분류기의 점진적 개선
    - 대표적인 부스팅 모듈
      - 그래디언트 부스트
      - XGBoost
      - LightGBM
  - Stacking
    - 여러 가지 다른 모델의 예측 결괏값을 다시 학습 데이터로 만들어서 다른 모델로 재학습시켜서 결과를 예측하는 방법

## Voting

- 여러 분류기 합쳐서 보팅한다고 해서 무조건 예측 성능이 향상되지는 않는다.
- 개쩌는 분류기 하나랑 개구대기 분류기랑 합쳐서 보팅하면...
- 그냥 개쩌는 분류기 사용하는게 낫잖음
- 근데 배깅이랑 부스팅 앙상블 기법은 보통 하나보다 합친 경우가 더 나은경우가 많다.

## Bagging

- 대부분 결정 트리 알고리즘 기반
- 분류기 결합을 통해 단일 결정 트리 모델의 단점을 극복 가능
- 랜덤 포레스트
  - 배깅 : 같은 알고리즘으로 여러 개의 분류기 만들어서 Voting 하기
  - 은근 빠름
  - 전체 데이터 셋에서 샘플링을 통해 학습
  - bootstrapping (부트스트래핑)
    - bootstrap aggregating을 줄여서 bagging
    - 여러 개의 데이터 세트를 중첩을 허락하여 분리하는 것
  - 결정 트리 기반의 앙상블 단점 
    - 하이퍼 파라미터가 너무 많아서 튜닝하는데 시간이 많이 걸린다.

## Boosting

- 대부분 결정 트리 알고리즘 기반

- 분류기 결합을 통해 단일 결정 트리 모델의 단점을 극복 가능

- 여러 개의 weak learner를 순차적으로 학습-예측

- 앞에서 잘못 예측한 데이터를 참고하여

- 다음 분류기에는 저번에 잘못 예측한 거를 제대로 예측할 수 있도록 가중치를 부여하여 학습하는 원리

- 결합 후 예측

- GBM

  - 경사 하강법을 이용한 boosting 기법

  - GradientBoostingClassifier

  - 분류 말고 회귀도 가능

  - ```python
    from sklearn.ensemble import GradientBoostingClassifier
    import time
    import warnings
    warnings.filterwarnings('ignore')
    
    X_train, X_test, y_train, y_test = get_human_dataset()
    
    # GBM 수행 시간 측정을 위함. 시작 시간 설정.
    start_time = time.time()
    
    gb_clf = GradientBoostingClassifier(random_state=0)
    gb_clf.fit(X_train , y_train)
    gb_pred = gb_clf.predict(X_test)
    gb_accuracy = accuracy_score(y_test, gb_pred)
    
    print('GBM 정확도: {0:.4f}'.format(gb_accuracy))
    print("GBM 수행 시간: {0:.1f} 초 ".format(time.time() - start_time))
    ```

- 순차적 학습을 해야하므로 병렬처리가 불가능해서 보팅이나 배깅보다 느리당;;

## XGBoost

- extra gradient boost

- 트리 기반의 앙상블 학습에서 가장 각광받고 있는 알고리즘 중 하나

- 병렬 가능;; GBM의 단점을 보완햇따

- 장점

  - 뛰어난 예측 성능
  - GBM 대비 빠른 수행 시간
  - 과적합 규제
  - 나무 가지치기
    - 의미없는 분할을 줄인다.
  - 자체 내장된 교차 검증
  - 결손값 자체 처리

- XGBClassifier

- ```python
  # xgb 파라미터
  {
      'objective': 'binary:logistic', # 다중 분류일 때는 'multi:softmax'
      'use_label_encoder': False, 
      'base_score': None, 
      'booster': None, 
      'callbacks': None, 
      'colsample_bylevel': None, 
      'colsample_bynode': None, 
      'colsample_bytree': None, # 피처 개수와 관련
      'early_stopping_rounds': None, 
      'enable_categorical': False, 
      'eval_metric': None, 
      'gamma': None, 
      'gpu_id': None, 
      'grow_policy': None, 
      'importance_type': None, 
      'interaction_constraints': None, 
      'learning_rate': None, # 학습률, 순차적으로 오류를 보정해 나가는 데 적용하는 계수
      'max_bin': None, 
      'max_cat_to_onehot': None, 
      'max_delta_step': None, 
      'max_depth': None, # 깊이 설정
      'max_leaves': None, 
      'min_child_weight': None, 
      'missing': nan, 
      'monotone_constraints': None, 
      'n_estimators': 100, # weak learner의 개수
      'n_jobs': None, # -1 : 모든 코어 사용
      'num_parallel_tree': None, 
      'predictor': None, 
      'random_state': None, 
      'reg_alpha': None, # 과적합 감소 관련
      'reg_lambda': None, # 과적합 감소 관련
      'sampling_method': None, 
      'scale_pos_weight': None, # 특정 값으로 치우진 데이터셋 균형 관련
      'subsample': None, # 데이터 샘플링 비율 0.3이면 전체 데이터셋의 30프로
      'tree_method': None, 
      'validate_parameters': None,
      'verbosity': None
  }
  ```

- 좋은 알고리즘 일 수록 파라미터 튜닝에 들어가는 노력 대비 성능 향상 효과가 미미하다.

- 피처의 수가 매우 많거나, 피처 간 상관관계 정도가 크거나, 데이터set의 형태에 따라 파라미터 튜닝이 들어간다.

- XGBoost와 LightGBM은 조기 중단 기능이 있어서 n_estimators 지정해 놨어도, 부스팅을 진행하다가 더 이상 앞 오류가 개선되지 않으면 반복 알아서 중지한다.

  - 조기 중단이란 예를들어서 진행 중인데 20번 째 진행한게 가장 성능이 좋았다 치자 근데 계속 진행해도 20번 째 보다 나은게 안나오는거임;; 그러면 30번만 더 하고 꺼라 이런식으로...
  - 설정해두면 50번째까지도 더 나은거 안나오면 걍 꺼버림

- ```python
  # sklearn xgboost 사용법 기본
  # 사이킷런 래퍼 XGBoost 클래스인 XGBClassifier 임포트
  from xgboost import XGBClassifier
  
  xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
  xgb_wrapper.fit(X_train, y_train) # 학습 시키고 ~
  w_preds = xgb_wrapper.predict(X_test) # 예측 결과 두구두구두구
  w_pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1] # 이건 일단 무시
  ```

- ```python
  # 조기 중단 관련은 fit() 안에 파라미터 입력하면 됨
  from xgboost import XGBClassifier
  
  xgb_wrapper = XGBClassifier(n_estimators=400, learning_rate=0.1, max_depth=3)
  evals = [(X_test, y_test)]
  xgb_wrapper.fit(X_train, y_train, 
                  early_stopping_rounds=100, 
                  eval_metric="logloss", 
                  eval_set=evals, # 평가 set
                  verbose=True)
  
  ws100_preds = xgb_wrapper.predict(X_test)
  ws100_pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1]
  ```

- ```python
  # 피처 중요도 결정하는 기준에 대해서
  sns.barplot(x=xgb_wrapper.feature_importances_, y=dataset.feature_names)
  # 여기서 애초에 xgb_wrapper를 만들 때, 파라미터로 importance_type='' 넣어줘야함
  xgb_clf = XGBClassifier(importance_type='gain')
  # 이렇게
  ```

- XGBoost에서 지원하는 importance 타입

  - Gain / Total gain
    - 기본으로 지정되어 있는 타입
    - 해당 feature가 모델 예측에 어느정도 영향을 미쳤는가를 측정하는 방법
    - 노드가 특정 feature로 분기되었을 때 얻는 성능 상의 이득
    - Gain 타입은 feature가 사용된 전체 노드의 평균 gain 
    - Total gain 타입은 feature가 사용된 전체 노드의 gain의 총합입니다.
  - Cover / Total cover
    - Cover 타입은 해당 feature와 관련된 샘플의 상대적인 개수
    - 예를 들어 4개의 feature를 가진 100개의 샘플을 3개의 의사결정나무로 훈련시키고 feature 1이 10/5/2 개의 샘플을 각각 tree1/tree2/tree3 에서 구분했다고 가정했을 때 feature 1의 절대적인 cover 타입 개수는 17
    - Cover 타입은 해당 feature가 관여한 샘플의 평균 수
    - Total cover 타입은 총합입니다.
  - Weight
    - Weight 타입은 해당 feature가 노드 분기에 사용된 횟수
    - 예를 들어 feature 1이 분기 2/1/3 회만큼 tree1/tree2/tree3 에 사용되었을 때 weight 타입의 feature1 importance는 6

## LightGBM

- XGBoost 에서 파라미터 튜닝하다보면 그래도 오래걸림;;;;;;;;

- GBM 보단 빠르지

- 대용량 데이터의 경우 CPU 코어 많은 컴에서 병렬처리해서 돌려야 좋지

- LightGBM 개념

  - 일반 GBM 계열의 트리 분할 방법과 다르게 리프 중심 트리 분할(Leaf Wise) 방식을 사용한다.
  - 대부분은 깊이를 줄이기 위해 균형적으로 나눈다 (Level Wise)
  - 왜냐면 최대한 균형 잡힌 트리를 유지하면서 분할하여, 깊이를 최소화하면
    - 오버피팅에 더 강한 구조를 가진다고 알려져있어서..
    - 대신 균형을 맞추는데 시간이 걸린다
  - LightGBM은 균형 안맞춤
    - 최대 손실 값을 가지는 리프 노드를 지속적으로 분할하면서 트리를 생성하면
    - 학습할수록 균형 맞추는 거보다 예측 오류 손실을 최소화 할 수 있다.

- 특징

  - XGBoost 보다 학습에 걸리는 시간이 적다.
  - 메모리 사용량도 적다
  - 예측 성능은 별 차이 없다.
  - XGBoost 보다 2년 뒤에 만들어져서 단점 보완
  - 데이터 set가 적은 경우에는 과적합이 발생하기 쉽다. 만 건 이하
  - 병렬 컴퓨팅 기능 제공, GPU까지 지원;;

- ```python
  # LightGBM 파라미터
  {
      'boosting_type': 'gbdt',
      'class_weight': None,
      'colsample_bytree': 1.0,
      'importance_type': 'split',
      'learning_rate': 0.05,
      'max_depth': -1, # 이것도 건듬
      'min_child_samples': 20, # 리프노드가 되기 위한 최소한의 샘플 데이터 수 ex) 샘플이 총 3개 이하면 리프로 설정 여기 많이 건듬
      'min_child_weight': 0.001,
      'min_split_gain': 0.0,
      'n_estimators': 400,
      'n_jobs': -1,
      'num_leaves': 31, # 트리가 가질 수 있는 최대 리프 개수. 여기 많이 건듬
      'objective': None,
      'random_state': None,
      'reg_alpha': 0.0,
      'reg_lambda': 0.0,
      'silent': 'warn',
      'subsample': 1.0,
      'subsample_for_bin': 200000,
      'subsample_freq': 0
  }
  ```

- 학습률을 작게하면서 부스팅 횟수 늘리는 것은 기본적인 튜닝 방법

- 부스팅 횟수가 너무 많으면 과적합 이슈가 있을 수 있음

- ```python
  # lightgbm 은 feature 중요도 시각화 할 때 걍 이거 쓰는게 나은 듯
  from lightgbm import plot_importance
  import matplotlib.pyplot as plt
  %matplotlib inline
  
  fig, ax = plt.subplots(figsize=(10, 12))
  plot_importance(lgbm_wrapper, ax=ax)
  plt.savefig('lightgbm_feature_importance.tif', format='tif', dpi=300, bbox_inches='tight')
  ```

## 하이퍼 파라미터 튜닝

- GridSearchCV를 사용해왔는데
- 이거 사실 별로임
- 튜닝 할 파라미터 개수가 많으면 진짜 개느림

- 베이지안 최적화를 파라미터 튜닝에 적용할 수 있도록 해주는 패키지

  - HyperOpt, Bayesian Optimization, Optuna 등

- HyperOpt 활용 주요 로직

  - 입력 변수명과 입력값의 Search Space 설정
  - 목적 함수 설정
  - 목적 함수의 반환 최솟값을 가지는 최적 입력값을 유추

- ```python
  from hyperopt import hp
  
  # -10 ~ 10까지 1간격을 가지는 입력 변수 x와 -15 ~ 15까지 1간격으로 입력 변수 y 설정.
  search_space = {'x': hp.quniform('x', -10, 10, 1), 'y': hp.quniform('y', -15, 15, 1) }
  
  from hyperopt import STATUS_OK
  
  # 목적 함수를 생성. 
  # 변숫값과 변수 검색 공간을 가지는 딕셔너리를 인자로 받고, 특정 값을 반환
  def objective_func(search_space): # 걍 정의역 공역 입력하라는 뜻;
      x = search_space['x']
      y = search_space['y']
      retval = x**2 - 20*y
      return retval
  
  from hyperopt import fmin, tpe, Trials
  import numpy as np
  
  # 입력 결괏값을 저장한 Trials 객체값 생성.
  trial_val = Trials()
  
  # 목적 함수의 최솟값을 반환하는 최적 입력 변숫값을 5번의 입력값 시도(max_evals=5)로 찾아냄.
  best_01 = fmin(
      fn=objective_func, 
      space=search_space, 
      algo=tpe.suggest, 
      max_evals=5, 
      trials=trial_val, 
      rstate=np.random.default_rng(seed=0)
  	)
  print('best:', best_01)
  
  print(trial_val.vals)
  print(trial_val.results)
  
  # 표로 편하게 보자 x, y, 예측값 (현재 z = f(x,y) 형태임)
  import pandas as pd
  
  # results에서 loss 키값에 해당하는 밸류들을 추출하여 list로 생성. 
  losses = [loss_dict['loss'] for loss_dict in trial_val.results]
  
  # DataFrame으로 생성.
  result_df = pd.DataFrame({'x': trial_val.vals['x'], 'y': trial_val.vals['y'], 'losses': losses})
  result_df
  ```

- 실제로 HyperOpt를 이용하며 XGBoost 파라미터 최적화 해보자

  - HyperOpt는 입력, 반환 값이 모두 실수형이라 int로 형변환 해야함

  - ```python
    # 전체 데이터 중 80%는 학습용 데이터, 20%는 테스트용 데이터 추출
    X_train, X_test, y_train, y_test=train_test_split(X_features, y_label, test_size=0.2, random_state=156 )
    
    # 앞에서 추출한 학습 데이터를 다시 학습과 검증 데이터로 분리
    X_tr, X_val, y_tr, y_val= train_test_split(X_train, y_train, test_size=0.1, random_state=156 )
    
    from hyperopt import hp
    
    # max_depth는 5에서 20까지 1간격으로, 
    # min_child_weight는 1에서 2까지 1간격으로,
    # colsample_bytree는 0.5에서 1사이, 
    # learning_rate는 0.01에서 0.2 사이 정규 분포된 값으로 검색.
    xgb_search_space = {
        'max_depth': hp.quniform('max_depth', 5, 20, 1), 
        'min_child_weight': hp.quniform('min_child_weight', 1, 2, 1),
        'learning_rate': hp.uniform('learning_rate', 0.01, 0.2),
        'colsample_bytree': hp.uniform('colsample_bytree', 0.5, 1),
    }
    
    from sklearn.model_selection import cross_val_score
    # cross_val_score 뭔데 ? ㅋ
    from xgboost import XGBClassifier
    from hyperopt import STATUS_OK
    
    # fmin()에서 입력된 search_space 값으로 입력된 모든 값은 실수형임.
    # XGBClassifier의 정수형 하이퍼 파라미터는 정수형 변환을 해줘야 함.
    # 정확도는 높을수록 더 좋은 수치임. -1 * 정확도를 곱해서 큰 정확도 값일수록 최소가 되도록 변환
    def objective_func(search_space):
        # 수행 시간 절약을 위해 nestimators는 100으로 축소
        xgb_clf = XGBClassifier(
            n_estimators=100, 
            max_depth=int(search_space['max_depth']),
            min_child_weight=int(search_space['min_child_weight']),
            learning_rate=search_space['learning_rate'],
            colsample_bytree=search_space['colsample_bytree'],
            eval_metric='logloss'
        	)
        
    	accuracy = cross_val_score(xgb_clf, X_train, y_train, scoring='accuracy', cv=3)
        # accuracy는 cv=3 개수만큼 roc-auc 결과를 리스트로 가짐. 이를 평균해서 반환하되 -1을 곱함.
        return {'loss':-1 * np.mean(accuracy), 'status': STATUS_OK}
    
    from hyperopt import fmin, tpe, Trials
    
    trial_val = Trials()
    best = fmin(
        fn=objective_func,
        space=xgb_search_space,
        algo=tpe.suggest,
        max_evals=50, # 최대 반복 횟수를 지정합니다.
        trials=trial_val, 
        rstate=np.random.default_rng(seed=9)
    )
    print('best:', best)
    
    # 최적의 파라미터로 다시 모델을 만들어보장
    
    xgb_wrapper = XGBClassifier(n_estimators=400,
                                learning_rate=round(best['learning_rate'], 5),
                                max_depth=int(best['max_depth']),
                                min_child_weight=int(best['min_child_weight']),
                                colsample_bytree=round(best['colsample_bytree'], 5)
                               )
    
    evals = [(X_tr, y_tr), (X_val, y_val)]
    xgb_wrapper.fit(X_tr, y_tr, 
                    early_stopping_rounds=50, # 조기 종료 
                    eval_metric='logloss',
                    eval_set=evals, 
                    verbose=True)
    
    preds = xgb_wrapper.predict(X_test)
    pred_proba = xgb_wrapper.predict_proba(X_test)[:, 1]
    
    get_clf_eval(y_test, preds, pred_proba)
    ```

  - 