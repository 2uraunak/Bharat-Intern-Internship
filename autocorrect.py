import nltk

def autocorrect(word):
  """Returns the most likely correct spelling of the word."""
  suggestions = nltk.suggest_spelling(word)
  if suggestions:
    return suggestions[0]
  else:
    return word

if __name__ == "__main__":
  word = "tehcnology"
  print(autocorrect(word))
