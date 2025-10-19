

import random


# Question super class
class Question:
    """
    Examples of each var
    question:
    - "What is 2 + 2?"
    correct:
    - "4"
    options:
    - [2, 3, 4, 5] --> 

    a) 2
    b) 3
    c) 4
    d) 5

    if they say the correct answer
    finalscore += 1
    """


    def __init__(self, question, correct):
        # The question posed to the user
        self.question = question
        # The correct answer
        self.correct = correct

    # Called when the game wants to ask the user the question.
    # Asks the question, then displays the options.
    def askQuestion(self, questionNumber): # when it's actually asking the user questions
        # asks the question to user, take in the input, & checks the answer correct/incorrect
        # Asks user question
        print(f"Q{questionNumber}: {self.question}")
        #if self.correct:
            # finalscore += 1

    def takeUserInput(self):
        userInput = input("Your answer here: ")
        return userInput
    

    def checkAnswer(self, userAnswer):
        # if ur answer is wrong:
        if userAnswer == self.correct: 
            print("Correct!")
            return True 
        else: 
            input(f"Incorrect. Your answer: {userAnswer}")
            print("Correct answer: {}".format(self.correct))
            return False
        


class QuestionMCQ(Question): #ABCD
    def __init__(self, question, correct, options):
        super().__init__(question, correct)
        self.options = options
        # Dictionary to convert numbers into letters
        self.alphabetOptions = {
        0 : "A",
        1 : "B",
        2 : "C",
        3 : "D",
        4 : "E",
        5 : "F",
        6 : "G",
        7 : "H",
        8 : "I",
        9 : "J"
        }

    # Randomizes options. Use before displayOptions
    def randomizeOptions(self):
        randomizedOptions = []
        while len(self.options) > 0: # loop until empty list
            randomIndex = random.randint(0, len(self.options) - 1) 
            randomizedOptions.append(self.options.pop(randomIndex))
        self.options = randomizedOptions # replace old list with a shuffled one

    def displayOptions(self):
        for optionNumber in range(0, len(self.options)):
            print(f"{self.alphabetOptions[optionNumber]}) {self.options[optionNumber]}")


class QuestionTF(Question): #T/F
    def __init__(self, question, correct): 
        super().__init__(question, correct)

    def displayOptions(self):
        print("T) TRUE")
        print("F) FALSE")
        

class QuestionFR(Question): # FOR REALLLLLL
    def __init__(self, question, correct):
        super().__init__(question, correct)

def writeFile(questions, fileName):
    file = open(fileName, "w")
    for question in questions:
        if isinstance(question, QuestionMCQ):
            file.write(f"1-{len(question.options)}\n")
        elif isinstance(question, QuestionTF):
            file.write("2\n") 
        else:
            continue
        file.write(f"{question.question}\n{question.correct}\n")
        if isinstance(question, QuestionMCQ):
            for option in question.options:
                file.write(f"{option}\n")
            # write question.options
            pass
    
# Reads a designated data file to load questions
def readFile(fileName):
    # Initialize needed variables
    file = open(fileName, "r")
    questionType = 0
    questionQuestion = ""
    questionCorrect = ""
    questionOptions = []
    questionList = []
    line = file.readline()
    # While the file's end isn't reached
    while line:
        # Check if the question type is MCQ
        questionType = line[0]
        if questionType == "1":
            for i in range(0, int(line[2])):
                questionOptions.append(0)
        
        # Store question's information
        line = file.readline().strip()
        questionQuestion = line
        line = file.readline().strip()
        questionCorrect = line
        if questionType == "1":
            for i in range(0, len(questionOptions)):
                questionOptions[i] = file.readline().strip()
            newQuestion = QuestionMCQ(questionQuestion, questionCorrect, questionOptions)
            questionList.append(newQuestion)
        if questionType == "2":
            newQuestion = QuestionTF(questionQuestion, questionCorrect)
            questionList.append(newQuestion)
        line = file.readline().strip()

    return questionList
        


def loadFileQuestions():
    pass

# Counts the amount of times a question is in a question list.
def searchQuestion(questionList, targetQuestion):
    questionCopies = 0
    for question in questionList:
        if question == targetQuestion:
            questionCopies += 1
    return questionCopies

# Counts the amount of unique questions inside a question list.
def countUniqueQuestions(questionList):
    uniqueQuestions = []
    for question in questionList:
        if question not in uniqueQuestions:
            uniqueQuestions.append(question)
    return len(uniqueQuestions)
    # checks for new questions to be added to question list

