# pip install scikit-learn
from sklearn.feature_extraction.text import CountVectorizer

documents = [
    "I love Cake",
    "I love Bun",
    "I love Biryani"]

# Apply BoW:-
vectorizer = CountVectorizer()

X = vectorizer.fit_transform(documents)

print("Vocabulary:", vectorizer.get_feature_names_out()) # ==> Vocabulary: ['biryani' 'bun' 'cake' 'love']
print("BoW Matrix:\n", X.toarray())
# BoW Matrix:
#  [[0 0 1 1]
#  [0 1 0 1]
#  [1 0 0 1]]