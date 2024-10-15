def can_be_made_of_letters(word, letters):
  for e in word:
    if word.count(e) > letters.count(e):
      return False
  return True

def possible_words(wordlist, letters):
   words = []
   for e in wordlist:
      if can_be_made_of_letters(e, letters):
         words.append(e)
   return words
