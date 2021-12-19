import sys
import math

def is_real(string):
    try:
        float(string)
        return True
    except (ValueError, TypeError):
        return False

def check(index, prompt, coef_str):
    while True:
            if not is_real(coef_str):
                print(f"{index} коэффициент введен неверно, невозможно "
                      f"преобразовать в вещественное число\n{prompt} ",end = '')
                coef_str = input()
            else:
                break
    return coef_str


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры
    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента
    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = check(index, prompt, sys.argv[index])
    except:
        # Вводим с клавиатуры
        print(prompt, end = ' ')
        coef_str = check(index, prompt, input())
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения
    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C
    Returns:
        list[float]: Список корней
    '''
    if a == 0 and b == 0 and c == 0:
        result = [1, 2, 3, 4, 5]
    elif a > 0 and b > 0 and c > 0 or a < 0 and b < 0 and c < 0:
        result = []
    elif a == 0 or b == 0:
        if c > 0:
            result = []
        elif c == 0:
            result = [0,]
        else:
            if a == 0:
                result = [-math.sqrt(-c/b), math.sqrt(-c/b)]
            else:
                result = [-math.sqrt(math.sqrt(-c/a)), math.sqrt(math.sqrt(-c/a))]
    elif c == 0:
        if a > 0 and b > 0:
            result = [0,]
        else:
            result = [-math.sqrt(abs(b/a)), 0, math.sqrt(abs(b/a))]
    else:
        D = b * b - 4 * a * c
        if D < 0:
            result = []
        elif D == 0:
            result = [-math.sqrt(-b / 2 / a), math.sqrt(-b / 2 / a)]
        else:
            D = math.sqrt(D)
            s1 = (-b + D) / 2 / a
            s2 = (-b - D) / 2 / a
            if s1 < 0 and s2 < 0:
                result = []
            elif (s1 > 0 and s2 < 0) or (s1 < 0 and s2 > 0):
                if s1 > 0:
                    result = [-math.sqrt(s1), math.sqrt(s1)]
                else:
                    result = [-math.sqrt(s2), math.sqrt(s2)]    
            else:
                result = [-math.sqrt(s1), -math.sqrt(s2), math.sqrt(s2), math.sqrt(s1)]
    return result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a, b, c)
    # Вывод корней
    len_roots = len(roots)
    if len_roots == 0:
        print("Нет корней")
    elif len_roots == 1:
        print(f"Один корень: {roots[0]}")
    elif len_roots == 2:
        print(f"Два корня: {roots[0]} и {roots[1]}")
    elif len_roots == 3:
        print(f"Три корня: {roots[0]}, {roots[1]} и {roots[2]}")
    elif len_roots == 4:
        print(f"Четыре корня: {roots[0]}, {roots[1]}, {roots[2]} и {roots[3]}")
    else:
        print("Бесконечное множество корней")
    

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()