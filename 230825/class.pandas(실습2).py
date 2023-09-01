import numpy as np
import pandas as pd 

# 1000명의 사람 데이터 만들기

# 1번 데이터셋
# 이름 : ID_1, ID_2, ... ID_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo

# 2번 데이터셋
# 이름 : ID_1, ID_2, ... ID_1000
# 연봉 : 랜덤

# 3번 데이터셋
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo
# 나라 : 특정 도시의 나라 ex) USA, France, Germany, Korea, Japan

# 1. 1번 데이터셋과 2번 데이터셋 병합(ID기준)
# 2. 병합된 데이터에 City를 기준으로 병합
# 3. 각 나라별 평균 연봉
# 4. 제일 연봉이 높은사람이 어느나라 사람인지?

np.random.seed(0)
data1 = pd.DataFrame({
    'Id':['ID_' + str(i) for i in range(1, 1001)],
    'Age': np.random.randint(20,60,1000), #20부터 60까지 1000개 
    'City': np.random.choice(["New York", "Paris", "Berlin", "London", "Seoul", "Tokyo"], 1000)
})
df = pd.DataFrame(data1)
df = df.sort_values('City', ascending=False)



data2 = pd.DataFrame({
    'Id':['ID_' + str(i) for i in range(1, 1001)],
    'Annual': np.random.randint(50000,150000, size=1000)
})
df = pd.DataFrame(data2)



data3 = pd.DataFrame({
    'City': ["New York", "Paris", "Berlin", "London", "Seoul", "Tokyo"],
    'Country': ["USA", "France", "Germany", "England", "Korea", "Japan"]
})
df = pd.DataFrame(data3)


print("-----------------------------------------")
print("1. 1번 데이터셋과 2번 데이터셋 병합 (ID기준)")
res = pd.merge(data1, data2, on='Id', how='outer')
print(res)


print("-----------------------------------------")
print("2. 병합된 데이터에 City를 기준으로 병합")
merged_data = pd.merge(res, data3, on='City')
print(merged_data.head(5))
print(merged_data.tail(5))

# df2 = pd.DataFrame(res, index=['City'])

# res = data1.join(data2)
# print(res)


print("-----------------------------------------")
print("3. 각 나라별 평균 연봉")
grouped_annual = merged_data.groupby('Country')['Annual'].mean()
print(grouped_annual)


print("-----------------------------------------")
print("4. 제일 연봉이 높은사람이 어느 나라 사람인지?")
highest_annual_country = merged_data.loc[merged_data['Annual'].idxmax()]['Country']
print("제일 연봉이 높은사람이 어느 나라:" , highest_annual_country)


