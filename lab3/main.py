import json
from lab_python_fp.gen_random import gen_random
from lab_python_fp.unique import Unique
from lab_python_fp.print_result import print_result
from lab_python_fp.cm_timer import cm_timer_1

with open('data.txt', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(list(Unique([job[name] for job in arg for name in job if name == 'job-name'])))

@print_result
def f2(arg):
    return list(filter(lambda x: x.lower().startswith('программист'), arg))

@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))

@print_result
def f4(arg):
    return [s1 + ', зарплата ' + str(s2) for s1, s2 in zip(arg, gen_random(len(arg), 100000, 200000))]

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))

