name = input('이름: ')
age = input('나이: ')
num = input('전화번호: ')
# dic = {"name": name, "age": age, "num": num}
# # print(dic)

# dic = dict(name = name, age = age, num = num)
# # print(dic)

lst = []
while True:
    name = input('이름: ')
    age = input('나이: ')
    num = input('전화번호: ') 
    
    if age == 0:
        break
    
    dic = {"name": name, "age": age, "num": num}
    lst.append(dic)
    print(lst)
    
print(lst)
