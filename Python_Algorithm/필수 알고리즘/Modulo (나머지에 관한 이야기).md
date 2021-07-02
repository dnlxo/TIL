## Modulo (나머지에 관한 이야기)

(A+B) mod C = (A mod C + B mod C) mod C

뺄셈과 곱셈에서도 똑같이 적용이 된다. 증명은 찾아보세요

백준 1629

### 자연수 A를 B번 곱한 수를 C로 나눈 나머지를 구하시오

A, B, C 의 범위가 21억까지라서 분할 정복을 생각해주어야 한다.

의식의 흐름을 잘 따라가면 된다....

1. A^B mod C 는 뭘까 ...?
2. 모듈로 property를 이용하면 (A^(B/2) mod C * A^(B/2) mod C) mod C 겠구나 ...!
3. A^(B/2) mod C 가 뭔지 알면 되겠네..
4. B 를 계쏙 2로 나누다보면 1이 되것네..?
5. A mod C 를 알면 다 알 수 있구나~

```python
# 재귀적으로 구현
def my_mod(A, B) :
		if B == 1 :
      	return A % C
    save = my_mod(A, B//2)
    if B % 2 == 0 : # 짝수의 경우
      	return save * save % C
    else :
        return save * save * (A % C) % C
```

역시 log 시간복잡도는 사기다.

