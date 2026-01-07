from nltk.stem import PorterStemmer, LancasterStemmer

# Initialize stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()  

# Stem words
p_words = porter.stem('Dancing')
l_words = lancaster.stem('Dancing')  

# Print results
print("Porter Stemmer:", p_words)   # ==> Porter Stemmer: danc
print("Lancaster Stemmer:", l_words)    # ==> Lancaster Stemmer: dant