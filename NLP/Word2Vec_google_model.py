# import os
# os.environ["GENSIM_DATA_DIR"] = "E:/Generative AI/NLP/gensim_data"

import gensim.downloader as api
import numpy as np

# Load Google pre-trained Word2Vec model (300 dimensions)
model = api.load("word2vec-google-news-300")

# Input sentence
text = "Machine Learning is Great"

# Tokenize and keep only words present in the model
words = [word for word in text.lower().split() if word in model.key_to_index]

if words:
    # Create sentence vector by averaging word vectors
    Vector = np.mean([model[word] for word in words], axis=0)

    print("Vector Shape:", Vector.shape)   # (300,)
    print(Vector)
else:
    print("No Words found in the model vocabulary")









# Exception: Can't create C:\Users\Admin/gensim-data. Make sure you have the read/write permissions to the directory or you can try creating the folder manually
# import os
# os.environ["GENSIM_DATA_DIR"] = "E:/Generative AI/NLP/gensim_data"