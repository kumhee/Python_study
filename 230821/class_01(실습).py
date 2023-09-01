# 01.
number = [12,32,55,12,32,4,86,50]

print(list(map(lambda x: "합격" if x>60 else "대기" if x>50 else "불합격", number)))




# 02.
print("jpg")
files = ["member.text", "1.jpg", "32.png", "23.jpg", "223.jpg"]

# 02-1.
print(list(filter(lambda x: x.find(".jpg") != -1, files)))

# 02-2.
print(list(filter(lambda x: '.jpg' in x, files)))

# 02-3.
for i in files:
    if ".jpg" in i:
        print(i)
        
# in, .jpg 사용하지 않고
print(list(filter(lambda s: ".jpg" == x[len(x)-4:], files)))

lst = []
for i in files:
    for j in range(len(i)):
        if(i[j] == "."):
            if i[j+1:] == 'jpg':
                lst.append(i)
                break

print()
# 리스트 세 개의 곱
lst1 = [1,2,3,4,5]
lst2 = [1,3,5,7,9]
lst3 = [2,4,8]
lst = []

# 01-1
print(list(map(lambda x, y, z: x*y*z ,lst1 , lst2, lst3))) # [2, 24, 120]
# 01.2
print(list(map(lambda x: x[0] * x[1] * x[2], zip(lst1 , lst2, lst3))))




print()
# 1부터 10까지의 제곱 값 중 홀수만 출력하기
a = [1,2,3,4,5,6,7,8,9,10]
b = []

# x = filter(lambda x: x%2 == 1, a)
# print(list(x))

b = list(map(lambda x: x**2,a))
print(list(filter(lambda x: x%2 == 1, b))) #[1, 9, 25, 49, 81]


a = list(map(lambda x: x*x, range(1,11)))
print(a) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


print(list(filter(lambda x: x%2 == 1, a))) #[1, 9, 25, 49, 81]
print(list(filter(lambda x: x%2 == 1, map(lambda x: x*x, range(1,11))))) #[1, 9, 25, 49, 81]