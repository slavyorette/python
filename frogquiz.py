print("Frog Quiz!")

score = 0

ans1 = input("\nWhat class of animals are frogs? \n A. Mammals \n B. Birds \n C. Reptiles \n D. Amphibians \nType the letter of your answer: ")
if ans1.lower() == "d":
  score += 1
  print("Correct! Yay :D")
else:
  print("You got it wrong :C")
  
ans2 = input("\nFrogs can breathe through all of the following except for... \n A. Liver \n B. Lungs \n C. Mouth Lining \n D. Skin \nType the letter of your answer: ")
if ans2.lower() == "a":
  score += 1
  print ("Correct! Yay :D")
else:
  print("You got it wrong :C")

ans3 = input("\nWhat is the size of the smallest frog? \n A. 13 centimetres \n B. 5 centimetres \n C. 7 millimeters \n D. 4 millimeters \nType the letter of your answer: ")
if ans3.lower() == "c":
  score += 1
  print ("Correct! Yay :D")
else:
  print("You got it wrong :C")
  
ans4 = input("\nWhat do you call a group of frogs? \n A. A swarm \n B. A ribbit \n C. An army \n D. A school \nType the letter of your answer: ")
if ans4.lower() == "c":
  score += 1
  print ("Correct! Yay :D")
else:
  print("You got it wrong :C") 
  
ans5 = input ("\nHow long have frogs been on Earth? \n A. 100 million years \n B. 200 million years \n C. 300 million years \n 4. 500 million years \nType the letter of your answer: ")
if ans5.lower() == "b":
  score += 1
  print("Correct! Yay :D")
else:
  print("You got it wrong :C")
  
print("\nYour score was " + str(score) + ". \nThank you for playing!")
