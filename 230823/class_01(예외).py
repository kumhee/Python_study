class MyError(Exception):
    def __init__(self):
        super().__init__("나의오류")
        
try:
    raise MyError
except Exception as e:
    print("예외발생", e)
    

    
# 실습 (구구단)  
class NotNumberException(Exception):
    def __init__(self):
        super().__init__("NotNumber: 잘못된 숫자입니다.")
        
 def gugudan(n):
    if not(2 <= n <= 9):     
         try:
             raise NotNumberException
         except Exception as e:
             print(e)
    else :
        for i in range(1, 10):
            print(" {} X  {} =",format(n,i,n*i))   
            
            
# 패키지에서 디렉토리 내에 __init__.py      
     
               
        
   