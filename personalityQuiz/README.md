<img
  src="photos/Women in Tech.png"
  alt="Women in Tech: Reshma Saujani, Margaret Hamilton, Susan Wojcicki, and Katherine Johnson"
  style="float: left; margin-right: 90px;"
/>

# Learn Python with the Women in Tech Personality Quiz

## Created by Locksley Kolakowski

| **Project Goal**            | **Build a Women in Tech Personality Quiz** |
|-------------------------|----------------------------------------|
| **What you'll learn**       | Learn the basics of Python             |
| **Tools you'll need**       | [Python Sandbox](http://pythonsandbox.com/) |
| **Time needed to complete** | <1 hour                                |
| **Finished Solution**       |  |

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
  - If you have Python preinstalled on your computer, feel free to use a text editor to run your code

## Step 2: Experiment with some basic Python

1. In the **Editor Window**, type the following code
```
# Hello, world!
```
2. Click the **Play**(▶️) button. What do you see in the **Output Window**?
3. You should see nothing! The first thing we did was create a **Comment**
  - A **Comment** can only be seen by the developer and is used to help make the code easier for humans to read.
  - It is also used to help test the code when we run into an error.
4. Now let's create a **variable**. The first variable we are going to create is a **string** which is used when we want to save text. Try typing the following code and hit **Play**.
```
firstProgram = "Hello, world!"
```
5. Although we created a **variable**, it is not appearing in the **Output Window** yet. There is one more thing we need to do. Add the following code below your variable:
```
print("Hello, world!")
```
6. Try clicking **Play** again. This time, **Hello, World!** should appear in the **Output Window**.
7. You can also print **Hello, world!** by using our **string** variable from earlier.
```
print(firstProgram)
```

## Step 3: Let's level up!

1. In addition to the **string** variable, we're going to learn about an **int**. An **int** is short for integer, and it can be a whole number. 
2. Create an int that holds your age.
```
myAge = 20
```
3. Now, create one more variable that holds your name.
```
myName = "Locksley"
```
4. Let's bring it all together! We're going to bring our **firstProgram**, **myAge**, and **myName** variable together into the following statement with a couple extra pieces. Replace all of your current code with the following snippet:
```
firstProgram = "Hello, world!"
intro = "My name is"
myName = "Locksley"
i = "I am"
myAge = 20
years = "years old"

fullsentence = firstProgram + intro + myName + i + strInt + years
print(fullsentence)
```
5. This program won't work. You'll recieve an error message explaining that you cannot concatenate 'str' and 'int' objects. We'll change this by implementing the **str()** function to convert our string into an integer. We'll create a new variable to hold this **string**.
```
firstProgram = "Hello, world!"
intro = "My name is"
myName = "Locksley"
i = "I am"
myAge = 20
years = "years old"

strInt = str(myAge)

fullSentence = firstProgram + intro + myName + i + strInt + years
print(fullsentence)
```
6. After running the program, you'll notice that all of the phrases are stuck together. When concatenating strings, you need to manually add the spaces. Change the **fullSentance** to include the following spaces.
```
fullSentence = firstProgram + " " + intro + " " + myName + ". " + i + " " + strInt + " " + years + "."
```
  - We have also added some punctuation to this line!

## Step 4: Let's encode our quiz questions!

### These are the questions we're going to use:

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
question = input( "What is your favorite color?\n(A) Red\n(B) Blue\n(C) Green\n(D) Purple" )

question = input( "What would you like to major in?\n(A) Business\n(B) Law\n(C) Mathematics\n(D) Computer Science\n(E) Other")

question = input( "3. What company would you most like to work for?\n(A) NASA\n(B) Google\n(C) Start my own company" )

question = input( "What is the best invention?\n(A) Space travel\n(B) Smart phones\n(C) The internet" )
```
2. The **input()** function will trigger a pop up in our Python Sandbox where you can input your response. The new line character **\n** will space the answers across multiple lines.
3. Paste the code into Python Sandbox and click **Play**. A pop-up will appear that you can click through.

## Step 5: Add our counter variables
1. Right now, we can click through the pop-up, but no tallies are scored. We need to add some **counter** variables to store this information.
2. At the top of the **Editor Window**, input the following code:
```
reshma = 0
maragaret = 0
susan = 0
katherine = 0
```







