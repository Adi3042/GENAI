import nltk
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

# 1. Take raw text
text = "This is a SIMPLE text!!! NLP 2025 is amazing 🙂."

# 2. Lowercase
text = text.lower()  # "this is a simple text!!! nlp 2025 is amazing 🙂."
# 3. Remove punctuation and numbers
import string
text = "".join([ch for ch in text if ch not in string.punctuation and not ch.isdigit()])

# 4. Tokenize the text (convert sentence → words)
words = nltk.word_tokenize(text)

# 5. Remove stopwords
filtered = [word for word in words if word not in stopwords.words('english')]

print("Original Text after lowercasing:", text)
# Original Text after lowercasing: this is a simple text nlp  is amazing 🙂

print("Tokenized Words:", words)
# Tokenized Words: ['this', 'is', 'a', 'simple', 'text', 'nlp', 'is', 'amazing', '🙂']

print("Filtered Words:", filtered) 
# Filtered Words: ['simple', 'text', 'nlp', 'amazing', '🙂']