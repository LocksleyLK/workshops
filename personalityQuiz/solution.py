answer = input( "What is your favorite color?\n(A) Red\n(B) Blue\n(C) Green\n(D) Purple" )
answer = input( "What would you like to major in?\n(A) Business\n(B) Law\n(C) Mathematics\n(D) Computer Science\n(E) Other")
answer = input( "3. What company would you most like to work for?\n(A) NASA\n(B) Google\n(C) Start my own company" )
answer = input( "What is the best invention?\n(A) Space travel\n(B) Smart phones\n(C) The internet" )

reshma = 0
margaret = 0
susan = 0
katherine = 0

if answer == "A":
  reshma += 1
elif answer == "B":
  margaret += 1
elif answer == "C":
  susan += 1
elif answer == "D":
  katherine += 1
else:
	print("You did not select one of the answers for question 1. We're going to say you selected A")
	reshma += 1
  
if answer == "B":
  reshma += 1
elif answer == "A" or "E":
  susan += 1
elif answer == "C" or "D":
  margaret += 1
  katherine += 1
else:
  print("You did not select one of the answers for question 2. We're going to say you selected C")
  margaret += 1
  katherine += 1

if answer == "A":
  margaret += 1
  katherine += 1
elif answer == "B":
  susan += 1
elif answer == "C":
  reshma += 1;
else:
  print("You did not select one of the answers for question 3. We're going to say you selected B")
  susan += 1  
  
if answer == "A":
  margaret += 1
  katherine += 1
elif answer == "B":
  susan += 1
elif answer == "C":
  reshma += 1;
else:
  print("You did not select one of the answers for question 4. We're going to say you selected A")
  margaret += 1
  katherine += 1
  
if (reshma > margaret and susan and katherine):
	print("Congratulations! You are most like Reshma!")
elif (margaret > reshma and susan and katherine):
  print("Congratulations! You are most like Margaret!")
elif (susan > margaret and susan and katherine):
  print("Congratulations! You are most like Susan!")
else:
  print("Congratulations! You are most like Katherine!")
