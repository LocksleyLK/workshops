<img
  src="photos/Women in Tech.png"
  alt="Women in Tech: Reshma Saujani, Margaret Hamilton, Susan Wojcicki, and Katherine Johnson"
  style="float: left; margin-right: 90px;"
/>

# Learn Python with the Women in Tech Personality Quiz

## Created by **Locksley Kolakowski** with inspiration from the [Learn Python basics with Wonder Woman](https://docs.microsoft.com/en-us/learn/paths/python-partnership/) Microsoft Learn module!

| **Project Goal**            | **Build a Women in Tech Personality Quiz** |
|-------------------------|----------------------------------------|
| **What you'll learn**       | Learn about variables, if/else statements, functions, and more in the Python programming language  |
| **Tools you'll need**       | [Python Sandbox](http://pythonsandbox.com/) |
| **Time needed to complete** | <1 hour                                |
| **Finished Solution**       | [Link](https://github.com/LocksleyLK/workshops/blob/main/personalityQuiz/solution.py) |

## Let's meet our inspiring Women in Tech!

### Reshma Saujani
Reshma Saujani is the Founder and CEO of Girls Who Code. Girls Who Code is leading the movement to inspire, educate, and equip young women with the computing skills to pursue 21st century opportunities. [Source](https://reshmasaujani.com/about/).

### Margaret Hamilton
Margaret Hamilton led the NASA software team that landed astronauts on the moon. The computing software she created for the Apollo missions was to interrupt one task to take on a more important one. She also popularized the term "software engineering." [Source](https://www.smithsonianmag.com/smithsonian-institution/margaret-hamilton-led-nasa-software-team-landed-astronauts-moon-180971575/).

### Susan Wojcicki
Susan Wojcicki joined Google the year after it was founded and has been behind many of the search engine’s most defining features, including creating the first ever Google Doodle. She became head of YouTube last year, after it was bought by Google in 2006. [Source](https://www.theguardian.com/guardian-professional/women-leadership-blog/gallery/2015/jun/22/10-of-the-best-female-role-models-in-tech-in-pictures).

### Katherine Johnson
Katherine Johnson helped synch Project Apollo’s Lunar Module with the lunar-orbiting Command and Service Module. At age 97, President Barack Obama awarded her the Presidential Medal of Freedom. [Source](https://www.nasa.gov/content/katherine-johnson-biography).


## Step 1: Navigate to Python Sandbox

1. Go to [Python Sandbox](http://pythonsandbox.com/)
  	- If you have Python and a text edtor preinstalled on your computer, feel free to use that to run your code

## Step 2: Experiment with some basic Python

1. In the **Editor Window**, clear the line of code that was already there and insert the following:
```
# Hello, world!
```
2. Click the **Play** (▶️) button. What do you see in the **Output Window**?
3. You should see nothing! The first thing we did was create a **Comment**
  	- A **Comment** can only be seen by the developer and is used to help make the code easier for humans to read.
  	- It is also used to help test the code when we run into an error.
4. Now let's create a **variable**. The first variable we are going to create is a **string** which is used when we want to save text. Try typing the following code and hit **Play** (▶️).
	- You can use a single quote or double quote to create a string
```
firstProgram = "Hello, world!"
```
5. Although we created a **variable**, it is not appearing in the **Output Window** yet. There is one more thing we need to do. Add the following **print()** method to your program:
```
print("Hello, world!")
```
6. Try clicking **Play** (▶️) again. This time, **Hello, World!** should appear in the **Output Window**.
7. You can also print **Hello, world!** by using our **string** variable from earlier.
```
print(firstProgram)
```

## Step 3: Let's level up!

1. In addition to the **string** variable, we're going to learn about **ints** and **booleans** today. 
	- An **int** is short for integer, and it can be a whole number. 
	- A **boolean** is a binary operator that can return either **True** or **False**.
	- There are other common variables such as **floats** and **lists**, but we won't be using them in our workshop today.
2. Create an int that holds your age and call the **print()** method. After doing that, hit **Play** (▶️).
```
myAge = 20
print(myAge)
```
3. Now, create one more variable that holds your name. Once again, call the **print()** method and click **Play** (▶️).
```
myName = "Locksley"
print(myName)
```
4. Let's bring it all together! We're going to bring our **firstProgram**, **myAge**, and **myName** variable together into the following statement with a couple extra pieces. Replace all of your current code with the following snippet that we'll declare the sentence we want to print and **concatenate** the sentence together.
```
firstProgram = "Hello, world!"
intro = "My name is"
myName = "Locksley"
i = "I am"
myAge = 20
years = "years old"

# Save concatenated values in a string variable.
fullSentence = firstProgram + intro + myName + i + myAge + years
print(fullSentence)
```
5. This program won't work. You'll recieve an error message explaining that you cannot concatenate 'str' and 'int' objects. 

<img
  src="photos/concatenate.png"
  alt="Concatenate command line error"
  style="float: left; margin-right: 90px;"
/>

6. We'll change this by implementing the **str()** function to convert our string into an integer. We'll create a new variable to hold this **string**.
```
firstProgram = "Hello, world!"
intro = "My name is"
myName = "Locksley"
i = "I am"
myAge = 20
years = "years old"

strInt = str(myAge)

# Save concatenated values in a string variable.
fullSentence = firstProgram + intro + myName + i + strInt + years
print(fullSentence)
```
7. After running the program, you'll notice that all of the phrases are stuck together. 

<img
  src="photos/output1.png"
  alt="All of the phrases are stuck together"
  style="float: left; margin-right: 90px;"
/>
8. When concatenating strings, you need to manually add the spaces. Change the **fullSentance** to include the following spaces.
```
fullSentence = firstProgram + " " + intro + " " + myName + ". " + i + " " + strInt + " " + years + "."
```
<img
  src="photos/output2.png"
  alt="Phrases seperated with proper punctuation"
  style="float: left; margin-right: 90px;"
/>
  - We have also added some punctuation to this line!

## Step 4: Let's encode our quiz questions!

### These are the questions and answers we're going to use:

#### 1. What is your favorite color?
- Red
- Blue
- Green
- Purple

#### 2. What would you like to major in?
- Business
- Law
- Mathematics
- Computer Science
- Other

#### 3. What company would you most like to work for?
- NASA
- Google
- Start my own company

#### 4. What is the best invention?
- Space travel
- Smart phones
- The internet

### Implement the code

1. Replace all of the code in the **Editor Window** with the following snippet:
```
# Collect input for our questions.
answer = input( "What is your favorite color?\n(A) Red\n(B) Blue\n(C) Green\n(D) Purple" )

answer = input( "What would you like to major in?\n(A) Business\n(B) Law\n(C) Mathematics\n(D) Computer Science\n(E) Other")

answer = input( "3. What company would you most like to work for?\n(A) NASA\n(B) Google\n(C) Start my own company" )

answer = input( "What is the best invention?\n(A) Space travel\n(B) Smart phones\n(C) The internet" )
```
2. The **input()** function will trigger a pop up in our Python Sandbox where you can input your response. 
	- The new line character **\n** will space the answers across multiple lines.
3. Paste the code into Python Sandbox and click **Play** (▶️). A pop-up will appear that you can click through.

<img
  src="photos/popup1.png"
  alt="Pop up example"
  style="float: left; margin-right: 90px;"
/>

## Step 5: Add our counter variables
1. Right now, we can click through the pop-up, but no tallies are scored. We need to add some **counter** variables to store this information.
2. Below the code that is already there, input the following variables:
```
# Start all of the women in tech at 0.
reshma = 0
margaret = 0
susan = 0
katherine = 0
```

## Step 6: Add our logic
1. Now, we need to create logic that counts up the values when you select the corresponding answer. Copy and paste the following code for our first question: what is your favorite color?
	- We will use **if/elif/else** statements to run through the code
	- If an input is equal to a variable, it will trigger our counter
	- If the user incorrectly typed in something (or neglected to type in anything), it will choose a value to use.
```
# Answer counter for our first question: what is your favorite color?
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
```

2. Copy and paste the following code for our second question: what would you like to major in?
```
# Answer counter for our second question: what would you like to major in?
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
```  

3. Copy and paste the following code for our third question: what company would you most like to work for?
``` 
# Answer counter for our third question: hat company would you most like to work for?
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
``` 


4. Copy and paste the following code for our fourth question: what is the best invention?
``` 
# Answer counter for our fourth question: wWhat is the best invention?
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
``` 

## Step 7: Determine what score is the highest
1. Our final step is to add some logic to figure out which score is the highest. Use the following **if/elif/else** statements to determine which role model had the highest score and **print** that person to the **Output Window**.
``` 
# Determine which woman in tech had the highest score and print the results!
if (reshma > margaret and susan and katherine):
	print("Congratulations! You are most like Reshma!")
elif (margaret > reshma and susan and katherine):
  print("Congratulations! You are most like Margaret!")
elif (susan > margaret and susan and katherine):
  print("Congratulations! You are most like Susan!")
else:
  print("Congratulations! You are most like Katherine!")
``` 

## Step 8: Think critically
Congratualtions! You have built a working personality quiz! If you have extra time, start thinking about what you can add to make your personality quiz unique:
- Can I add more role models?
- Can I add more questions?
- If the player wanted to leave early or quit, how would that be done?

Adding these extra pieces will help you think about your work in new ways and display your own creativity.

## Next steps
If you are interested in learning more and growing your Python skills, check out these resources:
- [Learn Python basics with Wonder Woman](https://docs.microsoft.com/en-us/learn/paths/python-partnership/) - This was the inspiration for this workshop!
- [Take your first steps with Python](https://docs.microsoft.com/en-us/learn/paths/python-first-steps/)




