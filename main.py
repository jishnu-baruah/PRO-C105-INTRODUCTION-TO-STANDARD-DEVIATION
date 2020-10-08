import math
import csv
import pandas as pd
import plotly.express as px


def calculateStdev(fileName,rowIndex)
    with open(fileName, newline='') as f:
        reader = csv.reader(f)
        file_data = list(reader)

    data1 = file_data[rowIndex]

    # def mean(data):
    n = len(data1)
    total = 0
    for i in data1:
        total += int(i)

    mean = total/n


    squaredList = []

    for n in data1:
        a = int(n) - mean
        a = a**2
        squaredList.append(a)

    listSum = 0

    for i in squaredList:
        listSum += i

    result = listSum/(len(data1)-1)

    sd = math.sqrt(result)

    print(sd)
    
   
fileName=input("file name : ")
rowIdex=input('find standard deviation of row : ')
calculateStdev(fileName,rowIndex)
