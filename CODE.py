from recsys.algorithm.factorize import SVD
from recsys.datamodel.data import Data
import csv
import numpy as np
import matplotlib.pyplot as plt
print ("similarity in marvel comics")
data_file=open('test1.csv','rU')
reader=csv.DictReader(data_file)
likes={}
for row in reader:
    if row['username'] in likes:
        likes[row['username']].append(row['user_likes'])
    else:
        likes[row['username']] = [row['user_likes']]
data_file.close()
data = Data()
VALUE = 1.0
for username in likes:
    for user_likes in likes[username]:
        data.add_tuple((VALUE, username, user_likes)) # Tuple format is: <value, row, column>

svd = SVD()
svd.set_data(data)
k = 5 # Usually, in a real dataset, you should set a higher number, e.g. 100
svd.compute(k=k, min_values=3, pre_normalize=None, mean_center=False, post_normalize=True)
l1=svd.similar('toby')
keylist3=sorted(l1,key=lambda x: x[0])
print(l1)
labels, ys = zip(*keylist3)
xs = np.arange(len(labels)) 
width = 1
plt.bar(xs, ys, width, align='center')
plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)

plt.savefig('netscore.png')
plt.cla()   # Clear axis
plt.clf()   # Clear figure
#close()
print ("similarity in music")
data_file=open('test2.csv','rU')
reader=csv.DictReader(data_file)
likes={}
for row in reader:
    if row['username'] in likes:
        likes[row['username']].append(row['user_likes'])
    else:
        likes[row['username']] = [row['user_likes']]
data_file.close()
data = Data()
VALUE = 1.0
for username in likes:
    for user_likes in likes[username]:
        data.add_tuple((VALUE, username, user_likes)) # Tuple format is: <value, row, column>

svd = SVD()
svd.set_data(data)
k = 5 # Usually, in a real dataset, you should set a higher number, e.g. 100
svd.compute(k=k, min_values=3, pre_normalize=None, mean_center=False, post_normalize=True)
l2=svd.similar('toby')
keylist2=sorted(l2,key=lambda x: x[0])
print(l2)
labels, ys = zip(*keylist2)
xs = np.arange(len(labels)) 
width = 1

plt.bar(xs, ys, width, align='center')

plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)
plt.savefig('netscore2.png')
plt.cla()   # Clear axis
plt.clf()   # Clear figure
#close()
print ("similarity in Dc comics")
data_file=open('test3.csv','rU')
reader=csv.DictReader(data_file)
likes={}
for row in reader:
    if row['username'] in likes:
        likes[row['username']].append(row['user_likes'])
    else:
        likes[row['username']] = [row['user_likes']]
data_file.close()
data = Data()
VALUE = 1.0
for username in likes:
    for user_likes in likes[username]:
        data.add_tuple((VALUE, username, user_likes)) # Tuple format is: <value, row, column>

svd = SVD()
svd.set_data(data)
k = 5 # Usually, in a real dataset, you should set a higher number, e.g. 100
svd.compute(k=k, min_values=3, pre_normalize=None, mean_center=False, post_normalize=True)
l3=svd.similar('toby')
keylist = sorted(l3,key=lambda x: x[0])
labels, ys = zip(*keylist)
xs = np.arange(len(labels)) 
width = 1

plt.bar(xs, ys, width, align='center')

plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)
plt.savefig('netscore3.png')
print(l3)
plt.cla()   # Clear axis
plt.clf()   # Clear figure
#close()

#keylist = sorted(l3,key=lambda x: x[0])
#keylist2=sorted(l2,key=lambda x: x[0])
#keylist3=sorted(l1,key=lambda x: x[0])
#keylist = keylist+keylist2+keylist3
final=[]
final2=[]

#for a,b,c in zip(keylist,keylist2,keylist3):
#    fin.append(a[1]+b[1]+c[1])
#print (final)
list(keylist)
list(keylist2)
list(keylist3)

#t = [[0 for x in range(len(keylist))] for y in range(len(keylist))]

final=[]
for a in range(0,len(keylist)):
    temp=[]
    temp.append(keylist[a][0])
    temp.append(keylist[a][1]+keylist2[a][1]+keylist3[a][1])
    final.append(temp)

labels, ys = zip(*final)
xs = np.arange(len(labels)) 
width = 1

plt.bar(xs, ys, width, align='center')

plt.xticks(xs, labels) #Replace default x-ticks with xs, then replace xs with labels
plt.yticks(ys)
plt.savefig('final.png')
print(l3)
plt.cla()   # Clear axis
plt.clf()   # Clear figure
print(final)

