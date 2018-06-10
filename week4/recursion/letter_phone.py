from array import *

def get_mapping(digit):
    mapping = { '0':'0', '1':'1', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
    chars = mapping.get(digit, None)
    return chars
    
def get_char(digit, index): 
  """
  returns a character mapped to a digit on a telephone for given index
  """
  chars = get_mapping(digit)
  return chars[index] if chars and index < len(chars) else None

def generate_words(digits, index, words, word):
  """
  generates words for given digits
  """
  # base case, when index reachs to the end of the word, get the word temporarily generated in the array
  if index == len(digits):    
    words.append(''.join(word))
    return
  else:
    # recursively call for each position in the word
    if digits[index] == '0' or digits[index] == '1':
        _range = 1
    else:
        _range = len(get_mapping(digits[index]))
    for i in range(_range):
      ch = get_char(digits[index], i)
      # temporarily save the word in an array
      if ch: word[index] = ch
      generate_words(digits, index+1, words, word)

def main():
  digits = "23"
  words = []
  word = array('c', [' ' for _ in digits])
  generate_words(digits, 0, words, word)
  print "words : %s" % (words)

if __name__ == "__main__":
  main()
