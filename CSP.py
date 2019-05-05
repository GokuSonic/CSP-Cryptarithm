from itertools import permutations
from time import time
import random
import itertools


DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

LETTERS= []


def get_value(word, substitution):
    s = 0
    factor = 1
    for letter in reversed(word):
        s += factor * substitution[letter]
        factor *= 10
    return s

def heurstic(LETTERS,equation):
    print("finding the letters with the most dependencies")
    #loop counting most occurands then reording letters smallest to biggest



def addition_solve(equation):
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print("Addtion: ", equation)
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('+')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)


    digits = range(10)

    #generate graph
    graph = []
    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))

        if sum(get_value(word, sol) for word in left) == get_value(right, sol):
            answer = " = {} {}".format(get_value(right, sol), sol)
            junk, answer = answer.split('{')
            AllDiff = True
            for num in DIGITS:
                if str(answer[:-1]).replace('\'', '').count(str(num)) >1:
                    AllDiff = False
                    break
            if AllDiff:
                graph.append(str(answer[:-1]).replace('\'',''))

    print(letters)
    letters_left = letters


    #calculate the number of carries
    print("Number of carries: ",len(right)-1)
    carry = []
    for x in range(0,(len(right)-1)):
          carry.append("C"+str(x))

    print ('carries: ', carry)

    #what i want to do
    #    cba
    #+    ed
    #=   hgf
    #constaint [0] will have a+d =f
    #constraint[1] will have (carry.pop()) C0+b+e = g
    #constaint [2] will have carry.pop()  C1+c = h
    constraints = []

    #generate constraints
    #get all the carries
    while len(carry) > 0:
        constraints.append(str(carry.pop()))

    constraints.append('')
    print(constraints)

    left_size = len(left)

    i=0

    #get rows top to bottom and add them in
    while i != left_size:
        j= len(left[i])
        k = len(constraints)
        #move through the constraints left to right adding the logic
        while 0 != j:
            if constraints[k-1] == '':
                constraints[k-1] = (left[i])[j-1]
            else:
                constraints[k - 1] = constraints[k-1] + " + " + (left[i])[j - 1]
            j-=1
            k -= 1
        i+=1


    print(constraints)

    letters_left = letters
    orign = equation
    #go through letters checking if their values are correct
    while len(letters_left) !=0 :
        current_letter = letters_left.pop()
        found = False
        while not found :
            #check if satisfies domains and sums while ALLDIFF constraint is satisfied
            print("\nChoose \nA value for: ", str(current_letter).capitalize())
            choice = input("Enter Number: ")

            #forward checking and backwards checking
            found = False

            for x in graph:
                check = x[x.find(current_letter):x.find(current_letter)+4]
                if str(check).__contains__(choice):
                    found = True

            if not found:
                print("Choice does not work try again")
            else:
                equation =equation.replace(str(current_letter).capitalize(),choice )

    # output solution
    print("\n")

    for x in equation.split('+'):
        if x.__contains__('=') :
            x, right = x.split('=')
            print ('%s' % (x.rjust(9)))
            print('------------')
            print( '=%s' % (right.rjust(7)))
        else:
            print ('%s' % (x.rjust(9)))

    print("\n")
    for x in orign.split('+'):
        if x.__contains__('='):
            x, right = x.split('=')
            print('%s' % (x.rjust(9)))
            print('------------')
            print('=%s' % (right.rjust(7)))
        else:
            print('%s' % (x.rjust(9)))
    print("\n")

    return;





