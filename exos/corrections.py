# -*- coding: utf-8 -*-
from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args

from math import sqrt

def isPrime(n):
    if n==2 or n==3:
        return True
    if n%2 == 0 or n<=1:
        return False
    d=3
    while n%d!=0 and d <= sqrt(n):
        d+=2
    return n%d!=0

inputs_isPrime = [
    Args(1), Args(2), Args(3), Args(5), Args(17), Args(1001)  
]

exo_isPrime = ExerciseFunction(
    isPrime,
    inputs_isPrime,
    layout='pprint',
    layout_args=(40, 25, 25),
)