# module_c.py

from module_b import sum_of_three
from module_a import add

def final_calculation(a, b, c):
    result = sum_of_three(a, b, c)
    return add(result, 10)
