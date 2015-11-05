import csv
import glob
import collections
import numpy
import time
import textedit

pas="D:/Lresult/"
tnum=100

###load stopwords
sfile=open(pas+"stopwords/b6list.csv","r")
stoplist=collections.Counter()
sdata=csv.reader(sfile)
for line in sdata:
    stoplist[line[0]]=1
sfile=open(pas+"stopwords/over4word.csv","r")
sdata=csv.reader(sfile)
for line in sdata:
    stoplist[line[0]]=1
sfile.close()
print "stop fin",time.ctime(),len(stoplist)

###ake subrev list
subfile=open(pas+"NV_s5/subrev_1000.csv","r")
subdata=csv.reader(subfile)
subdata.next()
subidlist=collections.Counter()
for line in subdata:
    subidlist[line[0]]=line[1]
subfile.close()
print "sub fin"

###laod train bow
busbowlist=glob.glob(pas+"NVbus/*")
bblist=collections.Counter()
bblen=collections.Counter()
for bus in busbowlist:
    busname=bus[6:-4]###bus_id####
    bblist[busname]=collections.Counter()
    bfile=open(bus,"r")
    bdata=csv.reader(bfile)
    for line in bdata:
        if(line[0] not in subidlist):
            doc=textedit.textedit(line[5])
            doc=doc.lower().split()
            for t in doc:
                if(t not in stoplist):
                    bblist[busname][t]=bblist[busname][t]+1
    bblen[busname]=numpy.linalg.norm(bblist[busname].values())
    bfile.close()
print "train fin",len(bblist),time.ctime()
#print bblen

###load subrev bow
subfile=open(pas+"NV_s5/subrev_1000.csv","r")
subdata=csv.reader(subfile)
subdata.next()
snum=0
for line in subdata:
    snum=snum+1
    if(snum%100==0):
        print snum,time.ctime()
    sublist=collections.Counter()
    doc=textedit.textedit(line[5])
    doc=doc.lower().split()
    for t in doc:
        if(t not in stoplist):
            sublist[t]=sublist[t]+1
    ###print sublist
    snum=snum+1
    sublen=numpy.linalg.norm(sublist.values())
    wfile=open(pas+"bowo4b6/"+line[0]+".csv","wb")
    writer=csv.writer(wfile)
    writer.writerow(["revid","busid","score","seikai"])
    for bus in bblist:
        #print bblist[bus]
        score=0
        if(bblen[bus]*sublen!=0):
            for t in sublist:
                if(t in bblist[bus]):
                    score=score+bblist[bus][t]*sublist[t]
            score=score/bblen[bus]/sublen
      #  print line[0],bus,score,sublen,bblen[bus]
        writer.writerow([line[0],bus,score,line[2]])
    wfile.close()
