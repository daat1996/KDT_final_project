from itertools import permutations

def make_algorithm(numbers):
    str_numbers = list(map(str, numbers))
    arithmetics = ['+', '-', '*', '/']
    expression_dict = {}

    def calcul(used_numbers, expression, remaining_numbers):
        # 모든 숫자를 사용하거나 사용하지 않았을 때 결과 추가
        if len(used_numbers) == len(numbers) or len(remaining_numbers) == 0:
            result = round(eval(expression), 3)
            expression_dict[result] = expression
            return

        # 재귀 호출을 통해 가능한 모든 경우 탐색
        for i, num in enumerate(remaining_numbers):
            # 사용된 숫자, 계산식, 남은 숫자 업데이트
            new_used_numbers = used_numbers + [num]
            new_expression = expression + num
            new_remaining_numbers = remaining_numbers[:i] + remaining_numbers[i+1:]

            # 사칙연산 삽입
            for arithmetic in arithmetics:
                calcul(new_used_numbers, new_expression + arithmetic, new_remaining_numbers)

    # 초기 호출
    calcul([], '', str_numbers)
    return expression_dict

numbers = [1, 2, 3, 4]
all_expressions = make_algorithm(numbers)
print(all_expressions)
