print("01.사각형별--------------------")
# 01.
a = "*"
for i in range(5):
    for j in range(5):
        print(a, end = " ")  
        
    print()
    
print() 
    
    
# 02.  
lst = ["*"*5 for _ in range(5)]   # ['*****', '*****', '*****', '*****', '*****']
for i in lst:
    print(i)
# print(lst)
    
    

print("02.계단식별--------------------")
#01.
a = "*"
for i in range(5):
    for j in range(i+1):
        print(a, end = " ")  
        
    print()

print() 
   
    
# 02. 
for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()


print()     
# 03-list.    
lst = []  
for i in range(5):
    temp = ""
    for j in range(i+1):
        temp += "*"
    lst.append(temp)
for i in lst:
    print(i)
print(lst) #['*', '**', '***', '****', '*****']


print() 
# 04. 
lst = ["*"*(i+1) for i in range(5)] 
for i in lst:
    print(i)



print("03.대각선별--------------------")
# 01. 
for i in range(5):
    for j in range(5):
        if i == j:
            print("*")
            break
        else :
            print(end=" ") #공백출력
       

print()     
# 02-list.    
lst = []  
for i in range(5):
    temp = ""
    for j in range(5):
        if i == j: # i랑 j가 같을때, (0,0)(1,1)(2,2)(3,3)(4,4)이렇게 같을때, "*"을 넣는다.
            temp += "*"
            break
        else:
            temp += " "
    lst.append(temp)
for i in lst:
    print(i)
print(lst) # ['*', ' *', '  *', '   *', '    *'] 공백으로 바뀜

      
print()       
# 03. 
lst = [" "*i + "*" for i in range(5) ] #  " " + "*" 항상 공백이 있고, 뒤에 "*"이 붙어야 한다. 
#공백개수에 0,1,2,3,4(i)를 곱한다. 
for i in lst:
    print(i)       
        
        
        
print("04.계단식(역순)--------------------")
#01.
a = "*"
for i in range(5):
    for j in range(5):
        if i + j < 5:
            print(a, end = " ")  
        
    print()

print() 
#02.
for i in range(5):
    for j in range(4, -1, -1):
        if i <= j: # i가 0일때, j가 0,1,2,3,4 / i가 1일때, j가 1,2,3,4 / i가 2때, j가 2,3,4 / ...
            print("*", end="")
    print()
     
    

print()     
# 03-list.    
lst = []  
for i in range(5):
    temp = ""
    for j in range(5):
        if i <= j: #i=0, j=0,1,2,3,4 / i=1, j=1,2,3,4 / i=2, j=2,3,4 / ...
            temp += "*"
    lst.append(temp)
for i in lst:
    print(i)
print(lst) #['*****', '****', '***', '**', '*'] 5,4,3,2,1
    
    
print()       
# 04. 
# lst = [["*" for i in range(5-j)] for j in range(5)] 
lst = ["*"*(5-i) for i in range(5)] 
for i in lst:
    print(i)
print(lst)
    


print("05.계단식(역순)--------------------")
#01.
for i in range(5):
    for j in range(5):
        if i <= j: # i가 0일때, j가 0,1,2,3,4, i가 1일때, j가 1,2,3,4,
            print("*", end="")
        else:
            print(end=" ")
    print()
print() 


print()     
# 02-list.    
lst = []  
for i in range(5):
    temp = ""
    for j in range(5):
        if i <= j: 
            temp += "*"
        else:
            temp += " "
    lst.append(temp)
for i in lst:
    print(i)
# print(lst) 
    
    
print()       
# 03. 
lst = [" "*i + "*"*(5-i) for i in range(5)] # " "*i 대각선 만들어주고, "*"*(5-i) 4번처럼 5,4,3,2,1 채우기
for i in lst:
    print(i)
print(lst)





print()
#1번을 뒤집어서 2번으로 (reversed)
# 01.
lst = ["*"*(i+1) for i in range(5)] 
for i in lst:
    print(i)

# 02  
lst = ["*"*(i+1) for i in range(5)] 
for i in reversed(lst):
    print(i)
print(lst)