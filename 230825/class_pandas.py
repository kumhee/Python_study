# Pandas
# 데이터 분석 및 조작을 위한 라이브러리 (Numpy 기반)

import numpy as np
import pandas as pd 

# Series : 1차원 배열 구조
# DataFrame : 2차원 배열 구조

# CSV, Excel, SQL 쿼리

#Series
s = pd.Series([1,3,4, np.nan, 7,8])
print(s)

s = pd.Series([1,3,4, np.nan, 6,8], index=['A','B','C','D','E','F'])
print(s)
print(s['C'])

s1 = pd.Series([10,20,30,40,50])
print(s1)
print(s1.index)
print(s1.values)

s2 = pd.Series(['a','b','c',1,2,3])
print(s2)


print()
date = ['2023-01-01','2023-06-15', '2023-08-25','2023-10-06']
s4 = pd.Series([200,180,np.nan,210], index=date)
print(s4)

s5 = pd.Series({'2023':200, '2022':180, '2021':210})
print(s5)


print()
day = pd.date_range(start='2023-08-15', end='2023-08-25')
print(day)

day2 = pd.date_range(start='2023-08-25',periods=4)
print(day2)

day3 = pd.date_range(start='2023-08-25',periods=6, freq='30min') #'H','30T'...
print(day3)

day4 = pd.date_range(start='2023-08-21', periods=5)
s = pd.Series(["짜장면","짬뽕",np.nan,"탕수육","팔보채"], index=day4)
print(s)


# DateFrame------------------------------------------------------------------------
print()
data = {
    'Name':['짱구','철수','훈이'],
    'Age':[5,5,5]
}

df = pd.DataFrame(data)

print(df)
print('--------------------')
print(df['Name'])
print('--------------------')
print(df.loc[0]) # 이름
print('--------------------')
print(df.iloc[0]) # 위치

print()
a = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(a)

data_list = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = pd.DataFrame(data_list)
print(b)

# date = pd.date_range('2023-08-15')
# column = ['A','B','C']
# pd.set_eng_float_format(date, index = date, columns=column)

data1 = {'A': [1,2,3,4,5], 'B':[6,7,8,9,10], 'C':[11,12,13,14,15]}
data2 = {'B': [1,2,3,4,5], 'C':[6,5,7,4,2], 'A':[11,12,14,52,23]}
d1 = pd.DataFrame(data1)
d2 = pd.DataFrame(data2)
d2
print(d1)
print(d2)
print(d1+d2)

print()
KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
            '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
            '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
            '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
            '동해선 KTX': [np.nan,np.nan, np.nan, np.nan, 2395, 3786, 6667]}
col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX']
index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017']

df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list)
print(df_KTX)
print('----------------------------------------------------------------')
print(df_KTX.head(3))
print('----------------------------------------------------------------')
print(df_KTX[2:4])
print('----------------------------------------------------------------')
print(df_KTX.loc['2012']['경전선 KTX'])
print('----------------------------------------------------------------')
df = df_KTX.sort_values('호남선 KTX')
print(df)
print('----------------------------------------------------------------')
print(df.loc['2015'])

# 실습
print()
data = {
    'Name':['John','Anna','Peter','Linda'],
    'Age':[28,24,35,32],
    'City':['New York','Paris','Berlin','London']
}
df = pd.DataFrame(data)
print(data)

# 1. 도시기준으로 정렬
df = pd.DataFrame(data)
df = df.sort_values('City')
print(df)

print()
# 2. 평균 나이 구하기
print(df['Age'].mean())

print()
# 3. 이름이 Peter인 사람의 나이 출력
print(df[df['Name']=="Peter"]['Age'].values)

print()
# 4. 가장 나이가 많은 사람이 살고 있는 이름, 도시 출력 
print(df.loc[df['Age'].idxmax()])

print()
# 5. 모든 사람의 이름을 대문자로 변경하기
df['Name'] = df['Name'].str.upper()
print(df)

print()
# 6. 나이가 30 이상인 사람들만 선택하기
older_than_30 = df[df['Age']>=30]
print(older_than_30)

print()
# 7. 각 도시별로 몇명이 살고있는지 계산하기
city_count = df['City'].value_counts()
print(city_count)

print()
# 8. Gender라는 새로운 열을 추가해서 임의 성별 할당하기
df['Gender'] = np.random.choice(['Male','Female'], size = df.shape[0])
print(df)