def subtration_solve(equation):
    print(equation)
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    left = left.split('-')
    # create list of used letters
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    graph = []

    for perm in itertools.permutations(digits, len(letters)):
        sol = dict(zip(letters, perm))
        first_word = word

        for word2 in left:
            if str(word2) != str(first_word):
                if ((get_value(word2, sol)) - get_value(first_word, sol)) == get_value(right, sol):
                    answer = " = {} (mapping: {})".format(get_value(right, sol), sol)
                    junk, answer = answer.split('{')
                    AllDiff = True
                    for num in DIGITS:
                        for num in DIGITS:
                            if str(answer[:-1]).replace('\'', '').count(str(num)) > 1:
                                AllDiff = False
                                break
                    if AllDiff:
                        graph.append(str(answer[:-1]).replace('\'', ''))

    print(letters)
    letters_left = letters


    #calculate the number of carries
    print("Number of carries: ",len(right)-1)
    carry = []
    for x in range(0,(len(right)-1)):
          carry.append("C"+str(x))

    print ('carries: ', carry)

    #what i want to do
    #    cba
    #+    ed
    #=   hgf
    #constaint [0] will have a+d =f
    #constraint[1] will have (carry.pop()) C0+b+e = g
    #constaint [2] will have carry.pop()  C1+c = h
    constraints = []

    #generate constraints
    #get all the carries
    while len(carry) > 0:
        constraints.append(str(carry.pop()))

    constraints.append('')
    print(constraints)

    left_size = len(left)

    i=0

    #get rows top to bottom and add them in
    while i != left_size:
        j= len(left[i])
        k = len(constraints)
        #move through the constraints left to right adding the logic
        while 0 != j:
            if constraints[k-1] == '':
                constraints[k-1] = (left[i])[j-1]
            else:
                constraints[k - 1] = constraints[k-1] + " + " + (left[i])[j - 1]
            j-=1
            k -= 1
        i+=1


    print(constraints)

    letters_left = letters
    orign = equation
    #go through letters checking if their values are correct
    while len(letters_left) !=0 :
        current_letter = letters_left.pop()
        found = False
        while not found :
            #check if satisfies domains and sums while ALLDIFF constraint is satisfied
            print("\nChoose \nA value for: ", str(current_letter).capitalize())
            choice = input("Enter Number: ")

            #forward checking and backwards checking
            found = False

            for x in graph:
                check = x[x.find(current_letter):x.find(current_letter)+4]
                if str(check).__contains__(choice):
                    found = True

            if not found:
                print("Choice does not work try again")
            else:
                equation =equation.replace(str(current_letter).capitalize(),choice )

    # output solution
    print("\n")

    for x in equation.split('-'):
        if x.__contains__('=') :
            x, right = x.split('=')
            print ('%s' % (x.rjust(9)))
            print('------------')
            print( '=%s' % (right.rjust(7)))
        else:
            print ('%s' % (x.rjust(9)))

    print("\n")
    for x in orign.split('-'):
        if x.__contains__('='):
            x, right = x.split('=')
            print('%s' % (x.rjust(9)))
            print('------------')
            print('=%s' % (right.rjust(7)))
        else:
            print('%s' % (x.rjust(9)))
    print("\n")

    return;


def mult_slove(equation):
    print("mult")



if __name__ == '__main__':
    choice =0
    while choice !=4:
        print("------------------------------------------------------\nChoose \n1)Addition \n2)Subtraction \n3)Multiplication\n4)Quit")
        choice = input("Enter Number: ")


        addition =["HERE + SHE = COMES"
            , "SEND + MORE = MONEY"
            , "I + BB = ILL"
            , "MEMO + FROM = HOMER"
            , "COCA + COLA = OASIS"
            , "GREEN + ORANGE = COLORS"
            , "NO + NO + GUN = HUNT"]

        multiply =['SEE * SO = EMOO + MESS = MIMEO'
            ,'DID * TO =HDTE + ODOT = THOSE'
            ,'GET * BY = BABE + GET = BEARE'
            ,'WHO * IS = HOBS + HAWI = MOSIS'
            ,'BAD * HI = BOAE + LDH = BOOZE'
            ,'SEE * ME = HHOM + LTHL = KKOLM'
            ,'DID * AD = EBOR + HEBE = AIRER'
            ,'LET * IT = COOL + TALC = ISOSL'
            ,'MAD * BE = MAD + RAE = AMID'
            ,'ALL * OK = PALS + HLLO = PPASS']

        subtraction = ['ABCD - DCBA = BDAC'
                       ,'ONE - IS = OHH'
                       ,'PAT -IT = PTO'
                       ,'PARK - AT = PAIL'
                       ,'TRAIL - ONE = TOON']

        if choice == '1' :
            addition_solve(random.choice(addition))
        if choice == '2' :
            subtration_solve(random.choice(subtraction))
        if choice == '3':
            mult_slove(random.choice(multiply))

