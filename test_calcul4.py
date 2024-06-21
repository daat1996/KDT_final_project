from itertools import permutations

def find_pairs(numbers):
    pairs = list(permutations(numbers,2))
    return pairs



def make_algorythm(numbers):
    strnumbers = list(map(str,numbers))
    arithmetics = ['+', '-', '*', '/']
    expression_dict = {}

    def calcul(strnumbers):
        all_pairs = find_pairs(strnumbers)
        for pair in all_pairs:
            remain_numbers = [num for num in strnumbers if num not in pair]

            # 사칙연산 삽입
            for arithmetic in arithmetics:
                express = '(' + pair[0] + arithmetic + pair[1] + ')'
                key = round(eval(express), 3)
                # 계산 값이 없는 경우 key로서 계산 딕셔너리에 입력
                if not key in expression_dict:
                    expression_dict[key] = express

                # 남은 숫자리스트에 계산식 넣기
                remain_numbers = [express] + remain_numbers

                # 남은 숫자 리스트 길이가 2이상이라면 이 과정을 반복
                if len(remain_numbers) >= 2:
                    calcul(remain_numbers)
                # 남은 리스트 수가 1개 라면
                else:
                    remain_numbers=[]
    calcul(strnumbers)
    return expression_dict

numbers = [1,2,3,4]

all_express = make_algorythm(numbers)

print(all_express)