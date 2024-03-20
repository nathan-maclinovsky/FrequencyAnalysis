import random
import copy

def frequencyAnalysis(text):
  # Create a dictionary to store the frequency of each character in the text
  freq = {}
  for char in text.lower():
    if char in freq:
      freq[char] += 1
    else:
      freq[char] = 1
  
  # Sort the dictionary by frequency in descending order
  sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
  
  # Print the frequency of each character in the text
  spaces = freq[" "]
  for char, count in sorted_freq:
    print(f"{char}: {count} | percent: {count/(len(text) - spaces)*100}")

# Test the function with the text "The quick brown fox jumps over the lazy dog"

def letterSwitch(text,a,b):
  letters = list(text)
  for i in range(len(letters)):
    if letters[i] == a:
      letters[i] = b
    elif letters[i] == b:
      letters[i] = a  
      
  mytext = "".join(letters)
  return mytext


letters ="abcdefghijklmnopqrstuvwxyz"
def program():
  print("Welcome to my Caesar Cipher decryption via frequency analysis demo!")
  print()

def buildCipher(letters):
  ciphers = list(letters)
  for i in range(len(letters) - 1):
    tempLetter = ciphers[i]
    index = random.randint(0,25)
    ciphers[i] = ciphers[index]
    ciphers[index] = tempLetter
  cipher_map = {}
  for i in range(len(letters)):
    cipher_map[letters[i]] = ciphers[i]
  return cipher_map


  
  print(cipher_map)
buildCipher(letters)

def encrypt(text, cipher_map):
  text = list(text)
  for ind in range(len(text)):
    if text[ind] in cipher_map:
      text[ind] = cipher_map[text[ind]]
  text = "".join(text)    
  return text
 



text = "the quick brown fox jumps over the lazy dog ben bruh yo yup valvas jacob berns hellcat"
program()
map = buildCipher(letters)
text = encrypt(text, map)
text_copy = list(text)
while(True):
  print(text)
  frequencyAnalysis(text)
  x,y  = input("What letters do you wanna switch? Enter the letters seprated by a space: ").split()
  text = letterSwitch(text, x, y)

  