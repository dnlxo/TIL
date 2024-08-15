## 03_Evaluation

- 모델의 평가 지표
- 분류모델의 평가 지표 (특히 이진 분류에서의)
- 정확도 Accuracy
- 정밀도 Precision
- 오차행렬 Confusion Matrix
- 재현율 Recall
- F1 score
- ROC AUC

- 보통 특이사항을 양성으로 분류 (1로)

  - 암이 걸린거면 1

  - 사기행위면 1

- 모델의 평가 방법

  - TP : 암인데 암이라고 함

  - TN : 암이 아닌데, 암이 아니라고 함

  - FP : 암이 아닌데, 암이라고 함

  - FN : 암인데, 암이 아니라고 함

  - 보통 FP와 FN이 문제가 된다.

    - 둘의 중요도 차이는 크다.

  - 정확도 (Accuracy)

    - 만든 모델이 예측을 올바르게 한 비율
    - (TP + TN) / (TP + TN + FP + FN)

  - 정밀도 (Precision)

    - TP / (TP + FP)
    - 암이 맞다고 진단 내린 판단 중에서
      - 실제로 암이 맞는 경우
    - 이것을 정밀도라고 함

  - 재현률 (Recall)

    - TP / (TP + FN)
      - 실제로 암이 맞는 애들중에
        - 암이라고 맞춘 확률

  - 암의 예시에서는 

    - 실제로 암인데 암이 아니라고하면 큰일남;;
    - 따라서 재현률이 극히 높아야함 (FN이 극히 낮아야함)

  - 정밀도와 재현률 예시

    - 스팸메일이 있을 때,
    - TP = 8 (스팸 인걸 스팸 이라고)
    - TN = 17 (스팸 아닌걸 스팸 아니라고)
    - FP = 2 (스팸 아닌걸 스팸이라고)
    - FN = 3 (스팸 인걸 스팸 아니라고)
    - 이라고 하자
    - 더 신경써야하는 건 뭘까?
      - 스팸 아닌걸 스팸이라고 하면 큰일난다;;
      - 따라서 정밀도가 극히 높아야한다.
    - raising the classification threshold reduces false positives, thus raising precision.

    - 스팸 예시에서
    - threshold를 raise 한다는 말은
      - 각 data마다 spam일 확률이 0.7 넘을 경우에만 스팸으로 분류
      - 그럼? 스팸으로 식별하는 data가 적어진다..
      - 스팸 아니라고 식별하는 data가 많아진다.
      - 그럼 보통 FP는 감소하고, FN은 증가한다.

- ROC-AUC

  - **receiver operating characteristic curve**
  - 모든 분류 임계값에서 분류 모델의 성능을 보여주는 그래프입니다.
  - 이 곡선은 두 개의 매개변수를 표시합니다.
    - TPR : 재현률 ( TP / (TP + FN) ) 
      - 실제 스팸인 메일이 스팸판정 받는 확률
      - Sensitivity
      - 민감도
    - FPR : ( FP / (FP + TN) ) 
      - 스팸 아닌 메일이 스팸판정 받을 확률
      - Specificity
      - 특이도
  - ROC 곡선은 다양한 분류 임계값에서 TPR 대 FPR을 표시합니다. 
  - 분류 임계값을 낮추면 더 많은 항목이 양성으로 분류되어 거짓 양성과 참 양성이 모두 증가합니다.

- 정밀도와 재현율이 모두 높은 수치를 보이면 가장 좋다.

- 정밀도와 재현율 둘 중 하나는 높고 하나는 낮으면 별루다.

- ```python
  from sklearn.metrics import accuracy_score, precision_score , recall_score , confusion_matrix
  
  # 정확도 정밀도 재현율 한 번에 구하기
  def get_clf_eval(y_test , pred):
      confusion = confusion_matrix( y_test, pred)
      accuracy = accuracy_score(y_test , pred)
      precision = precision_score(y_test , pred)
      recall = recall_score(y_test , pred)
      print('오차 행렬')
      print(confusion)
      print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}'.format(accuracy , precision ,recall))
  ```

- 분류 업무 특성상 정밀도가 엄청 중요하거나 재현율이 엄청 중요한 경우가 있다.

- 하지만 정밀도와 재현율은 상호 보완적인 평가 지표이기 때문에

- 한 쪽을 강제로 높이면 한 쪽 수치는 떨어지기 쉽다. (Trade-off)

- 분류 작업은 해당 데이터가 0일 확률, 1일 확률을 각각 구해서, 보통 0.5를 기준으로 라벨을 결정을 한다.

