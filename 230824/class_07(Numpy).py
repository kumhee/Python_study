# 2차원 배열에서 각 행과 각 열의 합을 구하여 리스트로 반환해보기

# 1 2 3
# 4 5 6
# 7 8 9

# 6 15 24
# 12 15 18

import numpy as np

a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

for i in range(len(a)):
    sum = a[i].sum()
    print(a[i].sum())


arr = a.transpose()
print(arr)
for i in range(len(arr)):
    sum = arr[i].sum()
    print(arr[i].sum())



print()
for i in a:
    print(i.sum(),end=" ")
print()

print(a.transpose())

for i in a.transpose():
    print(i.sum(),end=" ")
print()



print()
print(a)
print(a.sum(axis=None)) # 45 None은 축 기준 상관없이 전부 다 더해줌.
print(a.sum(axis=0)) # x축기준 [12 15 18]
print(a.sum(axis=1)) # y축기준 [ 6 15 24]