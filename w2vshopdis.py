import csv
import collections
import numpy
import textedit

print "dim"
dim=raw_input()
pas="D:/Lresult/w2v/"

#####load stopword
stopfile=open("D:/Lresult/stopwords/over4word.csv","r")
stopdata=csv.reader(stopfile)
stoplist=[]
for line in stopdata:
	stoplist.append(line[0])
stopfile.close()

####load vecfile
dfile=open(pas+"scmodoki"+str(dim)+"_5.csv","r")
ddata=csv.reader(dfile)
ddic=collections.Counter()
for line in ddata:
	ddic[line[0]]=map(float,line[1:])
dfile.close()
print "dic fin",len(ddic),len(ddic["we"])

##base data
revfile=open("D:/Lresult/subrev_1000.csv","r")
revdata=csv.reader(revfile)
revdata.next()
revid=collections.Counter()
revvec=collections.Counter()
for line in revdata:
	revid[line[0]]=line[1]
	text=textedit.textedit(line[2])
	revvec[line[0]]=numpy.array([0]*int(dim))
	for num in range(0,len(text)):
		if(num not in stoplist):
			revvec[line[0]]=revvec[line[0]]+numpy.array(ddic[text[num]])
revfile.close()
print "rev fin",len(revvec)

####comp data
sfile=open("D:/Lresult/NVreview.csv","r")
sdata=csv.reader(sfile)
sdata.next()
svec=collections.Counter()
lnum=0
slist=[]
for line in sdata:
	if(line[0] not in revid):
		if(line[2] not in slist):
			slist.append(line[2])
			svec[line[2]]=numpy.array([0]*int(dim))
		else:
			doc=textedit.textedit(line[5])
			text=doc.lower().split()
			for num in range(0,len(text)):
				if(num not in stoplist):
					svec[line[2]]=svec[line[2]]+numpy.array(ddic[text[num]])
	if(lnum%100000==0):
		print lnum
	lnum=lnum+1
sfile.close()
print "base din",len(svec)

###calc sim svec and revvec
for rid in revid:
	wfile=open(pas+"res_o4t"+str(dim)+"/"+rid+".csv","wb")
	writer=csv.writer(wfile)
	writer.writerow(["revid","busid","sim","seikai"])
	rlen=numpy.linalg.norm(revvec[rid])
	if(rlen!=0):
		for sid in svec:
			slen=numpy.linalg.norm(svec[sid])
			if(slen!=0):
				sim=numpy.dot(revvec[rid],svec[sid])/slen/rlen
				writer.writerow([rid,sid,sim,revid[rid]])
	wfile.close()
