import csv
import numpy as np
import matplotlib.pyplot as plt

# CSV 파일 읽기
def read_csv_file(file_path):
    data = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader) # 헤더 건너뛰기
        
        for row in reader:
            name, age, gender, _ = row
            data.append((int(age), gender))
              
    return data


print(read_csv_file('./seocho_people.csv'))


# 나이와 성별에 따른 산점도 그래프를 그리고
# 선별 평균 나이 구해보기

age = [0]
gender = [1]

plt.plot('age', 'r', 'gender', 'b')

#축 라벨 설정
plt.xlabel('나이')
plt.ylabel('여성','남성')

#제목설정
plt.title('서초구 주민 인구 - 나이와 성별')

#차트 출력
plt.show()