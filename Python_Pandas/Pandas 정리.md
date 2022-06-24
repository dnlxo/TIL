# Pandas 정리

- 시작

  - ```python
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    help() # 이용하며 도움말 확인 가능
    ```

- Pandas의 데이터 구조

  - Series
    - 1차원 데이터 구조
    - 변수명 : s, sr
  - DataFrame
    - 2차원 데이터 구조
    - 변수명 : df

- Series

  - pd.Series()로 생성
  - pd.Series([1,2,3,4])
    - 인덱스 지정 안할 시 0부터 시작
  - pd.Series([1,2,3,4], index=['a','b','c','d'])
  - Series는 index와 values를 가진다.
  - s.index
  - s.values
  - 요소 조회 가능 (인덱스 명 또는 인덱스 순서)
  - s['a']
  - s[0]
  - 파이썬의 딕셔너리와 유사하다.
  - 따라서 파이썬의 딕셔너리로 Series 생성 가능
  - 딕셔너리에 index : value 로 담고, pd.Serise(dict) 하면 됨
  - 딕셔너리와 차이점은 시리즈는 순서가 있따.
  - 그리고 시리즈 자체에 곱하기 1000 같은걸 하면, 알아서 각각의 value들에 1000이 다 곱해진다.

- DataFrame

  - 엑셀 스프레드시트, 데이터베이스등과 동일한 2차원 구조
  - 가장 많이 활용하게될 구조
  - Series가 합쳐진 형태
  - 2차원 리스트를 넣으면 생성 됨
  - pd.DataFrame([['Belgium', 'Brussels', 11190846],
            ['India', 'New Delhi', 1303171035],
            ['Brazil', 'Brasília', 207847528]])
  - 컬럼명 정의하는 법
    - df = pd.DataFrame(data, columns=['Country', 'Capital', 'Population'])
    - 딕셔너리로 넘겨주면 컬럼명 같이 전달가능
      - pd.DataFrame({'Country': ['Belgium', 'India', 'Brazil'],
                'Capital': ['Brussels', 'New Delhi', 'Brasília'],
                'Population': [11190846, 1303171035, 207847528]})

  - 인덱스 변경하는 법
    - df_2 = pd.DataFrame(data, index=['aa', 'bb', 'cc'])
  - 데이터프레임 하나의 column은 Series이다.
  - DataFrame의 속성
    - index
    - columns
    - dtypes
    - values
    - 합쳐서 info()
  - 인덱스는 여러개가 가능하다
    - df.set_index(['Country', 'Capital'])

- Import, Export

  - csv, excel, sql, json 등
  - pd.read_~
  - df.to_~

- 행삭제 (axis = 0)

  - df.drop(1)
  - df.drop([0,1])

- 열삭제 (axis = 1)
  - df.drop('Country', axis=1)
- 여러 함수들
  - df.describe()
  - df.head()
  - df.sort_values()
  - df.isnull()
  - df.isnull().any(axis=0)
  - df.isnull().any().any()
  - df.copy()
- loc 인덱싱
  - loc를 활용해서 인덱싱 하는 방법은 헷갈일 일이 없어서 편하다. 
  - 첫 번째에는 인덱싱할 row를 넣고, 
  - 두 번째에는 인덱싱할 column을 넣으면 된다. 
  - row나 column의 이름을 넣어도 되고, 리스트를 넣어도 되며, 리스트 슬라이싱을 넣어도 원하는 결과가 나온다. 
  - row나 column자리에 : 를 쓰게되면 전체를 인덱싱한다는 뜻이다. 
  - df.loc[:, "나이"]를 한다면 모든 row의 나이를 인덱싱하게 된다.
- apply 함수
  - df['새로운열'] = df.column.apply()
  - 특정 column에 내가 만든 함수를 적용해서 새로운 열로 생성
- groupby().함수적용
- 판다스 column 조회
  - 칼럼 조회할때 .보다는 [ ]을 사용을 권장함
    1. 칼럼명에 스페이스가 들어가도 된다
    2. 칼럼명이 메소드명과 동일해도 된다
    3. 변수와 함께 사용할 수 있다
    4. 칼럼명이 문자가 아니라도 된다
    5. 새로운 칼럼을 선언할 수 있다
    6. 여러 칼럼을 동시에 조회할 수 있다
    7. . 을 통한 조회는 []을 통한 조회의 부분집합이다(일부분의 기능만 가져옴)
    8. 항상 사용가능한 방법을 쓰는것이 낫다
    9. 파이썬에서 원소를 조회하는 일반적인 방법이 [] 이다
- boolean 조건 걸 때, and 말고 & 써야함 (or not 도 마찬가지 |, ~)
- 