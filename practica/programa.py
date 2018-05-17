import string
from . import stop_words
def wordStats(text):
	count={}
	result=[]
	for sign in string.punctuation:
		text = text.lower().replace(sign, "")
	for word in text.split():
		if word in stop_words.stopWordsEs:
			break
		elif word in count:
			count[word] +=1
		else:
			count[word]=1
	for v,k in sorted( ((v,k) for k,v in count.items())):
		result.append("%s %d" % (k,v))
	return result
