pyg = 'ay'

original = input('Enter a word: ')

if len(original) > 0 and original.isalpha():  
  print (original)
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print (">")
  print (new_word)
  #This should translate common to pyglatin
else:
  print ('empty')