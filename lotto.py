# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 20:15:41 2021

@author: jayson
"""

from random import seed
from random import randint
import plotly.express as px
import numpy as np
import statistics
import math
def lottoSample():
    sample = []
    nums = []
    for i in range(1,7):
        if len(nums) == 5:
            nums.append(randint(1, 26))
        else:
            nums.append(randint(1,70))
    sample.append(nums)
    return nums
            



def main():
    population = []
    numsNoPowerBall = []
    for i in range(200000):
        population.append(lottoSample())
        
    for i in population:
        for j in range(len(i)):
            if j != 5:
                numsNoPowerBall.append(i[j])
    fig = px.histogram(numsNoPowerBall,x = numsNoPowerBall)
    fig.show()
    su = 0
    total = 0
    sums = []
    for i in population:
        sums.append(sum(i))
    
    fig = px.histogram(sums , x = sums)
    fig.show()
    sumAverage = sum(sums)/len(sums)
    SD= statistics.stdev(sums)
    print(sumAverage)
    print(SD)
    print("99.9% confidence interval for lotto nums sums without powerball")
    upperSum = sumAverage + 3.291 * (SD/math.sqrt(200000))
    lowerSum = sumAverage - 3.291 * (SD/math.sqrt(200000))
    print("Upper: ", upperSum)
    print("Lower: ", lowerSum)
if __name__ == "__main__":
    main()