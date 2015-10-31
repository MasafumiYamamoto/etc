from gensim import corpora, models, similarities
import csv
import time

def textedit(text):
	te=text.lower()
	te=te.replace("!"," ")
	te=te.replace('"'," ")
	te=te.replace("#"," ")
	te=te.replace("$"," ")
	te=te.replace("%"," ")
	te=te.replace("&"," ")
	te=te.replace("'"," ")
	te=te.replace("("," ")
	te=te.replace(")"," ")
	te=te.replace("="," ")
	te=te.replace("-"," ")
	te=te.replace("^"," ")
	te=te.replace("~"," ")
	te=te.replace("|"," ")
	te=te.replace("["," ")
	te=te.replace("]"," ")
	te=te.replace("{"," ")
	te=te.replace("}"," ")
	te=te.replace("`"," ")
	te=te.replace("@"," ")
	te=te.replace("+"," ")
	te=te.replace(";"," ")
	te=te.replace("*"," ")
	te=te.replace(":"," ")
	te=te.replace("<"," ")
	te=te.replace(","," ")
	te=te.replace(">"," ")
	te=te.replace("."," ")
	te=te.replace("?"," ")
	te=te.replace("/"," ")
	te=te.replace("_"," ")
	return te

pas="D:/Lresult/"
print "mkcorpus_start",time.ctime()
dlist=[]
dfile=open(pas+"nNVreview.csv","r")
ddata=csv.reader(dfile)
dnum=0
for line in ddata:
	te=line[0]
	doc=textedit.textedit(te)
	dlist.append(doc)
	dnum=dnum+1
	if(dnum%10000==0):
		print dnum,
dfile.close()
print "dfile fin",len(dlist),ime.ctime()

#texts = [[word for word in document.lower().split()] for document in dlist]
#print "text fin",time.ctime()
# remove words that appear only once
#all_tokens = sum(texts, [])
#tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
#texts = [[word for word in text if word not in tokens_once] for text in texts]
print "input word"
word=raw_input()
for el in dlist:
	if(word in el) :
