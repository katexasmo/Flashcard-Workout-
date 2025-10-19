## Inspiration
- Back in high school, it felt as if we had much more free time to exercise — but now, a significant chunk of our time goes towards studying and sitting down in lectures. You definitely can't give up on your studies, and not necessarily forget about exercise either. In fact, exercise has been scientifically proven to improve studying by reducing stress and improving memory. (https://pmc.ncbi.nlm.nih.gov/articles/PMC6719811/)
- If that's the case, why not find a fun way to implement and incorporate both? 

## What it does
- Flashcard Workout! is a text-based interactive Python program where users are able to load their questions into the program, including potential correct and incorrect answers as well. 
- Through this, MCQ-styled questions and True or False questions are then placed in the following format:

```python
MCQ1: What's 2+2? #input A B C or D

a) 3
b) 4
c) 38
d) 22

MCQ2: What's a shiny red fruit?
a) Banana
b) Peach
c) Grapefruit 
d) None of the above
```

- If answered correctly, users can move on to the next question appropriately. 
- If answered incorrectly, users are told to do **10 jumping jacks.**
- The incorrectly answered question will be later asked again, and if still incorrect, the number increases to **20!**
- Luckily, the maximum amount of jumping jacks is capped at 50, so you shouldn't be too tired.

-# Not that you'll make that many mistakes for one question with 4 possible answers.... right.....


## How we built it
- A WiE x ESSS Hackthon of python and coffee.
- Zero use of AI! 

## Challenges we ran into
- Ensuring user honesty in doing the jumping jacks — we've integrated a system where they won't be able to see their overall mark until the very end.
- Understanding how the code comes together, debugging where issues occurred. 
- A wide variety of lists and classes that needed to stay organized. 
- Logic issues with the output depending on the answer.

## Accomplishments that we're proud of
- We implemented a text-to-file system where user input for questions and answers are placed into a file at the start. 
- One member of the team learnt Python today—through this Hackathon!
- Understanding the overall scope of the code and keeping track of logic breaks. 

## What we learned
- How to create and apply classes, and implement a text-to-file system. 
- Appropriate text formatting to keep track of all the code. 
- How to set up Live Share on VS Code. 

## What's next for Flashcard Workout?
- Having an Integrated Development Environment (IDE) to transition towards a mobile App
- Backend features for storage & databases 
- Installing UI/UX for optimal user experience. 

