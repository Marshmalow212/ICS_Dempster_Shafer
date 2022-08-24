import numpy as np

L = int(2) 
w = []
# L basic attributes
w.append(float(0.35)) #mass of accuracy
w.append(float(0.65)) #mass of reputation
# print(type(w[1]))
Warr = np.array(w)
print(Warr)

N = int(3)
H = ['poor','average','good'] #N distinctive evaluation grades

# The basic attribute accuracy, is assessed to be poor by an observer, with a degree of
# belief β1,1 of 40%, average β2,1 by 50 %, and good to the degree of belief β3,1 of 0 %.

DBA = []
DBA.append(float(0.4))
DBA.append(float(0.5))
DBA.append(float(0.0))
# DBA.append(float(0.1))


DBR = []
DBR.append(float(0.1))
DBR.append(float(0.75))
DBR.append(float(0.15))
# DBR.append(float(0.00))

DB = [DBA,DBR]
# print(DB)
DBarr = np.array(DB)
print("Degree of Belief Bf : ",DBarr)

#probability mass

PMA = np.multiply(Warr[0],DBarr[0])
PMR = np.multiply(Warr[1],DBarr[1])
PM = np.array([PMA,PMR])

print("Probability Mass M(L,N) : ",PM)
# for i in range (0,L):
#     for j in range (0,N):
#         M[i].append(round((w[i]*DB[i][j]),4))
# print(M)
print("============")
print(DBarr[0])
sumofDBA = np.sum(DBarr[0])
print(sumofDBA)
sumofDBR = np.sum(DBarr[1])
print(DBarr[1])
print(sumofDBR)
print(sumofDBA,sumofDBR)
print("==============")
delM = np.array([np.subtract([1],Warr[0]),np.subtract([1],Warr[1])])
print("delMh : " ,end="")
print(delM)
tilM = np.array([np.multiply(Warr[0],np.subtract([1],sumofDBA)),np.multiply(Warr[1],np.subtract([1],sumofDBR))])
print("tildaMh : ",end="")
print(tilM)

hM = np.array([np.add(delM[0],tilM[0]),np.add(delM[1],tilM[1])])
print("Mh : ",end="")
print(hM)

I = L-1
print("I",I)
n = N
cumSum = float(0)

m11 = np.array(np.multiply(PM[I][1:],PM[I-1][0]))
m11Sum = np.sum(m11)
# print(m11)
m21 = np.array(np.multiply(PM[I][::2],PM[I-1][1]))
# print(m21)
m21Sum = np.sum(m21)

m31 = np.array(np.multiply(PM[I][:1],PM[I-1][2]))
m31Sum = np.sum(m31)
# print(m31)
cumSum += m11Sum + m21Sum + m31Sum
print("Cumulative Sum : ",cumSum)
consK = round((1/(1-cumSum)),5) # Aggregation Constant K
print("Constant K : ",consK)

#Aggregation for probability mass m1,m2,m3
#for M1
m1 = (np.multiply(PM[I][0:1],PM[I-1][0:1]))
m1h = (np.multiply(hM[I-1][0:1],PM[I][0:1]))
mh1 = (np.multiply(hM[I][0:1],PM[I-1][0:1]))
print(m1,m1h,mh1)
m1sum = np.add(m1,m1h)
m1sum = np.add(mh1,m1sum)
print(m1sum)
m1sum = np.multiply([consK],m1sum)
print("M1 : ",m1sum)
#for M2
m2 = (np.multiply(PM[I][1:2],PM[I-1][1:2]))
m2h = (np.multiply(hM[I-1][0:1],PM[I][1:2]))
mh2 = (np.multiply(hM[I][0:1],PM[I-1][1:2]))
print(m2,m2h,mh2)
m2sum = np.add(m2,m2h)
m2sum = np.add(mh2,m2sum)
print(m2sum)
m2sum = np.multiply([consK],m2sum)
print("M2 : ",m2sum)
#for M3
m3 = (np.multiply(PM[I][2:],PM[I-1][2:]))
m3h = (np.multiply(hM[I-1][0:1],PM[I][2:]))
mh3 = (np.multiply(hM[I][0:1],PM[I-1][2:]))
print(m3,m3h,mh3)
m3sum = np.add(m3,m3h)
m3sum = np.add(mh3,m3sum)
print(m3sum)
m3sum = np.multiply([consK],m3sum)
print("M3 : ",m3sum)

#for tilda M

mtilda = (np.multiply(tilM[I][0:1],tilM[I-1][0:1]))
mtilda1 = (np.multiply(delM[I-1][0:1],tilM[I][0:1]))
mtilda2 = (np.multiply(delM[I][0:1],tilM[I-1][0:1]))
print(mtilda,mtilda1,mtilda2)
mtildasum = np.add(mtilda,mtilda1)
mtildasum = np.add(mtilda2,mtildasum)
print(mtildasum)
mtildasum = np.multiply([consK],mtildasum)
print("tilda M : ",mtildasum)

#for delta M

mdelta = np.multiply(delM[I-1][:],delM[I][:])
print(mdelta)
mdeltasum = np.multiply([consK],mdelta)
print("delta M : ",mdeltasum)

#for H M 
mHsum = np.add(mtildasum,mdeltasum)
print("HM : ",mHsum)

aggregatedDeltaM = mdeltasum[0]
denominator = 1 - aggregatedDeltaM
aggregatedTildaM = mtildasum[0]

#Combined degree of belief

B1 = round((m1sum[0] / denominator),4)
B2 = round((m2sum[0] / denominator),4)
B3 = round((m3sum[0] / denominator),4)
Bh = round((aggregatedTildaM / denominator),4)
print("========================================")
print("B1 : ",B1)
print("B2 : ",B2)
print("B3 : ",B3)
print("BH : ",Bh)







