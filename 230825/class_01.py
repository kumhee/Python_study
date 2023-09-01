 # read() : 파일을 전체 내용을 문자열로 반환.
 # readline() : 파일에서 한 줄씩 문자열로 읽어옵니다. 
 # readlines() :파일의 전체 내용을 한 줄씩 읽어와서 각각 리스트로 만들어서 반환.
 
with open('alice.txt', 'r') as f:
    line = f.readline()
    
    while line:
        print(line.strip())# print(line, end="")
        line = f.readline()
        
with open('alice.txt', 'r') as f:
    line = f.readlines()
    for i in line:
        # print(i)
        print(i.strip()) # strip추가해서 줄바꿈 띄어쓰기 없애줌
    print(len(line))
    
    
    
# 모드
# "r" : 읽기 모드
# "w" : 쓰기  모드 (이전에 데이터를 모두 삭제하고 새로 적는다.)
# "w" : 생성모드 (파일을 생성해주는 모드, 이미 파일이 있으면 error가 나옴.)
# "a" : 추가 모드 (파일에 데이터를 추가하기 위해 사용된다. 해당 파일이 이미 존재한다면, 기존의 데이터 위에 새로운 데이터를 추가한다.)
# "b" : 바이너리 모드 (바이너리 데이터를 다룰 때 바이너리 데이터를 사용하기 위해)
# "t" : 텍스트 모드 (텍스트 데이터를 다루기 위해 사용됨. - 기본값)
# "r+" : 파일 읽기 쓰기를 모두 사용할 수 있는 모드.

# "rb" : 읽기 모드
# "wb" : 쓰기 모드

# "ab" : 추가 모드
# "wb" : 생성 모드 (바이너리 파일을 생성하기 위해 쓰임)
# "r+b", "wb+", "ab+" : 읽기 쓰기 모드 