def calc(count):
  
  none = """
  ______
  |    |      
  |          
  |        
  |    
  |    
 _|_
|   |______
|          |
|__________|

"""



  head = """
  ______
  |    |      
  |    o      
  |        
  |    
  |    
 _|_
|   |______
|          |
|__________|

"""

  body = """
 ______
  |    |      
  |    o      
  |    |     
  |    |
  |    
 _|_
|   |______
|          |
|__________|

"""

  leftArm = """
 ______
  |    |      
  |    o      
  |   /|    
  |    |
  |    
 _|_
|   |______
|          |
|__________|

"""



  rightArm = """
 ______
  |    |      
  |    o      
  |   /|\     
  |    |
  |    
 _|_
|   |______
|          |
|__________|

"""



  leftLeg = """
 ______
  |    |      
  |    o      
  |   /|\     
  |    |
  |   / 
 _|_
|   |______
|          |
|__________|

"""




  rightLeg = """
 ______
  |    |      
  |    o      
  |   /|\     
  |    |
  |   / \\
 _|_
|   |______
|          |
|__________|

"""
  if count == 7:
    return none
  if count == 6:
    return head 
  if count == 5:
    return body
  if count == 4:
    return leftArm
  if count == 3:
    return rightArm
  if count == 2:
    return leftLeg
  if count == 1:
    return rightLeg
    

  
    
  
list = []
guessList = []
secretWord = input('Enter your word to guess: ')
secretWord = secretWord.lower()
for i in secretWord:
  list.append(i)
  guessList.append('_')

counter = 7
print(calc(counter))
print(guessList)

#index = 0
while guessList != list:
  guess = input('\n guess a letter: ')
  if guess in list:
      for i in range(len(list)):
        if guess == list[i]:
          print(calc(counter))
          print("\nCorrect!\n")
          pos = list[i]
          guessList.pop(i)
          guessList.insert(i, list[i])
          print(guessList)
          
  if guess not in list:
    if counter == 2:
      print(calc(counter -1))
      print("you have been hung")
      break
    counter -= 1
    print(calc(counter))
    print(guessList)
    print("\n you have {} tries left".format(counter-1))
    
      
      
if guessList == list:
  print("\n\nyou have won the game")
