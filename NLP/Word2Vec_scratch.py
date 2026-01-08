# Word2Vec: CBOW and Skip-gram 

# Import Word2Vec model from gensim
from gensim.models import Word2Vec

# STEP 1: Prepare tokenized sentences
sentences = [
    ["i", "love", "chocolate", "cake"],
    ["i", "love", "icecream"],
    ["cake", "is", "very", "tasty"],
    ["chocolate", "cake", "is", "delicious"]
]

# STEP 2: CBOW Model (sg = 0)
# CBOW predicts the TARGET word using CONTEXT words
# Example: (i love ___ cake) → chocolate
cbow_model = Word2Vec(
    sentences=sentences,   # training data
    vector_size=50,        # size of word embedding vector
    window=2,              # number of context words (left + right surrounding words)
    min_count=1,           # include all words (even rare ones)
    sg=0                   # sg=0 means CBOW
)

# Print embedding vector of the word "cake"
print("\nCBOW Embedding for 'cake':")
print(cbow_model.wv["cake"])


# STEP 3: Skip-gram Model (sg = 1)
# Skip-gram predicts CONTEXT words from TARGET word
# Example: chocolate → (i, love, cake)
skipgram_model = Word2Vec(
    sentences=sentences,   # training data
    vector_size=50,        # size of embedding
    window=2,              # context window size
    min_count=1,           # FIXED: correct parameter name
    sg=1                   # sg=1 means Skip-gram
)

# Print embedding vector of the word "cake"
print("\nSkip-gram Embedding for 'cake':")
print(skipgram_model.wv["cake"])


# STEP 4: Word Similarity
# Measures semantic similarity using cosine similarity
# Value range: -1 to +1

print("\nSimilarity between 'cake' and 'chocolate':")
print(skipgram_model.wv.similarity("cake", "chocolate"))

# --------------------------------------------
# vector_size ==> Bigger vector_size = more detail, but more computation
# 50 → small projects
# 100–300 → real-world NLP
# 768 → BERT-like models

# --------------------------------------------
# window ==> context window ==> How many words around a target word should the model look at
# A word’s meaning depends on surrounding words.
# Example:
#     "bank" near "money" → finance
#     "bank" near "river" → nature

# -------------------------------------------
# min_count ==> Minimum number of times a word must appear to be included
# Example text ==> cake cake cake icecream donut
#     Word	    Count
#     cake	    3
#     icecream	1
#     donut	    1

# If min_count = 1 ==> cake, icecream, donut
# If min_count = 2 ==> cake