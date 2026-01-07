import spacy
import re

nlp = spacy.load("en_core_web_sm")

text1 = "Hello! How are you🙂?"
text2 = "Today's class has 2kids."
text3 = "I scored 100marks🙂 today!"

doc1 = nlp(text1)
doc2 = nlp(text2)
doc3 = nlp(text3)

tokens1 = [token.text for token in doc1]
tokens2 = [token.text for token in doc2]
tokens3 = [token.text for token in doc3]

print(tokens1)  # ==>['Hello', '!', 'How', 'are', 'you', '🙂', '?']
print(tokens2)  # ==>['Today', "'s", 'class', 'has', '2kids', '.']
print(tokens3)  # ==>['I', 'scored', '100marks', '🙂', 'today', '!']



print('\n\n')



# # Custom Tokenization to handle number-word issues and emojis
# def custom_tokenize(text):
#     text = re.sub(r'(\d+)([A-Za-z]+)', r'\1 \2', text)
#     return [token.text for token in nlp(text)]

# print(custom_tokenize("Today's class has 2kids."))
# print(custom_tokenize("I scored 100marks🙂 today!"))
