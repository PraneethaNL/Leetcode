from sys import *
from collections import *
from math import *
import heapq

def largestElement(arr: [], n: int) -> int:

    # Write your code from here.

    # max=float("-inf")
    # for i in arr:
    #     if max<i:
    #         max=i
    # return max

    #OR
    heapq._heapify_max(arr)

    return arr[0]
