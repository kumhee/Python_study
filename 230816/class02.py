#Hello world -> o를 제거하고 Hllo world 출력

s = "Hello World"
print(s.replace('o',""))

lst = list(s)
print(lst)

for i in lst:
    if(i == 'o'):
        continue
    print(i, end="")     #print(i, end="\n") -> 줄바꿈

print()    
print(lst[:4] + lst[5:7] + lst[8:]) #[0:4] [5:7][8:0] 끝값은 비워둠
#lst[:4] -> Hell
#lst[5:7] -> 공백, w
#lst[8:] -> rld (8부터 끝까지)


#다시 문자열로 바꾸기
s = ""

for i in lst[:4] + lst[5:7] + lst[8:]:
    s += i
    
print(s)


#반복문과 if문을 사용한 간단한 방법:
lst2 = []
start = 0
for i in range(len(lst)):
    if lst[i] == 'o' or i == len(lst)-1:
        lst2 += lst[start:i] #현재 i의 위치 
        start = i+1

print(lst2)
        
print("---------------------------------------------")    

#'o'del
lst = list('hellooooo woorld')     
i = 0
while(True) :
    if(i == (len(lst))):
        break

    if lst[i] == 'o':
        del lst[i]
    else :
        i += 1
        
# lst = list('ooooooooooooooooooooo')

# for j in range(len(lst)):
#     for i in range(len(lst)):
#         if lst[i] == 'o':
#             del lst[i]
#             break
        
print(lst)




