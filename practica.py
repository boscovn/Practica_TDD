class StatClass(object):			
	@staticmethod
	def wordStats(text):
		import string
		lista = []
		from words import stopWordsEs as stop
		count = {}
		for sign in string.punctuation:
			text=text.replace(sign, "")
		for word in text.lower().split():
			if word in stop:
				pass
			elif word not in count:
				count[word]=1
			else:
				count[word] +=1
		valores = sorted(set(count.values()))
		for v in valores:
			for key in count:
				if count[key]==v:
					lista.append ("%s %s"% (key, v))
		return lista	