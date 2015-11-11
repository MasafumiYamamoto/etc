import csv
import collections

pas="D:/Lresult/NV_s5/b6t100_LDA_business_p/"
ifile=open(pas+"4bEjOyTaDG24SY5TxsaUNQ.csv","r")
idata=csv.reader(ifile)
ilist=collections.Counter()
for line in idata:
    ilist[line[0]]=line[5]
print ilist

wfile=open("D:/Lresult/ks/o4b6t100LDAbus_p/4bEjOyTaDG24SY5TxsaUNQ.csv","wb")
writer=csv.writer(wfile)
writer.writerow(["revid","userid","busid","star","date","text","clus"])
rfile=open("D:/Lresult/ks/NVrevraw.csv","r")
rdata=csv.reader(rfile)
for line in rdata:
    if(line[0] in ilist):
        doc=line
        doc=doc+[ilist[line[0]]]
        writer.writerow(doc)

ifile.close()
rfile.close()
wfile.close()
