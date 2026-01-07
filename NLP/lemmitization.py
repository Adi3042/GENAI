import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()

# Example 1: Single Word Lemmatization
print(lemmatizer.lemmatize("cars"))  # ==> car
print(lemmatizer.lemmatize("running"))  # ==> running

print(lemmatizer.lemmatize("cars", pos="n"))    # ==> car
print(lemmatizer.lemmatize("running", pos="v"))  # ==> run

# Example 2: Sentence Lemmatization
text = "The children are playing games"
tokens = word_tokenize(text)
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
print(lemmatized_words) # ==> ['The', 'child', 'are', 'playing', 'game']

# Example 3: Lemmatization with POS (Better Accuracy)
words = ["better", "running", "flies"]
print(lemmatizer.lemmatize("better", pos="a"))  # good (adjective)
print(lemmatizer.lemmatize("running", pos="v")) # run (verb)
print(lemmatizer.lemmatize("flies", pos="n"))   # fly (noun)