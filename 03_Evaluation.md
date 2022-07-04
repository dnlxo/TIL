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

- 