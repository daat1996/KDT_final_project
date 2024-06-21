import pandas as pd

#
# def find_expression(numbers, target):
#     def backtrack(expression, start, value):
#         if start == len(numbers):
#             if value == target:
#                 print("식을 찾았습니다:", expression)
#             return
#
#         for i in range(start, len(numbers)):
#             num = numbers[i]
#             backtrack(expression + "+" + str(num), i + 1, value + num)
#             backtrack(expression + "-" + str(num), i + 1, value - num)
#             backtrack(expression + "*" + str(num), i + 1, value * num)
#             if num != 0 and value % num == 0:  # 나눗셈에서 나머지가 없는 경우에만 진행
#                 backtrack(expression + "/" + str(num), i + 1, value // num)
#
#     backtrack("", 0, 0)
#
#     # 원하는 숫자를 만들 수 없다면
#     print("원하는 숫자를 만들 수 없습니다.")
#
# # 예제 사용
# numbers = [9, 10, 4, 2, 7, 5]
# target = 301
#
# find_expression(numbers, target)


def find_all_numbers(numbers):
    def backtrack(expression, start, value):
        if start == len(numbers):
            result=round(value, 6)
            results.add(result)
            algorythm[result]=expression
            return

        for i in range(start, len(numbers)):
            num = numbers[i]
            # 현재 숫자를 추가하여 재귀 호출
            backtrack(expression + "+" + str(num), i + 1, value + num)
            backtrack(expression + "-" + str(num), i + 1, value - num)
            backtrack(expression + "*" + str(num), i + 1, value * num)
            if num != 0:
                backtrack(expression + "/" + str(num), i + 1, value / num)

            # 현재 숫자를 추가하고 다음 숫자부터 시작하여 재귀 호출
            backtrack(expression + "*" + "(" + str(num), i + 1, value * num)
            if num != 0:
                backtrack(expression + "/" + "(" + str(num), i + 1, value / num)

    results = set()
    algorythm = {}
    for i in range(len(numbers)):
        backtrack(str(numbers[i]), i + 1, numbers[i])

    return results, algorythm


# 예제 사용
numbers = [9, 10, 4, 2, 3]

all_numbers, algorythm = find_all_numbers(numbers)
print("사칙연산과 괄호를 사용하여 만들 수 있는 모든 수:", sorted(all_numbers))
print(len(all_numbers))
print(algorythm)


