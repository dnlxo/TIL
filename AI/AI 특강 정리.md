# AI 특강 정리

- 1950년 튜링 테스트

  사람이 질문을 하고 (컴퓨터 또는 사람)에게 답변을 받았을 때, 사람인지 컴퓨터인지 구분할 수 있는가? 를 AI를 정의하려고 했다.

  그럼 AI = human-level intelligence 인가? 라는 문제가 생김

  AI를 정의하기보다 AI가 무엇을 할 수 있는지에 초점을 맞추자.

- 자율주행, 필기인식, 자연어처리 등

- 자연어 처리 Sentiment Analysis

  - ex) 영화 리뷰가 긍정적인지 부정적인지 판단하는 프로그램.

    예전에는 단어 기반으로 판단. 최근엔 문맥기준 판단 가능해짐.

  - ex) 기계번역 (번역기) 분야

- 인간과 기계의 대결
  - 1997 딥블루
  - 2011 IBM Watson
  - 2016 알파고

### AI 응용들의 공통점

- Computational Complexity
  - 바둑은 최적해가 존재하는 문제이지만 361의 200승의 경우의 수가 있다.
  - AI 문제의 특징은 최적해를 찾는게 너무 오래걸린다. NP-hard
- Information Complexity
  - 이미지 분류, 문장 번역
  - 많은 데이터를 필요로 한다.

따라서 많은 time/memory와 data가 필요하다.

인공지능 문제의 해결

- Big data
- hardware
- machine learning algorithm

이 있어야 한다.

AI를 배운다는 것

- Type of models
- Art of modeling
- Developing Algorithms

linear classifier 들을 모아서 non-linear 한 결과를.. > 딥러닝

## ML approach

영화 리뷰와 판단기준(Label)을 제공 > 가중치를 계산 후 > output

모델성능 체크 : 맞는지 틀린지 채점을 해줄 Training data 가 필요.

학습하지 않았던 새로운 데이터에 대한 성능이 진짜 성능이다.

이를 위해 generalize 가 필요



## 머신러닝의 종류

low-level 에서 high-level 까지..

- Reflex 모델 (각각의 가중치를 알맞게 설정)
- State 모델 (각각의 국면에 가장 좋은 선택들)
- Variable 모델 (가장 바람직한 value)
- Logic 논리적 문제

학습을 시킬 때 features 를 정해주는게 중요...

feature 벡터를 잘 define 해야 제대로 학습이 되고 결과값을 낼수있다.

새로운 linear feature 를 생성

## 머신러닝의 목적

일어나지 않은 미래의 문제에 대한 답의 오차를 최소화 하는것.. 젤 중요

트레이닝 데이터에 대해 overfitting 된(복잡) 모델은 

트레이닝 데이터에 대한 오차는 줄어들지만, 미래의 데이터에는 오차가 더 커질수있다.

## Our goal is to minimize error on unseen future examples

모델링을 잘해야하고 feature를 잘 찾아야하고 (충분한 양의 데이터) 모델이 너무 복잡해지지 않도록 조심

