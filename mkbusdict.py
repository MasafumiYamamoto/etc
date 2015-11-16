###make bow list

def main():
	from gensim import corpora, models, similarities
	import csv
	import textedit
	import time
	import collections
	import glob

	stopfile=open("D:/Lresult/NV_s5/subrev_1000.csv","r")
	stopdata=csv.reader(stopfile)
	stoplist=collections.Counter()
	for line in stopdata:
		stoplist[line[0]]=1
	stopfile.close()

	buslist=glob.glob("D:/Lresult/NVbus/*")
	print len(buslist)

	##make document bow
	for bus in buslist:
		dfile=open(bus,"r")
		ddata=csv.reader(dfile)
		dlist=[]
		busname=""
		for line in ddata:
			busname=line[2]
			if(line[0] not in stoplist):
					te=line[5]
					doc=textedit.textedit(te)
					dlist.append(doc)
		dfile.close()
		texts = [[word for word in document.lower().split()] for document in dlist]
		dictionary = corpora.Dictionary(texts)
		dictionary.save_as_text("D:/Lresult/NVbusdict/"+busname+".dict")

if __name__ == '__main__':
	main()
