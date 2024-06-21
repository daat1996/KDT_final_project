# 상급 ai 생성 완료


def find_all_numbers(numbers):
    def backtrack(expression, start, value):
        if start == len(numbers):
            results.add(value)
            algorithms[value] = expression[1:-1]
            return

        for i in range(start, len(numbers)):
            num = numbers[i]
            # 현재 숫자를 추가하여 재귀 호출
            backtrack("(" + expression + "+" + str(num) + ")", i + 1, value + num)
            backtrack("(" + expression + "-" + str(num) + ")", i + 1, value - num)
            backtrack(expression + "*" + str(num), i + 1, value * num)
            if num != 0:
                backtrack(expression + "/" + str(num), i + 1, value / num)

            # 현재 숫자를 추가하고 다음 숫자부터 시작하여 재귀 호출
            backtrack("(" + expression + "*" + str(num) + ")", i + 1, value * num)
            if num != 0:
                backtrack("(" + expression + "/" + str(num) + ")", i + 1, value / num)

    results = set()
    algorithms = {}
    for i in range(len(numbers)):
        backtrack(str(numbers[i]), i + 1, numbers[i])

    return results, algorithms

def print_all_numbers(numbers, target):
    all_numbers, algorithms = find_all_numbers(numbers)
    print("사용 가능한 숫자:", numbers)
    print("목표 값:", target)
    print("사칙연산을 사용하여 만들 수 있는 모든 수:")
    for number in sorted(all_numbers):
        print(number, ":", algorithms[number])
    return all_numbers, algorithms

# 예제 사용
# numbers = [9, 10, 4, 2,7,1,4]
# target = 301
# #
# # print_all_numbers(numbers, target)
# # _,b = find_all_numbers(numbers)
# # print(b)
#
# numbers = [4,9,10,2]
# # print_all_numbers(numbers, target)
#
# _,b = find_all_numbers(numbers)
# print(len(b))