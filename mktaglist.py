import csv

max=10
infile='i.csv'
ifile=open(infile,'r')
wfile=open("wfile.csv","wb")

idata=csv.reader(ifile)
csvwriter=csv.writer(wfile)


taglist=["id"]
next(idata)
limit=1
for line in idata:
	for num in range(1,len(line)):
		flag=1
		for n in range(0,len(taglist)):
			if(taglist[n]==line[num]):
				flag=0
				break
		if(flag==1 and line[num]!=''):
			taglist.append(line[num])
	limit=limit+1
	if(limit>max):
		break

print len(taglist)
csvwriter.writerow(taglist)

ifile=open(infile,"r")
idata=csv.reader(ifile)

next(idata)
limit=1
for line in idata:
	wlist=[0]*len(taglist)
	wlist[0]=line[0]
	for num in range(1,len(line)):
		for n in range(1,len(taglist)):
			if(line[num]==taglist[n]):
				wlist[n]=1
		
	csvwriter.writerow(wlist)
	limit=limit+1
	if(limit>max):
		break


ifile.close()
wfile.close()
