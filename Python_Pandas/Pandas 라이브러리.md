# Pandas 라이브러리

```python
import pandas as pd
data_frame = pd.read_csv('data/friend_list.csv')
```

엑셀이 있는데 데이터 프레임을 쓰는 이유?

1. 프로그램을 만들기 위해
2. Numpy 사용 위해

```python
data_frame.head(n) # 앞에 n개 불러오기
data_frame.tail(n) # 뒤에 n개 불러오기
# column 들은 series 이다.
# data frame은 series 의 집합체
```

## series 만들기

```python
s1 = pd.core.series.Series([1,2,3])
s2 = pd.core.series.Series(['a','b','c'])
# data frame 만들기
pd.DataFrame(data = dict(num = s1, word = s2))
```

| 0    | num  | word |
| ---- | ---- | ---- |
| 1    | 1    | 'a'  |
| 2    | 2    | 'b'  |
| 3    | 3    | 'c'  |

## 데이터를 불러오는 방법

```python
df = pd.read_csv('경로/파일') #txt 파일도 불러와 짐 
# 기본 쉼표 구분 
df = pd.read_csv('경로/파일', delimiter = '\t') # tab 구분
```

## column name 이 없는 데이터인 경우

```python
# 그냥 불러오면 첫 행이 column name 으로 불러와진다 ;;
df = pd.read_csv('경로/파일', header = None)
df.columns = ['name', 'age', 'job']
# 이런 식으로 불러오던지 아니면 한번에
df = pd.read_csv('경로/파일', header = None, names = ['name', 'age', 'job'])
```

## 딕셔너리 자료형을 이용한 data frame 만들기

```python
friend_dict_list = [{'name': 'Jone', 'age': 20, 'job': 'student'},
         {'name': 'Jenny', 'age': 30, 'job': 'developer'},
         {'name': 'Nate', 'age': 30, 'job': 'teacher'}]

df = pd.DataFrame(friend_dict_list)

# 데이터프레임 생성 시, 컬럼의 순서가 뒤바뀔 수 있습니다.
# 아래와 같이 컬럼을 원하시는 순서로 지정하실 수 있습니다.

df = df[['name', 'age', 'job']]
```

OrderedDict 자료구조로 데이터프레임을 생성하면, 컬럼의 순서가 뒤바뀌지 않습니다.

```python
from collections import OrderedDict

friend_ordered_dict = OrderedDict([ ('name', ['John', 'Jenny', 'Nate']),
          ('age', [20, 30, 30]),
          ('job', ['student', 'developer', 'teacher']) ] )

df = pd.DataFrame.from_dict(friend_ordered_dict)
```

## 리스트를 이용한 data frame 만들기

DataFrame.from_records() 를 이용

```python
friend_list = [ ['John', 20, 'student'],['Jenny', 30, 'developer'],['Nate', 30, 'teacher'] ]
column_name = ['name', 'age', 'job']
df = pd.DataFrame.from_records(friend_list, columns=column_name)
```

## 파일로 data frame 저장하기

```python
df.to_csv('파일이름.csv or txt')
# row index 와 column 이름의 저장 방법
df.to_csv('파일이름.csv or txt', header = False, index = False)
# 데이터에 None 값이 있는 경우 None 값을 원하는 값으로 변경하여 저장
df.to_csv('파일이름.csv or txt', header = False, index = False, na_rep = '-')
```

## row 선택하기

|      | name  | age  | job       |
| :--- | :---- | :--- | --------- |
| 0    | John  | 20   | student   |
| 1    | Jenny | 30   | developer |
| 2    | Nate  | 30   | teacher   |

```python
df[1:3] # 1번과 2번 인덱스
df.loc[[0,2]] # 연속되지 않은 row 선택
```

## column 값 조건에 따른 row 선택하기

```python
df[df.age > 25]

df.query('age>25') # 쿼리 사용

df[(df.age >25) & (df.name == 'Nate')]
```

## column filter 하기

|      | 0     | 1    | 2         |
| :--- | :---- | :--- | --------- |
| 0    | John  | 20   | student   |
| 1    | Jenny | 30   | developer |
| 2    | Nate  | 30   | teacher   |

```python
df.iloc[:, 0:2] # 모든 row를 보여주되, column은 0부터 1까지만 출력
df.iloc[:,[0,2]] # 연속되지 않은 column 선택
```

## column 이름으로 filter 하기

|      | name  | age  | job       |
| :--- | :---- | :--- | --------- |
| 0    | John  | 20   | student   |
| 1    | Jenny | 30   | developer |
| 2    | Nate  | 30   | teacher   |

```python
df[['name', 'age']]

df.filter(items=['age', 'job'])

# 같은 것 다른 방법
```

```python
# 원하는 글자를 가진 column 이름들만 선택
# select columns containing 'a'
df.filter(like='a', axis=1) # column 이름 행은 axis 1 이므로..

# 정규식으로 필터도 가능
# select columns using regex
df.filter(regex='b$', axis=1)
```

