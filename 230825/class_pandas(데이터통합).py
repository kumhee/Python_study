# 데이터 통합
# 여러개의 데이터셋을 결합해서 단일 데이터 셋으로 만든다.
import pandas as pd

print("concat-------------------------------------")
# concat : 동일한 열 이름을 가진 여러 데이터 프레임을 행 방향(axis = 0)이나 열 방향(axis = 1)으로 결합할 때 사용한다. 
df1 = pd.DataFrame({'A':['A0','A1'], 'B':['B0','B1']})
df2 = pd.DataFrame({'A':['A2','A3'], 'B':['B2','B3']})

row = pd.concat([df1,df2], ignore_index=True)
print(row)

column = pd.concat([df1, df2], axis=1)
print(column)


print("merge-------------------------------------")
# merge : 공통된 열 혹은 인덱스 기준으로 통합된다.
df1 = pd.DataFrame({'Name':['John', 'anna', 'Peter'], 'Age':[28,24,36]})
df2 = pd.DataFrame({'Name':['John', 'anna', 'Peter'], 'City':['New york', 'Paris', 'Seoul']})

res = pd.merge(df1, df2, on='Name')
print(res)


print("join------+-------------------------------")
#Join :  인덱스 기반 결합 작업, 왼쪽으로 조인, how(내부inner, 외부outer, 왼쪽left, 오른쪽right)
df1 = pd.DataFrame({'A':['A0','A1','A2']}, index=['I', 'J', 'K'])
df2 = pd.DataFrame({'B':['B0','B1', 'B2']}, index=['I', 'J', 'K'])

res = df1.join(df2)
print(res)
