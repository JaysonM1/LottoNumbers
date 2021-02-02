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
import pandas as pd
def lottoSample():
    sample = []
    nums = []
    for i in range(1,7):
        l = 0
        if len(nums) == 5:
            nums.append(randint(1, 26))
        else:
            nums.append(randint(1, 70))
    sample.append(nums)
    return nums
            
def numbersPlot(nums):
    fig = px.histogram(nums,x = nums)
    fig.show()


def sumOfLottoPlot(pop):
    sums = sumOfLotto(pop)
    
    fig = px.histogram(sums , x = sums)
    fig.show()


def sumOfLotto(pop):
    sums = []
    for i in pop:
        sums.append(sum(i))
    return sums


def differenceEachTicket(nums):
    total = 0
    pairs = (len(nums) + (len(nums) - 1))/2
    for i in nums:
        for j in nums:
            if i == j:
                continue
            total = abs(i - j) + total
    return total/pairs


def plotSums(pop):
    fig = px.histogram(sumOfLotto(pop) , x = sumOfLotto(pop))
    fig.show()
def sumsAverage(sums):
    return sum(sums)/len(sums)
def main():
    population = []
    numsNoPowerBall = []
    for i in range(5000):
        population.append(lottoSample())
        
    for i in population:
        for j in range(len(i)):
            if j != 5:
                numsNoPowerBall.append(i[j])
    numbersPlot(numsNoPowerBall)
    
    sumOfLotto(population)
    plotSums(population)
    
    
    ##dfdfdfdfd
    
    sumAverage = sumsAverage(sumOfLotto(population))
    SD= statistics.stdev(sumOfLotto(population))
    print(sumAverage)
    print(SD)
    print("99.9% confidence interval for lotto nums sums without powerball")
    upperSum = sumAverage + 3.291 * (SD/math.sqrt(5000))
    lowerSum = sumAverage - 3.291 * (SD/math.sqrt(5000))
    print("Upper: ", upperSum)
    print("Lower: ", lowerSum)
    
    total = 0
    
    for i in population:
        total = total + differenceEachTicket(i)
    diff = total / 5000
    print("average difference between the numbers in the tickets: ", diff)
if __name__ == "__main__":
    main()