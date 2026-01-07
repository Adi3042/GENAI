# Import TF-IDF Vectorizer from sklearn
from sklearn.feature_extraction.text import TfidfVectorizer

# Corpus = list of documents/sentences
# Example: 1
corpus = ["I love cake", "I love bun"]

# Create TF-IDF vectorizer object
vectorizer = TfidfVectorizer()

# Fit the model on corpus and transform text into TF-IDF matrix
X = vectorizer.fit_transform(corpus)

# Get unique words (features) from corpus
print("Features:", vectorizer.get_feature_names_out())  # ==> Features: ['bun' 'cake' 'love']

# Convert sparse matrix to array and print
print("TF-IDF Matrix:")
print(X.toarray())
# TF-IDF Matrix: 
# [[0.         0.81480247 0.57973867]
#  [0.81480247 0.         0.57973867]]


# Example 2: 
corpus2 = ["Data science is fun", "Data science is powerful"]
vectorizer2 = TfidfVectorizer()
X2 = vectorizer2.fit_transform(corpus2)

# Print feature names
print("\nFeatures (Example 2):", vectorizer2.get_feature_names_out())
# Features (Example 2): ['data' 'fun' 'is' 'powerful' 'science']

# Print TF-IDF values
print("TF-IDF Matrix (Example 2):")
print(X2.toarray())
# TF-IDF Matrix (Example 2):
# [[0.44832087 0.63009934 0.44832087 0.         0.44832087]
#  [0.44832087 0.         0.44832087 0.63009934 0.44832087]]