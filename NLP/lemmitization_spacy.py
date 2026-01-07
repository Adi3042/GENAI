import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

print("Example 1: Basic Lemmatization (No POS mentioned)")
doc1 = nlp("cars running")
for token in doc1:
    print(token.text, "->", token.lemma_)
    # OUTPUT:
        # cars -> car
        # running -> run

print("\nExample 2: Sentence Lemmatization")
text = "The children are playing games"
doc2 = nlp(text)
lemmatized_words = [token.lemma_ for token in doc2]
print(lemmatized_words)
# Output: ['the', 'child', 'be', 'play', 'game']

print("\nExample 3: Lemmatization with POS Display")
doc3 = nlp("better running flies")
for token in doc3:
    print(f"{token.text} ({token.pos_}) -> {token.lemma_}")
# OUTPUT:
    # better (ADV) -> well
    # running (VERB) -> run
    # flies (NOUN) -> fly