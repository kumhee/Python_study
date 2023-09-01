# 함수 - 매개변수

# 1. 기본 인자값 (Default Argument Value) : 함수에 전달되는 기본 매개변수 기본값을 지정해주는 것.
def func1(pa1 = 1, pa2 = 3, pa3 = 3):
    return 0 #값을 전달하지 않았을 때, 기본적으로 사용되는 값.


# 2. 키워드 인자 (Keuword Argument) : 함수에 전달되는 인자를 키와 값의 형태로 전달하는 것.
#    순서 상관없이 키값에 일치하는 곳에 값이 전달된다. 
def greeting(name, message = "Hello"):
    print(f"{message},{name}")
    
greeting(message="안녕", name="홍길동") #안녕,홍길동
greeting(name="김철수") #Hello,김철수


# 3. 가변 인수 리스트 (Arbitrary Argumeny Lists) : 함수에 전달되는 매개변수 앞에 (*)을 붙여서 가변 인수로 지정해주는 것.
#    인자가 일렬로 나열되서 전달되는데, tuple형태로 전달이 된다. 
def sum(*args):
    res = 0
    for arg in args:
        res += arg
    return res

print(sum(1,2,3))
print(sum(1,2,3,4,5,6,7))


# 4. 위치 인자 리스트 (Positional Argument Lists) : 함수에 전달되는 매개변수 앞에 (**)를 붙여서 인자 리스트로 지정해주는 것.
#    만약, 함수를 호출했을 경우, 키와값 쌍의 형태로 값이 전달되면 딕셔너리 형태로 전달된다. 
def greeting2(**kwargs):
    for name, message in kwargs.items(): #key-value = name-message
        print(f"{message}, {name}")
greeting2(chris="hello", Bob="안녕")