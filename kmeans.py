import numpy
import csv
from sklearn.cluster import KMeans
import collections
import glob

pas="D:/Lresult/NV_s5/b6t50_LDA_business/"
folder=glob.glob(pas+"*")
ifile=open(pas+"_2FUpthYr7h9VLNbe9Gxyw.csv","r")
idata=csv.reader(ifile)
revlist=collections.Counter()
star=collections.Counter()
for line in idata:
	if(line[3]=="5"):
		revlist[line[0]]=map(float,line[5:])
		star[line[0]]=line[3]
ifile.close()

kdata=numpy.array(revlist.values())
#print kdata

kmeans_model=KMeans(n_clusters=5,random_state=1).fit(kdata)
labels=kmeans_model.labels_

label=collections.Counter()
for num in range(0,len(revlist)):
	print revlist.keys()[num],labels[num],star[revlist.keys()[num]]
	label[revlist.keys()[num]]=labels[num]

wfile=open("D:/Lresult/hoge.csv","wb")
writer=csv.writer(wfile)
rfile=open("D:/Lresult/ks/NVrevraw.csv","r")
rdata=csv.reader(rfile)
for line in rdata:
	if(line[0] in revlist):
		doc=line
		doc.append(label[line[0]])
		writer.writerow(doc)
wfile.close()
rfile.close()
