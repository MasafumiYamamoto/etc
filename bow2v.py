import csv
import glob
import collections
import numpy
import time

pas="D:/Lresult/"
tnum=100

###ake subrev list
subfile=open(pas+"subrev_1000.csv","r")
subdata=csv.reader(subfile)
subdata.next()
subidlist=collections.Counter()
for line in subdata:
    subidlist[line[0]]=line[1]
subfile.close()

####load w2v list
w2vfile=open(pas+"w2v/scmodoki"+str(tnum)+"_5.csv")
w2vdata=csv.reader(w2vfile)
w2vdic=collections.Counter()
for line in w2vdata:
    w2vdic[line[0].lower()]=map(float,line[1:])
w2vfile.close()
print "w2v fin",len(w2vdic),time.ctime()

###laod train bow
busbowlist=glob.glob("D:/Lresult/NVbus_o4_bow/*")
bblist=collections.Counter()
for bus in busbowlist:
    busname=bus[24:-4]###bus_id####
    bblist[busname]=collections.Counter()
    bfile=open(bus,"r")
    bdata=csv.reader(bfile,delimiter="\t")
    for line in bdata:
        bblist[busname][line[1]]=int(line[2])
    bfile.close()
print "train fin",len(bblist),time.ctime()

###load subrev bow
subbowlist=glob.glob(pas+"NVsub_o4_bow/*")
snum=0
for subrev in subbowlist:
    snum=snum+1
    ifile=open(subrev,"r")
    idata=csv.reader(ifile,delimiter="\t")
    revname=subrev[24:-4]
    print revname,time.ctime(),snum
    wfile=open(pas+"res/"+revname+".csv","wb")
    writer=csv.writer(wfile)
    writer.writerow(["revid","busid","sim","seikai"])
    sblist=collections.Counter()####bow dic
    for line in idata:
        sblist[line[1]]=int(line[2])
    ifile.close()
    bnum=0
    for bus in bblist:
        bnum=bnum+1
        print revname,bus,bnum
        score=0
        sblen=numpy.linalg.norm(sblist.values())
        if(sblen!=0):
            for t in sblist:
                if(t in w2vdic):
                    tvec=w2vdic[t]
                    minw=""
                    mind=10000
                    match=0
                    bblen=numpy.linalg.norm(bblist[bus].values())
                    if(bblen!=0):
                        for w in bblist[bus]:
                            if(t==w):
                                match=1
                            wvec=w2vdic[w]
                            d=numpy.linalg.norm(numpy.array(tvec)-numpy.array(wvec))
                            if(d<mind):
                                minw=w
                                mind=d
                        if(mind<1):
                            if(match==1):
                                minw=t
                            score=score+sblist[t]*bblist[bus][minw]
                else:
                    for w in bblist:
                        if(t==w):
                            score=score+sblist[t]*bblist[bus][t]
        if(sblen!=0 and bblen!=0):
            score=score/sblen/bblen
        writer.writerow([revname,bus,score,subidlist[revname]])
    ifile.close()
    wfile.close()
