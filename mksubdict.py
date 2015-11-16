###make bow list for each line

def main():
	from gensim import corpora
	import csv
	import textedit
	import collections

	stopfile=open("D:/Lresult/NV_s5/subrev_1000.csv","r")
	stopdata=csv.reader(stopfile)
	stoplist=collections.Counter()
	for line in stopdata:
		te=line[5]
		dlist=[]
		doc=textedit.textedit(te)
		dlist.append(doc)
		texts = [word for word in document.lower().split()] 
		dictionary = corpora.Dictionary(texts)
		dictionary.save_as_text("D:/Lresult/NV_s5/subrevdict/"+line[0]+".dict")
	stopfile.close()

if __name__ == '__main__':
	main()
