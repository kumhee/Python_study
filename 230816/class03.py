x = int(input("찾고자 하는 값을 입력해주세요: "))

a = [1, 1, 2, 2 ,2, 3, 3]
print(a.count(x))

# for i in range(len(a)): #for(int i=0; i<a.length; i++)
#     print(a[i])
# #len(a) = a의 길이 = 7
# #range(7) = 0,1,2,3,4,5,6
# #range(2,7) = 2,3,4,5,6
# #range(2,7,2) = 2,4,6 #i+=2

# 01. count 함수 원리 구현해보기  
y = 0
for i in range(len(a)):
    if(x == a[i]):
        y += 1
print(y)
        
print("---------------------------------------------")

a = [1, 2, 3]
a.reverse()
print(a) #[3, 2, 1]


# 02-1. reverse 함수 원리 구현해보기
a = [1, 2, 3]
lst = []
for i in range(len(a)-1,-1,-1): #for(int i=1 , length-1 ; i>-1 ; i--)
    lst.append(a[i])
print(lst)

#02-2. while문
start, end = 0, len(a)-1 #처음값과 마지막값을 넣어줌
temp = 0 #옮길변수
while end > start:
    temp = a[start]
    a[start] = a[end]
    a[end] = temp #a[start], a[end] = a[end], a[start]
    start += 1
    end -= 1
print(a)

#02-3.
for i in range(len(a)//2):
    temp = a[i]
    a[i] = a[len(a)-i-1]
    a[len(a)-i-1] = temp
print(a)
    
print("---------------------------------------------")


# 03. list 함수 원리 구현 (숫자로)
# s = 123456 
# lst = list(s)
# print(lst)

# 04. 5x2 2차원리스트 만들어서 1-10까지 채우기
lst = [[0,0],[0,0],[0,0],[0,0],[0,0]]
a = 1
for i in range(len(lst)):
    for j in range(len(lst[i])):
        lst[i][j] = a
        a += 1

for i in range(len(lst)):
    for j in range(len(lst[i])):
        print(lst[i][j])




    
