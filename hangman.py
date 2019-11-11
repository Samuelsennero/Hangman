import getpass
print()
print("Välkommen till hänga gubbe")
print()
print("Detta spel kräver minst 2 spelare, en som väljer ord och resten som gissar")
print()
word = getpass.getpass("Välj ett ord: ")

letters = sum(c.isalpha() for c in word)

print("Det valda ordet har", letters, "bokstäver")
print()


def get_guess():
  
  dashes = "-" * len(word)
  turns = 10
  
  while turns > -1 and not dashes == word:
    
    print()
    print ("Du har", str(turns), "gissningar kvar")
    print(dashes)

    guess = input("Gissa på en bokstav: ")
    
    if len(guess) != 1:
      print ("Bara en bokstav i taget!")
    elif guess in word:
      print ("Bra gissat!")
      dashes = update_dashes(word, dashes, guess)
    else:
      print ("Detta ord innehåller inte den bokstaven!")
      turns -= 1
    
  if turns < 0:
    print ("Du förlorar, ordet var: " + str(word))
  else:
    print ("Grattis! Du vann, ordet var: " + str(word))
    

def update_dashes(secret, cur_dash, rec_guess):
  result = ""
  
  for i in range(len(secret)):
    if secret[i] == rec_guess:
      result = result + rec_guess   
    else:
      result = result + cur_dash[i]
      
  return result
    
get_guess()
