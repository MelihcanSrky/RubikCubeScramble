import random
import csv 
import time
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


with open("3x3x3.csv",'w') as solvefile:
        writer = csv.writer(solvefile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Sub","Scramble","Time"])
        solvefile.close()

col_list = ["Sub","Scramble","Time"]

moves = ["U","D","F","B","R","L"]
dir = [" ", "'", "2"]
slen = random.randint(16, 21)

Secenek = True

i=0
while Secenek == True:
    i=i+1
    def scramble_gen():
        scramble = [0] * slen
        for x in range(len(scramble)):
            scramble[x]=[0]*2
        return scramble
    
    def scramble_replace(ar):
        for x in range(len(ar)):
            ar[x][0] = random.choice(moves)
            ar[x][1] = random.choice(dir)
        return ar
    
    def valid(ar):
        for x in range(1,len(ar)):
            while ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
        for x in range(2,len(ar)):
            while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
                ar[x][0] = random.choice(moves)
            return ar
    
    def timer(sure):
        start = input("Press Enter to start timer")
        begin = time.time()
        stop = input("Press Enter to stop timer")
        end = time.time()
        score = end - begin
        
        sure = (float(score))
        print("%.2f" % score)
        return sure
        
    def sprint(ar):
        for x in range(len(ar)):
            print(str(ar[x][0]) + str(ar[x][1]), end = " ")

    s = scramble_replace(scramble_gen())
    sprint(valid(s))
    
    sure = 0
    sure = timer(sure)
    
    
    with open("3x3x3.csv",'a') as solvefile:
        writer = csv.writer(solvefile,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Sub"+str(i),valid(s),float(sure)])
        
    
    
    Tekrarla = input("Tekrar çözmek için Y, Çıkmak için H basınız")
    if Tekrarla == "y":
        Secenek = True
    else:
        Secenek = False
        solvefile.close()

df = pd.read_csv("3x3x3.csv",usecols=(col_list))

f,ax1 = plt.subplots(figsize =(10,10))
sns.pointplot(x=df["Sub"],y=df["Time"])