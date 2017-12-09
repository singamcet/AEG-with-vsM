import re
import math

def __main__():

	dict_1 = {}
	dict_2 = {}

	count1 = 0
	count2 = 0

	sum = 0

	file_1 = raw_input("Enter 1st file name:") #takes in the first file name
	file_2 = raw_input("Enter 2nd file name:") #takes in the second file

	with open(file_1,"r") as f1:
		for line in f1:	#loop to handle the words in the first file
			wordList = re.sub("[^\w]"," ",line).split() #using regex to first exchange all non-alphanumeric characters with a space and then spliting it with space as the delimiter
			for	word in wordList: 
				word = word.lower() #converting all letters to lower case so that case is not a problem
				if word in dict_1:	#if the spilt word has already appeared in the dictionary, then increase its count else introduce the word
					dict_1[word] += 1
				else:
					dict_1[word] = 1

	for word in dict_1:
		count1 += dict_1[word] * dict_1[word] #creating the absolute value of the vector of words in first file
	count1 = math.sqrt(count1)

	with open(file_2,"r") as f2:
		for line in f2:	#same purpose as loop 1 just now for the second file
			wordList = re.sub("[^\w]", " ",line).split()
			for word in wordList:
				word = word.lower()
				if word in dict_2:
					dict_2[word] += 1
				else:
					dict_2[word] = 1

	for word in dict_2:
		count2 += dict_2[word] * dict_2[word]
	count2 = math.sqrt(count2)

	for word in dict_1:	#matching words in both the dictionaries; More the words match, higher the similarity
		if word in dict_2:
			sum += (dict_1[word] * dict_2[word]) #creating the dot product of the vectors of file 1 and 2

	similarity = (float) (sum )/ (count2 * count1) # taking the similarity as the angle between the two vectors

	print format(similarity,'.2f')

	raw_input("Press any key to exit")

__main__() 