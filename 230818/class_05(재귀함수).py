# 재귀함수 (Recursion function)
# 1. 함수 내부에서 자기 자신함수를 호출해야 한다.
# 2. 재귀를 종료시켜주는 조건문이 존재해야 한다. (end)
def test(end):
    if end == 0: 
        return
    print('재귀함수!')
    test(end-1)
test(5) # 5부터 0번째가 됬을 때 종료됨. -> if end == 0: 


def test(end):
    if end == 0: 
        return
    print(end) # 5,4,3,2,1이 출력됨.
    test(end-1)
test(5)  

def test(end):
    if end == 0: 
        return 
    test(end-1) # 1,2,3,4,5가 출력됨.
    print(end)
    
test(5)  


print("팩토리얼 구하기-------------------------------")

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
factorial(5)
# factorial(5) = 5 * factorial(4) = 5*4*3*2*1

# factorial(4) = 4 * factorial(3) = 4*3*2*1

# factorial(3) = 3 * factorial(2) = 3*2*1

# factorial(2) = 2 * factorial(1) = 2*1

# factorial(1) = 1

print("홀수-------------------------------")

def f_sum(n):
    if n == 1: #if n <= 2:
        return 1
    return n + f_sum(n-1) # return f_sum(n-1) + 1
   
print(f_sum(5)) #15



print()
print("높은자리부터 출력-------------------------------")

def f_number(n):
    if n == 0: 
        return 0
    f_number(n//10)
    print(n%10)
   
f_number(1234)



print()
print("두 수 사이의 홀수출력-------------------------------")
# 두 수 사이의 홀수 구하기
# print_odd(1,10) - 1, 3, 5, 7, 9

def odd(start, end):
    if start == end: 
        return
    elif start%2 == 1:
        print(start)
    odd(start + 1, end)

odd(1, 10)



print()
print("피보나치 수열-------------------------------")
# 피보나치 수열 1 1 2 3 5 8 13 21 34 ...
# fibo(6) - 8

def fibo(n):
    if n == 1 or n == 2: 
        return 1
    return fibo(n-1) + fibo(n-2)
# fibo(3) = fibo(2) + fibo(1)
# fibo(4) = fibo(3) + fibo(2)
# fibo(5) = fibo(4) + fibo(3)
# .
# .
# fibo(n) = fibo(n-1) + fibo(n-2)

print(fibo(4))



print()
print("10진수 -> 2진수로 변환-------------------------------")
# 10진수 -> 2진수로 변환하기
# 10작성하면 1010나오게
# 2 - 10
# binary(10) - 1010
# 10 - 1010 = 1010

# 01.
def binary(n):
    if n < 1 :
        return
    binary(n//2)
    print(n%2, end="")
binary(10)
print()
binary(50)


# 02.
# def binary(n):
#     if n < 2 :
#         print(n%2, end="")
#         return
#     binary(n//2)
#     print(n%2, end="")
# binary(10)
# print()
# binary(50)



print()
print("-------------------------------")
example = [[1,2,3], [4, [5,6]], 7, [8,9]]



# lst = [[1,2,3]],[[4,5,6]]
# empty_lst = []

# for i in range(len(example)):
#     if type(example[i]) == list:
#         for j in range(len(example[i])):
#             if type(example[i][j]) == list:
#                 for k in range(len(example[i][j])):
#                     empty_lst.append(example[i][j][k])
#             else:
#                 empty_lst.append(example[i][j])
#     else:
#         empty_lst.append(example[i])
        
# print(empty_lst)



def flatten(date):
    flat_lst = []
    for i in date:  
        if type(i) == list:
            flat_lst.append(flatten(i))
        else: 
            flat_lst.append(i)
    flat_lst.append(i)
    return flat_lst
    

print(flatten(example)) # [1,2,3,4,5,6,7,8,9]



