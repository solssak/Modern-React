# 중앙값 구하기
def solution(a):
    a.sort() # 오름차순
    center_idx = len(a)//2 # 리스트 개수를 2로 나누어줌 (중간 값)
    return a[center_idx] # 중간 값을 리턴

    # 위 코드는 리스트가 홀수일 때만 적용되는 경우

# 문자열 안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2

#    if str2 in str1:
#       return 1
#    else: return 2
    

# 모음 제거
def solution(my_string):

  remove = ['a', "e", "i", "o", "u"]
  for i in remove:
    my_string = my_string.replace(i,'')
  return my_string
  
# 순서쌍의 개수 >> 다시 공부하기
def solution(n):
    answer = 0 
    for i in range(n):
        if n % (i+1) == 0:
            answer +=1
    return answer

# 피자 나눠먹기 >> 다시 공부하기
import math 

def solution(slice, n):
    return math.ceil(n/slice)

# 문자열 정렬하기 (1)
def solution(my_string):
    answer = []
    
    for i in my_string:
        if i.isdigit():
            answer.append(int(i))
            # answer += i >> 기존 내 것. 왜 안됐는지 생각해보기.
    answer.sort()
    return answer

# 인덱스 바꾸기
def solution(my_string, num1, num2):
    l_string = list(my_string)
    l_string[num1],l_string[num2] = l_string[num2],l_string[num1]
    return "".join(l_string)

    # 문자열을 즉시 수정할 수 없음 >> list()
    # 문자열 합치기 >> ''.join 

# 최댓값 만들기(1)
def solution(numbers):
    numbers = sorted(numbers)
    return max(numbers[0] * numbers[1], numbers[-2] * numbers[-1])
    
    # sorted(), sort() 차이
    # sorted 는 변수에 재할당 해줘야함. sort() 는 불필요

# 피자 나눠 먹기(2)
def solution(n):
    # pizza * 6 = total_slice
    # total_slice % n == 0
    
    # 피자는 1판부터 사직함
    pizza = 1
    # 피자를 6조각으로 나누었을 때 딱 딸어질 때까지 while 루프
    while (pizza * 6) % n:
        pizza += 1
    return pizza

# 다른 풀이 >> gcd 알아보기
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6

# 약수 구하기
def solution(n):
    answer = []
    for i in range(1, n+1):
        if n % i == 0: 
            answer.append(i)
# 내 실수 =>  answer = answer.append(i)
# AttributeError: 'NoneType' object has no attribute 'append'
    return answer

# 369 게임
def solution(order):
    answer = 0
    while order:
        if order % 10 in [3, 6, 9]:
            answer += 1
        order //= 10
        
    return answer

# 다른 풀이
def solution(order):
    order = str(order)
    
    return order.count('3') + order.count('6') + order.count('9')


# 문자열 정렬하기 (2) >> 온전한 내 힘으로 해결했다!!!!!!!
def solution(my_string):
    answer = ''
    
    for i in my_string.lower():
        answer += i
            
    return "".join(sorted(answer))
# "" 형태의 문자열에 정렬을 하고 싶으면 "".join() 메서드 이용!

# 다른 풀이 (리스트 컴프리헨션)
def solution(my_string):
    return ''.join(sorted(my_string.lower()))

def solution(num, k):
    answer = 0
    for i in num:
        if k in num:
            return 
        else:
            return -1
    return answer

# 합성수 찾기 >> 다시 공부하기
def solution(n):
    answer = 0
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer

# n의 배수 고르기 >> 리스트에 정수 넣을 때 append()
def solution(n, numlist):
  answer =[]
  for i in numlist:
    if i % n == 0:
      answer.append(i)
  return answer

def solution(numbers):
  return [i*2 for i in numbers]

# 중복된 문자 제거
def solution(my_string):
    answer = ''
    
    for i in my_string:
        if i not in answer:
            answer += i
            
    return answer

# 한 번만 등장한 문자
def solution(s):
    answer = ""
    # 사전 순으로 정렬한 문자열
    for alpha in "abcdefghijklmonqprstuvwxyz":
        # 한 번만 등장하는 문자
        if 1 == s.count(alpha):
            answer += alpha
    return answer

# 다른 풀이
def solution(s):
    return "".join(sorted([ alpha for alpha in s if s.count(alpha) == 1 ]))
# ==
def solution(s):
    answer = ""
    for alpha in s:
        if 1 == s.count(alpha):
            answer += alpha
    return "".join(sorted(answer))

# 숨어있는 숫자의 덧셈(2)
def solution(my_string):
    answer = 0
    num = ''
    
    for i in my_string:
        if i.isdecimal():
            num += i
        else:
            if len(num) == 0:
                continue
            answer += int(num)
            num = ''
            
    if len(num) != 0:
        answer += int(num)
    
    return answer

# 다른 풀이
def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())

# 진료 순서 정하기
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse = True)
    return [sorted_emergency.index(i)+1 for i in emergency]

# 주사위의 개수
def solution(box, n):
    return (box[0]//n) * (box[1]//n) * (box[2]//n)

# 세균 증식

def solution(n, t):
    return n << t
    # 비트 쉬프트 연산

# 암호 해독
def solution(cipher, code):
    answer = ''
    for i in range(code-1, len(cipher),code):
        answer += cipher[i] # 문자열인데 [i] 로 넣어주는 이유? >> for문이 배열로 return되기 때문?
    return answer