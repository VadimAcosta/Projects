import random
num  = random.randint(0,1)

   

def flip_the_coin(call):
    
    call = input("Please enter Heads or Tails: ")
   
    if call == "Heads" and num == 0:
        return "It's Heads, you win!"
    
    elif call == "Tails" and num == 1:   
        return "It's Tails, you win!"
    
    elif call == "Heads" and num == 1:
        return "It's Tails, you lose!"
    
    elif call == "Tails" and num == 0:
        return "It's a Heads, you lose!"
    
    else:
        return "Please input 'Heads' or 'Tails', remember to capitalize"

print (flip_the_coin(call))





