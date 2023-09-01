import pickle

def menu():
    print("1.입력  |  2.조회  |  3.삭제  |  0.종료")
    choice = int(input("어느 것을 하시겠습니까?"))
    
    if choice == 1:
        name = input("이름:")
        math = input("수학:")
        science = input("과학:")
        english = input("영어:")
        write_choice(name, math, science, english)

    elif choice == 2:
        load_choice()
        
    elif choice == 3:
        load_choice()
        delete = int(input("삭제할 번호를 입력해주세요 : "))
        delete_choice(delete)

    elif choice == 0:
        print("종료되었습니다.")
        return -1
    return 0
        
        
        
def write_choice(name, math, science, english):
    dic = {"이름":name, "수학":math, "과학": science, "영어": english}
    lst = []
    with open('date.p', 'rb') as f:
        lst.append(pickle.load())
    
    lst.append(dic)    
    with open('date.p', 'rb') as f:
        pickle.dump(dic, f)     
         
         
def load_choice():
    with open('date.p', 'wb') as f:
        data = pickle.load()
    
    for i in range(len(data)):
        print(f'[{i}] 이름: {data[i]["이름"]}, 수학: {data[i]["수학"]}, 과학: {data[i]["과학"]}, 영어 : {data[i]["영어"]}')
    
    
def delete_choice(delete):
    with open('date.p', 'rb') as f:
        lst = pickle.load()
        
    if delete < 0 or delete >= len(lst):
        print('잘못된 입력입니다. 삭제할 수 없습니다.')
        return
  
    lst.pop(delete)
    
    with open('date.p', 'wb') as f:
        pickle.dump(lst, f)
    
    print("삭제가 완료되었습니다.")
  
while True:
    if menu() == -1:
        break