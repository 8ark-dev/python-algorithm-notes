**입력 빠르게 받기**

```python
import sys
read = sys.stdin.readline
```
 <br>

 **입출력 시간 측정하기**

```python
import time
start = time.time()

#코드

end = time.time()

print('걸린 시간 : ', end-start)
```

#### 복잡도
- 시간복잡도 : 알고리즘을 위해 필요한 연산의 횟수 <br>
- 공간복잡도 : 알고리즘을 위해 필요한 메모리의 양 <br><br>

시간복잡도와 공간복잡도는 Trade-off관계에 있다. <br>
메모리를 사용해서 시간을 비약적으로 줄이는 방법을 **메모이제이션**이라고 한다. 


시간복잡도에 따른 설계로 문제를 해결할 수 있을 것


#### 파이썬 부동소수점 issue

```
0.1 * 3 === 0.3
False 
```

컴퓨터에서 부동소수점 숫자들은 2진 분수로 표현되기 때문에 위와 같은 상황이 생긴다.