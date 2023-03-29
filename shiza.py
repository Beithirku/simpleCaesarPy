def encodeCaesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalnum():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
        return
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
      
  print("                      Your ciphertext is: ", cipherText)
  return cipherText


def decodeCaesar(cipherText, shift): 
  plainText = ""
  for ch in cipherText:
    if ch.isalnum():
      stayInAlphabet = ord(ch) - shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
        return
      finalLetter = chr(stayInAlphabet)
      plainText += finalLetter
      
  print("                      Your plaintext is: ", plainText)
  return plainText

def menu():
  print("                     Welcome to a simple Caesar Cipher program!")
  print()
  
  choice = int(input("""
                      1: Encode
                      2: Decode

                      Please enter your choice:"""))
  

  if choice == 1:
    plainText = input("                      What is your plaintext? ")
    shift = int(input("                      What is your shift? "))
    print(shift)
    encodeCaesar(plainText, shift)
      
  if choice == 2:
    cipherText = input("                      What is your ciphertext? ")
    shift = int(input("                      What shift was used? "))
    print(shift)
    decodeCaesar(cipherText, shift) 

menu()