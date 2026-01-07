# Install NLTK library (run once in terminal)
# pip install nltk
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text1 = "Hello! How are you🙂?"
text2 = "Today's class has 2kids."
text3 = "I scored 100marks🙂 today!"
tokens1 = word_tokenize(text1)
tokens2 = word_tokenize(text2)
tokens3 = word_tokenize(text3)
# tokens_split = text.split()
print(tokens1)   # ['Hello', '!', 'How', 'are', 'you🙂', '?'] ==>  Emoji is attached to the word
print(tokens2)   # ['Today', "'s", 'class', 'has', '2kids', '.'] ==>  Number-Word issue
print(tokens3)   # ['I', 'scored', '100marks🙂', 'today', '!'] ==>  Number-Word issue and emoji attached to word
