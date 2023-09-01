import numpy as np
import pandas as pd 

# 1000명의 사람 데이터 만들기
# 이름 : Person_1, Person_2, ... Person_1000
# 나이 : 20 ~ 60 랜덤
# 도시 : 특정 도시에서 랜덤으로 할당 ex) New York, Paris, Berlin, London, Seoul, Tokyo

np.random.seed(0)
data = pd.DataFrame({
    'Name':['Person_' + str(i) for i in range(1, 1001)],
    'Age': np.random.randint(20,60,1000), #20부터 60까지 1000개 
    'City': np.random.choice(["New York", "Paris", "Berlin", "London", "Seoul", "Tokyo"], 1000)
})
df = pd.DataFrame(data)
df = df.sort_values('City', ascending=False)
print(data)
# groupby : 데이터 특징 조건에 따라 그룹으로 분류하는 함수


# 도시별 평균 나이 구하기
group = data.groupby('City')['Age'].mean()
print(group)


print()
# 가장 많은 사람이 살고 있는 도시
city_count = data['City'].value_counts().idxmax() # value_counts() 먼저 세준 다음, idxmax
print("가장 많은 사람이 살고 있는 도시:",city_count)


# 연봉 추가해서 랜덤으로 할당 ex) $50,000 ~ $150,000
np.random.seed(0)
df['Annual'] = np.random.randint(50000,150000,size=1000)
print(data)


# 연봉 1등과 꼴등 출력해보기
annual_max = df['Annual'].idxmax()
annual_min = df['Annual'].idxmin()

print("연봉 1등:", df.loc[annual_max])
print("연봉 꼴등:", df.loc[annual_min])

print("-----------------------------------------")
print("연봉 1등:",df.loc[df['Annual'].idxmax()])
print("연봉 꼴등:",df.loc[df['Annual'].idxmin()])

print("-----------------------------------------")
df = df.sort_values('Annual')
print(df.iloc[0])
print(df.iloc[len(df)-1])

print("-----------------------------------------")
print(df.head(1))
print(df.tail(1))


