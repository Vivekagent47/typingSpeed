from time import time

def typingErrors(prompt, input_prompt):
    input_words = input_prompt.split()
    words = prompt.split()
    errors = 0
    for i in range(len(input_words)):
        if i in (0, len(input_words)-1):
            if input_words[i] == words[i]:
                continue
            else:
                errors +=1
        else:
            if input_words[i] == words[i]:
                if (input_words[i+1] == words[i+1]) & (input_words[i-1] == words[i-1]):
                    continue
                else:
                    errors += 1
            else:
                errors += 1
    return errors

def typingSpeed(input_prompt, start_time, end_time):
    input_words = input_prompt.split()
    return len(input_words) / (end_time - start_time)

def timeTaken(start_time, end_time):
    time = end_time - start_time
    return time

if __name__ == '__main__':
    prompt = "Python is an interpreted, object-oriented, high-level programming language with dynamic semantics."
    print("Type the lines given below:- \n\n", prompt, "\n\n")

    input("Press ENTER when you are ready to type!")

    start_time = time()
    input_prompt = input()
    end_time = time()

    time = round(timeTaken(start_time, end_time), 2)
    speed = typingSpeed(input_prompt, start_time, end_time)
    errors = typingErrors(prompt, input_prompt)

    if errors == 0 and len(input_prompt) == len(prompt):
        print("Total Time Taken : ", time, "s")
        print("Your Average Typing Speed was : ", speed, "word/ minute")
    elif len(prompt) != len(input_prompt) and errors == 0:
        print("You have not typed all the words properly!")
    elif errors != 0:
        print("There is an error in your typing.")