- 이 기준값(임곗값)을 조정할 수 가 있다. threshold

- 각 데이터 별로 예측 확률을 반환하는 메서드가 있다.

  - predict_proba()
  - 학습 이후에 호출하면 됨

- 임계값 변환

  - ```python
    from sklearn.preprocessing import Binarizer
    
    #Binarizer의 threshold 설정값. 분류 결정 임곗값임.  
    custom_threshold = 0.5
    
    # predict_proba( ) 반환값의 두번째 컬럼 , 즉 Positive 클래스 컬럼 하나만 추출하여 Binarizer를 적용
    pred_proba_1 = pred_proba[:,1].reshape(-1,1)
    
    binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_1) 
    custom_predict = binarizer.transform(pred_proba_1)
    
    get_clf_eval(y_test, custom_predict)
    ```

- F1 score

  - 정밀도와 재현율을 결합한 지표

  - 한쪽으로 치우치지 않을 때 F1 스코어가 높게 나온당

  - ```python
    from sklearn.metrics import f1_score 
    f1 = f1_score(y_test , pred)
    ```

- ROC Curve, AUC

  - threshold...
    - 레이블 1 일 확률이 0.7 이상이면 레이블 1로 분류

### 실습

```python
# 기본적인 import
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import f1_score, confusion_matrix, precision_recall_curve, roc_curve
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data['Outcome'].value_counts())
diabetes_data.head(3)

# 병에 걸렸으면 1 아니면 0
# 데이터 이상치 수정 (feature 값이 0이 나오면 이상한 데이터임;; 뭘로 바꿔줄까 보통 평균?)

# 0값을 검사할 피처명 리스트 객체 설정
zero_features = ['Glucose', 'BloodPressure','SkinThickness','Insulin','BMI']

# 전체 데이터 건수
total_count = diabetes_data['Glucose'].count()

# 피처별로 반복 하면서 데이터 값이 0 인 데이터 건수 추출하고, 퍼센트 계산
for feature in zero_features:
    zero_count = diabetes_data[diabetes_data[feature] == 0][feature].count()
    print('{0} 0 건수는 {1}, 퍼센트는 {2:.2f} %'.format(feature, zero_count, 100*zero_count/total_count))
    
# zero_features 리스트 내부에 저장된 개별 피처들에 대해서 0값을 평균 값으로 대체
mean_zero_features = diabetes_data[zero_features].mean()
diabetes_data[zero_features]=diabetes_data[zero_features].replace(0, mean_zero_features)

X = diabetes_data.iloc[:, :-1]
y = diabetes_data.iloc[:, -1]

# StandardScaler 클래스를 이용해 피처 데이터 세트에 일괄적으로 스케일링 적용
# 피쳐들 간의 범위 차이가 많이 날 때
scaler = StandardScaler( )
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size = 0.2, random_state = 156, stratify=y)

# 로지스틱 회귀로 학습, 예측 및 평가 수행. 
lr_clf = LogisticRegression()
lr_clf.fit(X_train , y_train)
pred = lr_clf.predict(X_test)
pred_proba = lr_clf.predict_proba(X_test)[:, 1]

get_clf_eval(y_test , pred, pred_proba)

# 임계값 바꿔가며 학습결과를 보기
from sklearn.preprocessing import Binarizer

def get_eval_by_threshold(y_test , pred_proba_c1, thresholds):
    # thresholds 리스트 객체내의 값을 차례로 iteration하면서 Evaluation 수행.
    for custom_threshold in thresholds:
        binarizer = Binarizer(threshold=custom_threshold).fit(pred_proba_c1) 
        custom_predict = binarizer.transform(pred_proba_c1)
        print('임곗값:',custom_threshold)
        get_clf_eval(y_test , custom_predict, pred_proba_c1)
        
thresholds = [0.3 , 0.33 ,0.36,0.39, 0.42 , 0.45 ,0.48, 0.50]
pred_proba = lr_clf.predict_proba(X_test)
get_eval_by_threshold(y_test, pred_proba[:,1].reshape(-1,1), thresholds )

# 임곗값를 0.48로 설정한 Binarizer 생성
binarizer = Binarizer(threshold=0.48)

# 위에서 구한 lr_clf의 predict_proba() 예측 확률 array에서 1에 해당하는 컬럼값을 Binarizer변환. 
pred_th_048 = binarizer.fit_transform(pred_proba[:, 1].reshape(-1,1)) 

get_clf_eval(y_test , pred_th_048, pred_proba[:, 1])

```

