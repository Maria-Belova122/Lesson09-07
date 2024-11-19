# ЗАДАНИЕ ПО ТЕМЕ "Декораторы"

def is_prime(func):
    def wrapper(*args):
        result_d = func(*args)
        if result_d > 1:
            res_pr = 'Простое'
            for i in range(2, result_d - 1):
                if result_d % i == 0:
                    res_pr = 'Составное'
                    break
        else:
            res_pr = 'Число вне категории'
        print(res_pr)
        return result_d

    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)
