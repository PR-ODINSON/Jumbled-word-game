import random
from random_word import RandomWords
print("Welcome to the Jumble Game")
player_1=input("Enter Player1 name: ")
player_2=input("Enter Player2 name: ")

def choose_words():
    # Using the RandomWords class to get a random word
  r = RandomWords()
  return r.get_random_word()

def jumbled_words(word):
    # Creating a jumbled version of the word
  jumbled="".join(random.sample(word,len(word)))
  return jumbled

def Thank_you(player_1,player_2,point_1,point_2):
    # Displaying final scores and a thank you message
  print(player_1,"Your score is",point_1)
  print(player_2,"Your score is",point_2)
  print("Thank you for playing with us")
  print("Have a nice day")




def play(point_1,point_2):
  turn=0
  while(1):
    picked_word=choose_words()
    question=jumbled_words(picked_word)
    print("The jumbled word is-->",question)
    print("Hint: The first leter should be",picked_word[0],"And the last letter should be",picked_word[-1])
    if turn%2==0:
      print(player_1,"Your Turn to play")
      answer=input("What's on your mind? ")
      if answer== picked_word:
        point_1+=1
      
      print(player_2,"Your Turn to play")
      answer=input("What's on your mind? ")
      if answer==picked_word:
        point_2+=1

      print("BTW the correct word is",picked_word)
        
      d = int(input(player_1 + ", Press 1 to continue and 0 to quit: "))
      c = int(input(player_2 + ", Press 1 to continue and 0 to quit: "))

      if c==0 and d==0:
        Thank_you(player_1,player_2,point_1,point_2)
        break
      else:
        print("Your score is",point_1)
        print("Your score is",point_2)
        turn+=1
        play(point_1,point_2)

      


play(point_1=0,point_2=0)


        
    
