sad = ["sad", "miserable", "depress", "upset", "unhappy", "sorrow", "deject", "regret", "down", "despair"]
anxious = ["anxious", "worry", "concern", "apprehen", "fear", "fret"]
blood = ["bleeding", "blood", "discharge", "red"]
irritated = ["irritated", "angry", "annoyed"]
tired = ["tired", "sleepy", "insomnia", "no sleep", "sleep"]
appetite = ["hungry", "food"]
negative = ["negative", "depressed", "hate"]
hopelessness = ["hopeless", "motivation", "unbother", "uncaring"]     ##we will use AI to add to this word bank 
diagnosed = "no" 
ppdcalender = 0


# --- Define your functions below! ---

# The chatbot introduces itself and gives the user instructions. 
def intro():
    print("Hi, my name is Abigail. Let's talk!")

# Choose a response based on the user's input.
def process_input(answer):
    # Define a list of possible ways the user might say hello.
    greetings = ["hi", "hello", "hey", "hey there", "sup"]
    # Define a list of possible ways the user might say bye.
    farewells = ["bye", "see ya", "goodbye", "quit", "exit", "bye bye"]

    if is_valid_input(answer, farewells):
        say_goodbye()
        return True # The user wants to exit!
    else:
        say_greeting()

# Display a greeting message to the user.
def say_greeting():
  print("Hey there!")

# Display a farewell message to the user.
def say_goodbye():
  print("See you next time!")

# Display a default message to the user.
#def say_default():
  #print("That's cool!")

# Check if user_input matches one of the elements
#  in valid_responses.
def is_valid_input(user_input, valid_responses):
  for item in valid_responses:
    if user_input == item:
      # If you find a matching response, the input is
      #  valid for this kind of response.
      return True
  # If you didn't find a matching response, after
  #  going through the entire list, the input
  #  isn't valid for this kind of response.
  return False

# --- Put your main program below! ---
def main():
    global diagnosed
    
    intro()
    def text():
        file = open("diary.txt", "w")
        file.truncate()
        diary = input("Please input your diary entry for today >>>")
        file.write(diary)
        file.close()
        

    def ppdchecker():
        ppd = [sad, irritated, tired, appetite, negative, hopelessness, anxious]


        def ppdcheck():
            questions = ["do you feel more sad then usual >>>", "do you feel irritated easily >>>", "are you experiencing insomnia >>>", "have you experienced loss of appitite >>>", "have you noticed a dip in your mood lately >>>"]
            yes = 0
            for i in range(0,5):
                question = input(questions[i])
                if question == "yes":
                    yes = yes+1
            if yes > 2:
                print("""You may have post partum depression, here are some links to read and raise awareness. We will moniter this and if the trend continues reccomend you to a doctor

                """)
                found = True
                return found
            else:
                print("After further questioning you do not seem at risk of post partum depression")
        ppdcount=0
        for i in range(len(ppd)):
            word1 = ppd[i]
            with open(r'diary.txt', 'r') as f:
                content = f.read()
                for word in word1:
                    occurences = content.count(word)
                    ppdcount = ppdcount + occurences
        if ppdcount > 5:
            print("""Some of the things you have written have indicated possible post partum depression.
        Please can you answer some more questions to further explore this""")
            return ppdcheck()
            
    add=0
    found = False
    go = "yes"
    text()
    while go != "no" and diagnosed == "no" :
        found = ppdchecker()
        if found == True:
            add = add+1
            found = False
        if add > 2:   ##for purpose of demo this is only twice normally it would be more 
            print("""We have noticed consistant symptoms with post partum depression, we advice you go talk to (here we would link to reccomended doctors

    """)
            diagnosed = input("Have you been to see a doctor about post partum depression? If yes we will stop checking for this issue >>>")            
            add = 0
    ##        ###add algorithm to find contact details for relevant doctors

        go = input("Would u like to add another entry? >>>")
        if go == "yes":
            text()

    if diagnosed != "no":
        print("You have seen a doctor about this issue so we will no longer check for it, this prototype focuses on diagnoses of post partum depression so cannot check for any other issues, thank you for testing! We will now monitor this issue and see if it improves in two months")
    else:
        print("Thank you for using our app, this prototype focuses on diagnoses of post partum depression so cannot check for any other issues, thank you for testing!")


    done = False # Use this to keep track of when the user wants to exit.
    
    while not done:
        answer = input("Goodbye :)")
        done = process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
