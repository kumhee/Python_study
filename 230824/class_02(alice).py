# alice.txt에서 1. 단어가 총 몇개있는지 - 2145
# 숙제 2. 어떤 단어가 있는지, 각 단어가 몇 개씩 있는지

with open('alice.txt', 'r') as f:
    contents = f.read()
    
# 구두점 제거
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*~_'''
for punctuation in punctuations:
    contents = contents.replace(punctuation,"")
    
contents = contents.replace("\n", " ")

print(len(contents.split()))
print(contents.split(' '))


#각 단어 개수 계산
words = contents.lower().split()
# words = words.lower()

words_count = {} #딕셔너리 생성
for word in words:
    if word in words_count:
        words_count[word] += 1 # value값을 증가시킬지
    else :
        words_count[word] = 1 # 딕셔너리 새로 추가할지
        
# 단어 개수 출력
for word, count in words_count.items():
    print(f"{word}:{count}")

         



# 특정단어 개수 추출
count = 0
while len(contents) >= 5:
    temp = ""
    for i in range(5):
        temp += contents[i]
        
    if temp == "Alice":
        count += 1
        contents = contents[5:]
       
    contents = contents[1:]

print(count)