# Outputs directions to punish user
def punish (questionCopies):
    upperLimit = 50
    jumpingJackCount = 10 * questionCopies
    if jumpingJackCount > upperLimit:
        jumpingJackCount = upperLimit
    #-----------------------------------
    if questionCopies == 1:
        print(f"Incorrect, drop down and do {jumpingJackCount} jumping jacks!")
    elif questionCopies > 1:
        print(f"Still incorrect, do another {jumpingJackCount} jumping jacks.")
    else:
        print("Congrats! All correct.")

""" hypothetical alternative: 
punishments = [
    "Drop down and do 10", 
    "You suck haha +10",
    "Get moving and do 10 jacks of shame!"
    ]
print(random.choice(punishments))
"""


# Returns final score (0-100) based on percentage of questions scored correctly
def calcFinalScore(correctQuestionCount, totalQuestionCount):
    return round((correctQuestionCount/totalQuestionCount)*100)

def makerMode():
    questionType = 0
    questionQuestion = ""
    questionCorrect = ""
    questionOptions = []
    questionList = []
    while True:
        print("\nWhich question type would you like to create?")
        print("1) Multiple Choice Question\n2) True/False Question")
        userInput = input("Your choice: ").strip()
        if userInput == "1":
            questionType = "1"
        elif userInput == "2":
            questionType = "2"
        else:
            print("\nError: Unexpected input. Please enter 1 or 2.")
            continue

        print("What is the question? Ex: \"What is 2 + 2?\"")
        questionQuestion = input("The question: ")
        questionQuestion += " "

        if questionType == "1":
            questionCorrect = input("What is the correct answer to the question? ")
            questionOptions.append(questionCorrect)
            
        elif questionType == "2":
            userInput = input("Is the answer True or False? (T/F) ").lower()
            if userInput == "t":
                questionCorrect = "True"
            elif userInput == "f":
                questionCorrect = "False"
            else:
                print("\nError: Unexpected input. Please enter T or F.")
            continue
        if questionType == "1":
            while len(questionOptions) < 6:
                print("Please input other options to choose.")
                questionOptions.append(input("Option: "))
                if input("Would you like to stop adding options? (Y/N) (Max 6 options) ").lower() == "y":
                    break
            questionList.append(QuestionMCQ(questionQuestion, questionCorrect, questionOptions))
        elif questionType == "2":
            questionList.append(QuestionTF(questionQuestion, questionCorrect))
        questionType = 0
        questionQuestion = ""
        questionCorrect = ""
        questionOptions = []
        userInput = input("\nQuestion created! Would you like to make another? (Y/N) ").lower()
        if userInput == "n":
            break
    userInput = input("What name do you want to give the saved file? ")
    writeFile(questionList, f"{userInput}.txt")

    

# Python doesn't need main functions but TOO BAD I LIKE OOP CONVENTIONS
def main():
    listQuestions = []
    listIncorrectQuestions = []
    fileName = ""
    totalQuestionAmount = 0

    # Ask user "do you want to make questions or play a game from a question file?"
    print("What would you like to do?\n1) Create a set of questions\n2) Practice with a set of questions")
    userInput = input("Your response: ").strip()
    if userInput == "1":
        makerMode()
        return
    elif userInput == "2":
        pass
    else:
        print("Error: Unexpected input. Please enter 1 or 2.")
        return
    

    # If/else thing

    # Assuming game was selected
    """
    listQuestions = [QuestionMCQ("Who is Joe?", "JOEMAMA", ["JOEMAMA", "Who?", "No u"]), QuestionTF("Is true true", "True")]

    writeFile(listQuestions, "test.txt")

    listQuestions = readFile("test.txt")
    for question in listQuestions:
        print(question.question)
        print(question.correct)
        if isinstance(question, QuestionMCQ):
            print(question.options)

    """
    """
    newPlace = random.randint(0, len(listQuestions))
    listQuestions.append(0)
    for i in range(newPlace, (len(listQuestions) - 1)):
        temp = listQuestions[i]
        listQuestions[i] = listQuestions[i + 1]
    
    listQuestions[newPlace] = wrongQuestion

    loadFileQuestions()
    totalQuestionAmount = len(listQuestions)
    while True:
        pass
    """

    """
    test = QuestionMCQ("2 + 2?", "4", ["Joe", "Mama", "6969", "67", "4"])
    test2 = QuestionMCQ("3 + 3?", "6", ["Obama", "6"])
    test.askQuestion(1)
    print(" ")
    test.displayOptions()
    print (" ")
    test2.askQuestion(2)
    print(" ")
    test2.displayOptions()
    print(" ")
    """

main()
#calcFinalScore()

# ;1~Question~Correct~Wrong~Wrong~Wrong;1~Question~Correct~Wrong~Wrong~Wrong;2~Question~Answer
