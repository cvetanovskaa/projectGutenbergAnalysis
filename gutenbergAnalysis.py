from collections import Counter

class Analysis():	

	def __init__(self, fileName):
		self.fileName = fileName
	
	def getCollectionOfWords(self):
		c = Counter()
		with open(self.fileName, 'rb') as file:
			for line in file:
				c.update(line.split())
		return c

	def  getTotalNumberOfWords(self):
		c = self.getCollectionOfWords()
		return sum(c.values())
	
	def getTotalUniqueWords(self):
		c = self.getCollectionOfWords()
		return len(c.keys())

	def get20MostFrequentWords(self):
		c = self.getCollectionOfWords()
		wordsList = []
		for word, count in c.most_common(20):
			wordsList.append([word, count])		
		return wordsList

	def get20MostInterestingFrequentWords(self):
		mostFrequentWordsList = []
		with open('mostFrequentWords.txt', 'rb') as file:
			for line in file: 
				mostFrequentWordsList.append(line.rstrip('\n'))
		mostInterestingWordsList = []
		c = self.getCollectionOfWords()
		for word in c.keys():
			if (len(mostInterestingWordsList) == 20):
				return mostInterestingWordsList
			if word not in mostFrequentWordsList:
				mostInterestingWordsList.append(word)

	def get20LeastFrequentWords(self):
		c = self.getCollectionOfWords()
		wordsList = []
		for word, count in c.most_common()[-20:]:
			wordsList.append(word)
		return  wordsList
		
	def getFrequencyOfWord(self, word):
		frequencyInChapter = 0
		frequencyList = []
		with open(self.fileName, 'rb') as file:
			for line in file:
				if "Chapter" in line:
					frequencyList.append(frequencyInChapter)
					frequencyInChapter = 0
				else:
					line = line.strip(',')
					frequencyInChapter += line.split().count(word)
			return frequencyList[1:]
	

	
def main():
	analysis = Analysis("28054-0.txt")
	print analysis.getTotalNumberOfWords()
	print analysis.getTotalUniqueWords()
	print analysis.get20MostFrequentWords()
	print analysis.get20MostInterestingFrequentWords()
	print analysis.get20LeastFrequentWords()
	print analysis.getFrequencyOfWord("Fyodorovitch")
main()


	 
