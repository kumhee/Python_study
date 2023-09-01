# Numpy
# 과학, 공학 연산을 쉽게 하도록 지원하는 다차원 배얄(multi-dimensional array) 라이브러리
# Numpy를 사용해서 대규모 배열 처리를 쉽게 하도록 하고, 파이썬 List와는 차이가 있다. 

import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([[1,2,3],[4,5,6]])

print(a)
print(b)

# 내부에 연속된 메모리 구조를 가지고 있다. (Array Interface)를 가지고 있고, C를 통해 연산된다. 

# 생성 함수 : np.array(), np.zeros(), np.ones(), np.arange(), np.linspace()
# 변환 함수 : ndarray.reshape(), ndarray.rave(), ndarray.transpose(), ndarray.swapaxes()
# 연산 함수 : np.add(). np.substract(), np.miltiply(), np.divide(), np.sqrt(), np.dot(), np.sum()
#               np.mean(), np.std(), np.max(), np.min(), np.argman(), np.argmin()
# 집계 함수 : ndarray.sum(), ndarray.mean(), ndarray.str(), ndarray.man(), ndarray.min(),
#               ndarray.argmax(), ndarray.argmin()
# 논리 함수 : np.logcal_and(), np.logcal_or(), np.logcal_not()

arr1 = np.zeros(5) #1차원 - 0으로 채우기
print(arr1) #[0. 0. 0. 0. 0.]

arr2 = np.zeros((2,8)) #2차원
print(arr2) #[[0. 0. 0. 0. 0. 0. 0. 0.]
            # [0. 0. 0. 0. 0. 0. 0. 0.]]
            
arr3 = np.zeros((3,3,3)) #3차원
print(arr3)


# ones - 1로 채우기
arr1 = np.ones(5)
print(arr1)

arr2 = np.ones((10,10))
print(arr2)


# empty
arr3 = np.empty(5)
print(arr3)

arr4 = np.empty((3,3))
print(arr4)


# arange
arr1 = np.arange(5) #0부터 5전까지
print(arr1)

arr2 = np.arange(3,10) # 3부터 10 전까지
print(arr2)

arr3 = np.arange(1,10,0.2) #1부터 10까지할껀데, 0.2로 잡아줌.
print(arr3)


# linspace - 구간 나누기
arr1 = np.linspace(0,1,5) #0부터 1까지구간을 5칸으로 나눠줌 - [0.   0.25 0.5  0.75 1.  ]
print(arr1)

arr2 = np.linspace(-10,10,10) 
print(arr2)


# 변환함수
# 배열 형태 변환

# 1차원 배열을 2차원 배열로 변환
arr = np.array([1,2,3,4,5,6])
arr2 = arr.reshape(2,3)
print(arr2)

# 2차원 배열을 1차원 배열로 변환
arr1 = arr2.flatten()
print(arr1)


# 타입변환
# 정수를 실수로 변환
arr_int = np.array([1,2,3])
arr_float = arr_int.astype(float)
print(arr_float) #[1. 2. 3.]

#문자열 배열을 정수열 배열로 변환
arr_str = np.array(['1','2','3'])
arr_int = arr_str.astype(int)
print(arr_int) # [1 2 3]


# 축 변환
b = np.array([[1,2],[3,4],[5,6]])
trans = b
print(trans) #[[1 3 5]
             # [2 4 6]]
print(np.transpose(trans))


# 집계함수
print(b)
print(b.sum())
print(b.mean())
print(b.std()) #표준편차
print(b.max())
print(b.min())
print(b.argmax())
print(b.argmin()) 


# 논리함수
arr1 = np.array([True,False,False,True])
arr2 = np.array([True,True,False,False])
print(np.logical_and(arr1,arr2))
print(np.logical_or(arr1,arr2))
print(np.logical_not(arr1))
print(np.logical_not(arr2))

