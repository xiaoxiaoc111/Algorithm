# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:59:24 2018

@author: Administrator

函数功能： 使用二分法-迭代和循环寻找value在lst的位置，循环相比迭代效率高
定义四个参数，lst value low high  有序列表 值 最低值 最高值

"""

def binary_search_recursion(lst, value, low, high):
    if high < low:
        return None
    mid =int((low + high) / 2)
    if lst[mid] > value:
        return binary_search_recursion(lst, value, low, mid-1)
    elif lst[mid] < value:
        return binary_search_recursion(lst, value, mid+1, high)
    else:
        return mid

def binary_search_loop(lst,value):
    low, high = 0, len(lst)-1
    while low <= high:
        mid= int((low+high)/2)
        if lst[mid] < value:
            low = mid + 1
        elif lst[mid] > value:
            high = mid - 1
        else:
            return mid
    return None


if __name__ == "__main__":
    import random
    lst = [random.randint(0, 100) for i in range(100)]
    lst.sort()

    def test_recursion():
        binary_search_recursion(lst, 99, 0, len(lst)-1)

    def test_loop():
        binary_search_loop(lst, 99)

    import timeit
    t1 = timeit.Timer("test_recursion()", setup="from __main__ import test_recursion")
    t2 = timeit.Timer("test_loop()", setup="from __main__ import test_loop")

    print ("Recursion:", t1.timeit())
    print ("Loop:", t2.timeit())