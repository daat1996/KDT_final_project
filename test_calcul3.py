from itertools import permutations

def find_all_pairs(numbers):
    pairs = list(permutations(numbers, 2))
    return pairs

# 예제 사용
numbers = [1, 2, 3, 4, 5]
all_pairs = find_all_pairs(numbers)
print("리스트 안에서 가능한 모든 순서쌍:")
print(all_pairs)
print(permutations(numbers,2))

expression_dict = {}
arithmetics = ['+','-','*','/']


# 숫자 리스트에서 2개를 꺼냄
for pair in all_pairs:

    # 꺼내고 남은 숫자리스트 생성(2개일때를 제외할 if 처리 필요)
    remaining_numbers = [num for num in numbers if num not in pair]

    # 사칙연산을 두 숫자 사이에 삽입
    for arithmetic in arithmetics:
        express=f'{pair[0]}{arithmetic}{pair[1]}'
        key = round(eval(express),3)
        # 계산 값이 없는 경우 key로서 계산 딕셔너리에 입력
        if not key in expression_dict:
            expression_dict[key]=express

        # 남은 숫자리스트에 넣고 이 과정을 반복
        remaining_numbers.append(key)

print(expression_dict)
