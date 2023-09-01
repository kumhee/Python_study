#
#range(1.처음, 2.끝, 3.중간)
# 1. 어디부터 시작할래?
# 2. 어디까지 할래?
# 3. 어떻게 진행할래?
# 1,3 생략 가능.


#구구단 출력
# x = int(input("몇단을 출력하시겠습니까?: "))

# for i in range(1, 10):
#     print("" , x , " X " , i , " = " , x*i)
    
    
# #구구단 전체 출력  
# for i in range(2, 10):
#     print("-----------------", i , "단------------2")
#     for j in range(1, 10):
#         # print(str(i) + " X " + str(j) + " = " + str(i*j))
#         print("%d X %d = %d" %(i,j,i*j))
#     print()

    
#사용자로부토 숫자를 계속 입력받다가 0을 입력하면 합계를 출력해주세요
x = 1
sum = 0
# while(x != 0):
while(True):
    x = int(input("값을 입력해주세요: "))
    sum += x
    if x==0:
        break

print("합계: ", sum)


#구구단 홀수단, 짝수단 입력
x = int(input("입력: "))

if x == 1: #홀수
    for i in range(3, 10, 2):
        print("------------", i , "단------------")
        for j in range(1, 10):
            print("%d X %d = %d" %(i,j,i*j))
    print()
            
elif x == 2: #짝수
    for i in range(2, 10, 2):
        print("------------", i , "단------------")
        for j in range(1, 10):
            print("%d X %d = %d" %(i,j,i*j))        
    print()
    
  
#간단한 방법(홀수 짝수 구구단 출력)  
# 01
# x = int(input("홀수 단(1) 또는 짝수 단(2)을 선택하세요: "))   
for i in range(2, 10):
    if(i%2 != x):
        continue
    print("------------", i , "단------------")
    for j in range(1, 10):
        print("%d X %d = %d" %(i,j,i*j))        
print()

# 02
if x == 1: 
    x = 3
    for i in range(x, 10, 2): #1입력: 3단부터, 2입력했을때 2단부터
        print("------------", i , "단------------")
        for j in range(1, 10):
            print("%d X %d = %d" %(i,j,i*j))
    print()

# 03
for i in range(2, 10):
    if(i%2 == 1 and x == 1) or (q%2 == 0 and x == 2):
        print("------------", i , "단------------")
        for j in range(1, 10):
            print("%d X %d = %d" %(i,j,i*j))        
print()






    

    





