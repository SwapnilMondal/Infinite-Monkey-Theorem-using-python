## This is an experiment for the " INFINITE MONKEY THEOREM"

import string
import random
## to monitor the time taken by the program
import timeit
file = open('result.txt','w')

## declaring the string for the infinite monkey theorem problem
true_string = input('Enter a string: ')
length = len(true_string)
file.write("The string to be experimented on: " + true_string)

# a function to generate random strings

def generate():
# this function consistes of choice for random (imported) with method lowercase
# along with a white space  ## This runs for the range produced by the input string
    randchar = ''.join(random.choice(string.ascii_lowercase + ' ') for _ in range(length))
## returns the value to the variable in use
    return randchar

## function for defining score which will score the list's viability
def score(true_string, random_string):
## splitting the string into parts to compare
    true_string = true_string.split()
    random_string = random_string.split()
## for comparision we need sets of lists
## here we will run the comparision of randchar and true_string
## for any value a score is returned to the main program
    score = 0
    for i,j in zip(true_string, random_string):                 ## optional
        true_string = set(true_string)
        random_string = set(random_string)
        if(i == j):
## this compares if i is equal to j and returns value for score

            score = len(true_string & random_string)
            denominator = len(set(true_string))
            score = (score/denominator)*100

        return score

## this function is created to call the score and generate to evaluate score
def main():
    score_update = 0
    run = 0
## condition for the loop to stop
    while (score_update != 100):
## calls the function generate to a variable generator
        random_string = generate()

        print(random_string)

## to keep the score updated and return values
        score_update = score(true_string, random_string)

        print(score_update)

## for learning what value has the program scored yet
        run = run + 1

## loop for printing the value at every 1000 runs and printing the scores
        file.write('\n'+ random_string + ' ' + str(score_update)+ ' ' + str(run))

## Let us see the results ...
## timer to check the total time
start = timeit.default_timer()
main()
file.close()
stop = timeit.default_timer()
file = open('result.txt','a+')
file.write('\n'+'Start Time: ' + '00.0' + '\nStop Time: ' + str(stop))
file.close()
