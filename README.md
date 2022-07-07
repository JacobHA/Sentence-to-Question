# Sentence to Question
Uses NLTK to translate a given English statement to the question form.
This may be useful for natural language processing.
Requires NLTK as import (must also download NLTK databases).

# TODO:
- [x] check the tenses on certain verbs when converting
- [ ] add proper noun handling
- [ ] create an inverse function that converts a question to an English statement

## Requirements:
nltk
----
Do the following in a separate console (so as not to download each time the script is run):
`
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4') 
`