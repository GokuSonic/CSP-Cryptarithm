from itertools import permutations
import itertools
import random


DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

LETTERS= []

def wordToNum(word, charmap):
    power = 1
    result = 0
    for c in reversed(word):
        result += power * charmap[c]
        power *= 10
    return result



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
        print(left)
        print(left[i])
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
    #go through letters checking if their values are correct through ARC-3
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




















def subtraction_solve(equation):
    print(equation)
    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # split equation in left and right
    left, right = equation.lower().replace(' ', '').split('=')
    # split words in left part
    l1, l2 = left.split('-')
    # create list of used letters
    left = left.split('-')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters = list(letters)

    digits = range(10)
    graph = []
    charset = set(l1 + l2 + right)

    # build graph
    for vals in permutations(range(10), len(charset)):
        charmap = dict(zip(charset, vals))
        n1 = wordToNum(l1, charmap)
        n2 = wordToNum(l2, charmap)
        r = wordToNum(right, charmap)
        if (int(str(n1)[0]) != 0 and int(str(n2)[0])) != 0:
            if (int(n1) - int(n2) == int(r)) and (charmap[right[0]] != 0):
                # print("n1=", n1, "   n2=", n2, "     r= ", r)
                # print("n1 - n2 = r3??? ", (int(n1) - int(n2) == int(r)))
                answer = str(charmap)
                # print(str(answer[1:-1]).replace('\'', ''))
                graph.append(str(answer[1:-1]).replace('\'', ''))


       # calculate the number of carries
    print("Number of carries: ", len(l2))
    carry = []
    for x in range(0, (len(l2))):
        carry.append("C" + str(x))

    print('carries: ', carry)

    # what i want to do
    #    cba
    # -    ed
    # =   hgf
    # constaint [0] will have a-d =f
    # constraint[1] will have (carry.pop()) C0+a-d = f
    # constaint [2] will have carry.pop()  C1+b-e = g
    constraints = []

    # generate constraints
    # get all the carries
    for x in range(0, len(l1) - len(l2)):
        constraints.append('')
    while len(carry) > 0:
        constraints.append(str(carry.pop()))

    print(constraints)

    left_size = len(left)

    i = 0

    # get rows top to bottom and add them in
    while i != left_size:
        j = len(left[i])
        k = len(constraints)
        # move through the constraints left to right adding the logic
        while 0 != j:
            if constraints[k - 1].__contains__("C") and len(constraints[k - 1]) < 3:
                constraints[k - 1] = constraints[k - 1] + " + " + (left[i])[j - 1]
            else:
                if constraints[k - 1] == '':
                    constraints[k - 1] = (left[i])[j - 1]
                else:
                    constraints[k - 1] = constraints[k - 1] + " - " + (left[i])[j - 1]
            j -= 1
            k -= 1
        i += 1

    print(constraints)

    # orginal variables
    og_constraints = constraints.copy()
    og_letters = letters.copy()

    # ARC-3 only
    worked = False
    while (not worked):
        print("\nChoose \nA value for the following letters A1 B3....: ", )
        letters = og_letters.copy()
        inputs = ''
        while len(letters) > 0:
            if len(inputs) == 0:
                inputs = letters.pop()
            else:
                inputs = inputs + ", " + letters.pop()

        print(inputs)
        solutions = ""
        og_solutions = solutions = input("Enter solutions: ")
        print(solutions)

        constraints = og_constraints.copy()

        # check all diff
        AllDiff =True
        for num in DIGITS:
            if str(solutions).count(str(num)) > 1:
                AllDiff = False
                print("NOT ALL DIFFERENT")
                break

        zero_check = True
        if AllDiff:
            if int(solutions[solutions.find(l1[0:1])+1:solutions.find(l1[0:1])+2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", l1)
                zero_check = False
            if int(solutions[solutions.find(l2[0:1])+1:solutions.find(l2[0:1])+2]) ==0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", l2)
                zero_check = False
            if int(solutions[solutions.find(right[0:1])+1:solutions.find(right[0:1])+2]) ==0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", right)
                zero_check = False


            if zero_check:

                num_right = str(right)
                # replace all
                while len(solutions) != 0:
                    possible_solution = solutions[0:2]
                    solutions = solutions[3:]
                    # print("current sol ", possible_solution)
                    num_right = str(num_right).replace(possible_solution[:1], possible_solution[-1:])

                    for index, current_constraint in enumerate(constraints):
                        # print("looking at: ", current_constraint, "  looking for=", possible_solution[:1])
                        if current_constraint.__contains__(possible_solution[:1]):
                            constraints[index] = current_constraint.replace(possible_solution[:1], possible_solution[-1:])

                for x in constraints:
                    print("constraint: " , x)

                # arc 3 const checker
                con_index = 1
                print("len: ", len(constraints))
                print(num_right)

                # assume the user figured out all the math
                works = True
                while con_index != len(constraints) + 1:
                    print("\r\nindex: ", con_index)
                    string_cont = constraints[len(constraints) - con_index]

                    # checks if there is a carry
                    if len(str(string_cont)) > 1:
                        carry, compute = string_cont.split('+')
                        print("carry: ", carry)
                        print("Equation to check: ", compute, "  to sol : ", eval(compute))

                        # checks if it is negative then there needs to be a carry
                        if eval(compute) <= 0:
                            # updates formula to the left

                            # this adss 10 to the carry
                            print("Getting next constraint to satisfy first " + str(
                                constraints[len(constraints) - (con_index + 1)]))
                            updated_con = str(constraints[len(constraints) - (con_index + 1)])
                            if updated_con.__contains__('+'):
                                find_me = updated_con[updated_con.find('+') + 2:updated_con.find('+') + 3]
                                print("replace: ", find_me)
                                temp = int(find_me) - 1

                                constraints[len(constraints) - (con_index + 1)] = updated_con.replace(find_me, str(temp))
                                print("updated constraint: ", constraints[len(constraints) - (con_index + 1)])

                                right_answer = int(num_right[(len(num_right) - con_index):1 + (len(num_right) - con_index)])
                                left_answer = int(eval("" + str(10) + " + " + str(compute)))
                                print("orginal constraint with fwd checking: ", left_answer, " =? ", right_answer)

                                if left_answer == right_answer:
                                    print("          WORKS **** moving on")
                                else:
                                    print(str(og_constraints[len(og_constraints) - (con_index + 1)]),
                                          "Constraint Violated try again")
                                    works = False
                                    break
                            else:
                                print("No carry for ", updated_con)
                                temp = int(updated_con) - 1
                                print(temp)
                                constraints[len(constraints) - (con_index + 1)] = temp
                                left_answer = int(eval("" + str(10) + " + " + str(compute)))
                                right_answer = int(num_right[(len(num_right) - con_index):1 + (len(num_right) - con_index)])
                                print("orginal constraint with fwd checking: ", left_answer, " =? ", right_answer)

                                if left_answer == right_answer:
                                    print("          WORKS **** moving on")
                                else:
                                    print(str(og_constraints[len(og_constraints) - (con_index + 1)]),
                                          "Constraint Violated try again")
                                    works = False
                                    break

                        else:
                            left_answer = eval(compute)
                            right_answer = num_right[(len(num_right) - con_index):1 + (len(num_right) - con_index)]
                            print(left_answer, " =? ", right_answer)
                            if int(left_answer) == int(right_answer):
                                print("          WORKS **** moving on")
                            else:
                                print(str(og_constraints[len(og_constraints) - (con_index + 1)]),
                                      "Constraint Violated try again")
                                works = False
                                break
                    # nocarry
                    else:
                        right_answer = int(num_right[(len(num_right) - con_index):1 + (len(num_right) - con_index)])
                        print("one num: ", string_cont, " =? ", right_answer)
                        temp = int(string_cont)
                        if temp == right_answer:
                            print("          WORKS **** moving on")
                        else:
                            print(str(og_constraints[len(og_constraints) - (con_index + 1)]),
                                  "Constraint Violated try again-----")
                            works = False
                            break

                    con_index = con_index + 1

                if works:
                    break




    orign = equation
    print(og_solutions)
    og_solutions = og_solutions.replace(' ', '')

    # print final output
    while len(og_solutions) != 0:
        char = og_solutions[0:1]
        og_solutions = og_solutions[1:]
        value = og_solutions[0:1]
        og_solutions = og_solutions[1:]
        equation = equation.replace(char.capitalize(), value)

    # ask for user input
    letters_left = letters
    # output solution
    print("\n")

    for x in equation.split('-'):
        if x.__contains__('='):
            x, right = x.split('=')
            print('%s' % (x.rjust(9)))
            print('------------')
            print('=%s' % (right.rjust(7)))
        else:
            print('%s' % (x.rjust(9)))

    print("\n")
    for x in orign.split('-'):
        if x.__contains__('='):
            x, right = x.split('=')
            print('%s' % (x.rjust(9)))
            print('------------')
            print('=%s' % (right.rjust(7)))
        else:
            print('%s' % (x.rjust(9)))


















def mult_slove(equation):
    print("Multiplication: ", equation)
    #find top first then end the fill in middle for numbers
    #middle first

    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # split equation in left and right
    left, middle, right = equation.lower().replace(' ', '').split('=')


    # split words in left part
    l1, l2 = left.split('*')
    # create list of used letters
    left = left.split('*')
    letters = set(right)
    for word in left:
        for letter in word:
            letters.add(letter)
    letters_left = list(letters)

    # split words in middle part
    m1, m2 = middle.split('+')
    # create list of used letters
    mid = middle.split('+')
    for word in mid:
        for letter in word:
            letters.add(letter)
    letters_mid = list(letters)



    digits = range(10)
    graph = []
    charset = set(m1 + m2 + right + l1 + l2)


    # build graph
    for vals in permutations(range(10), len(charset)):
        charmap = dict(zip(charset, vals))
        n1 = wordToNum(l1, charmap)
        n2 = wordToNum(l2, charmap)
        r = wordToNum(right, charmap)
        if (int(str(n1)[0]) != 0 and int(str(n2)[0])) != 0:
            if (int(n1) * int(n2) == int(r)) and (charmap[right[0]] != 0):
                 #print("n1=", n1, "   n2=", n2, "     r= ", r)
                 #print("n1 - n2 = r3??? ", (int(n1) - int(n2) == int(r)))
                 answer = str(charmap)
                 #print(str(answer[1:-1]).replace('\'', ''))
                 graph.append(str(answer[1:-1]).replace('\'', ''))


    # calculate the number of carries
    print("Number of carries: ", )
    carry = []
    carry.append('')
    for x in range(0, (len(l1))):
        carry.append("C" + str(x))
    carry.append('')
    for x in range(len(l1), (len(l1)+len(l1))):
        carry.append("C" + str(x))

    constraints = []

    # generate constraints
    # get all the carries

    while len(carry) > 0:
        constraints.append(str(carry.pop()))

    print(constraints)

    left_size = len(left)

    i = 0

    j = len(left[i])
    k = len(constraints)
    next = 0

    #do top multiple
    while 0 != k:
        j = len(left[i])
        while 0 != j:
            if constraints[k - 1].__contains__("C") and len(constraints[k - 1]) < 3:
                constraints[k - 1] = constraints[k - 1] + " + " + (left[i])[j - 1]
            else:
                if constraints[k - 1] == '':
                    constraints[k - 1] = (left[i])[j - 1]
                else:
                    constraints[k - 1] = constraints[k - 1] + " * " + (left[i])[j - 1]
            j -= 1
            k -= 1
        k-=1


    i += 1
    j = len(left[i])
    k = len(constraints)

    while 0 !=j:
        multiplican = (left[i])[j - 1]
        l= len(left[i-1])
        while l !=0:
            constraints[k - 1] = constraints[k - 1] + " * " + (left[i])[j - 1]
            k-=1
            l-=1
        k-=1

        j-=1
    print(constraints)

    og_constraints = constraints.copy()
    og_letters = letters.copy()
    constraints_iterable = len(constraints)

    #first number
    how_many_numbers = len(left)
    iterable = len(m1)
    middle_index =0


    #loop

    works = False
    while not works:
        #get inputs
        print("\nChoose \nA value for the following letters A1 B3....: ", )
        letters = og_letters.copy()
        inputs = ''
        while len(letters) > 0:
            if len(inputs) == 0:
                inputs = letters.pop()
            else:
                inputs = inputs + ", " + letters.pop()

        print(inputs)
        solutions = ""
        og_solutions = solutions = input("Enter solutions: ")
        print(solutions)

        AllDiff = True
        for num in DIGITS:
            if str(solutions).count(str(num)) > 1:
                AllDiff = False
                print("NOT ALL DIFFERENT")
                break

        zero_check = True
        if AllDiff:
            if int(solutions[solutions.find(l1[0:1]) + 1:solutions.find(l1[0:1]) + 2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", l1)
                zero_check = False
            if int(solutions[solutions.find(l2[0:1]) + 1:solutions.find(l2[0:1]) + 2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", l2)
                zero_check = False
            if int(solutions[solutions.find(m1[0:1]) + 1:solutions.find(m1[0:1]) + 2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", m1)
                zero_check = False
            if int(solutions[solutions.find(m2[0:1]) + 1:solutions.find(m2[0:1]) + 2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", m2)
                zero_check = False
            if int(solutions[solutions.find(right[0:1]) + 1:solutions.find(right[0:1]) + 2]) == 0:
                print("FIRST DIGIT CAN NOT BE A 0 in: ", right)
                zero_check = False

            if zero_check:
                num_right = str(right)
                num_m1 = str(m1)
                num_m2 = str(m2)

                # replace all
                while len(solutions) != 0:
                    possible_solution = solutions[0:2]
                    solutions = solutions[3:]
                    # print("current sol ", possible_solution)
                    num_right = str(num_right).replace(possible_solution[:1], possible_solution[-1:])
                    num_m1 = str(num_m1).replace(possible_solution[:1], possible_solution[-1:])
                    num_m2 = str(num_m2).replace(possible_solution[:1], possible_solution[-1:])

                    for index, current_constraint in enumerate(constraints):
                        # print("looking at: ", current_constraint, "  looking for=", possible_solution[:1])
                        if current_constraint.__contains__(possible_solution[:1]):
                            constraints[index] = current_constraint.replace(possible_solution[:1],
                                                                            possible_solution[-1:])

                #constraints and solutions TO NUM
                num_mid = [num_m1, num_m2]
                print("constraints with numbers: " , constraints)

                #****************MULTIPLICATION ARC3
                con_index =1
                works =True
                while con_index != len(constraints) + 1:
                    #print("\r\ncon index: ", con_index)
                    #print("mid index: ", middle_index)
                    string_cont = constraints[len(constraints) - con_index]

                    iterable = len(num_mid[middle_index])
                    #print("iter: ", iterable)
                    right_check =str(num_mid[middle_index])
                    print(right_check)
                    string_index =1
                    #does the 2 MULTIPLICATIONS
                    while iterable !=0:
                        #print("iterable: " ,iterable)
                        string_cont = constraints[len(constraints) - con_index]
                        iterable -=1
                        # checks if there is a carry
                        if (string_cont).__contains__("C"):
                            carry, compute = string_cont.split('+')
                            print("carry: ", carry)
                            print("Equation to check: ", compute, "  to sol : ", eval(compute))
                        # nocarry
                        else:

                            right_answer=int(right_check[(len(right_check) - string_index):1 + (len(right_check) - string_index)])
                            #right_answer = int(num_right[(len(num_right) - con_index):1 + (len(num_right) - con_index)])
                            print("Evaluate: ", string_cont, " =? ", right_answer)
                            temp = eval(string_cont)
                            #print("eval = ", temp%10)
                            if temp%10 == right_answer:
                                carry = int(temp/10)
                                #checks for carry
                                if carry !=0:
                                    next_con = str(constraints[len(constraints) - (con_index+1)])
                                    constraints[len(constraints) - (con_index+1)] =  str(carry) + next_con[3:]
                                print("          WORKS **** moving on")
                            else:
                                print(str(og_constraints[len(og_constraints) - (con_index )]),"Constraint Violated try again-----")
                                works = False
                                break


                        con_index +=1
                        string_index +=1

                    if  not works:
                        break
                    else:
                        middle_index += 1

                print("---------Multiplication Constraints satisfied --------")

                #addition

                print("Number of carries: ", len(right) - 1)
                carry_add = []

                for x in range(0, (len(right) - 1)):
                    carry_add.append(str("C" + str(x)))

                print('carries for addition : ', carry_add)

                # what i want to do
                #    cba
                # +    ed
                # =   hgf
                # constaint [0] will have a+d =f
                # constraint[1] will have (carry.pop()) C0+b+e = g
                # constaint [2] will have carry.pop()  C1+c = h
                constraints_add = []

                # generate constraints
                # get all the carries
                while len(carry_add) > 0:
                    constraints_add.append(str(carry_add.pop()))

                constraints_add.append('')
                print(constraints_add)


                # add's to numbers as they increase in the MUL table
                for min_index, number in enumerate(mid):

                    zero_count =0
                    zeros = ''

                    while zero_count != min_index:
                        zeros += '0'
                        zero_count +=1

                    number = str(number) + str(zeros)
                    mid[min_index]= number


                mid_size = len(mid)
                i = 0

                # get rows top to bottom and add them in
                while i != mid_size:
                    j = len(mid[i])

                    k = len(constraints_add)
                    # move through the constraints left to right adding the logic
                    while 0 != j:
                        if constraints_add[k - 1] == '':
                            constraints_add[k - 1] = (mid[i])[j - 1]
                        else:
                            constraints_add[k - 1] = constraints_add[k - 1] + " + " + (mid[i])[j - 1]
                        k-=1
                        j-=1
                    i += 1


                print("Addition constraints: ", constraints_add)

                solutions = og_solutions
                # replace all
                while len(solutions) != 0:
                    possible_solution = solutions[0:2]
                    solutions = solutions[3:]
                    # print("current sol ", possible_solution)
                    num_right = str(num_right).replace(possible_solution[:1], possible_solution[-1:])
                    num_m1 = str(num_m1).replace(possible_solution[:1], possible_solution[-1:])
                    num_m2 = str(num_m2).replace(possible_solution[:1], possible_solution[-1:])

                    for index, current_constraint in enumerate(constraints_add):
                        # print("looking at: ", current_constraint, "  looking for=", possible_solution[:1])
                        if current_constraint.__contains__(possible_solution[:1]):
                            constraints_add[index] = current_constraint.replace(possible_solution[:1],
                                                                            possible_solution[-1:])

                # constraints and solutions TO NUM
                num_mid = [num_m1, num_m2]
                print("constraints with numbers: ", constraints_add)

                # arc 3 const checker
                con_index = 1
                carry_num = 0
                # assume the user figured out all the math


                works_add = True
                while con_index != len(constraints_add)+1:
                    string_cont = constraints_add[len(constraints_add) - con_index]
                    print("current equation: ", string_cont)
                    next_con = con_index+1


                    #if has carry
                    if string_cont.__contains__("C"):
                        #get rid of zero
                        string_cont = string_cont[4:]
                        print("check ", eval(string_cont), " =? ", num_right[len(num_right) - (con_index)])

                        #if carry
                        if eval(string_cont) >= 10:
                            #update const
                            next_str = constraints_add[len(constraints_add) - next_con]
                            next_str = str(next_str)
                            new_carry = str(int(eval(string_cont)/10))
                            print("carry FWD check constraint ", next_str, " : " , new_carry + " + " + next_str[next_str.find('+')+2:])
                            constraints_add[(len(constraints_add) - next_con)] = new_carry + " + " + next_str[next_str.find('+')+2:]

                            print("check ", eval(string_cont)%10, " =? ", num_right[len(num_right) - con_index])
                            if eval(string_cont)%10 == int(num_right[len(num_right) -con_index]):
                                print("          WORKS **** moving on")
                            else:
                                print(string_cont, "Constraint Violated try again-----")
                                works = False
                                break


                    #if no carry
                    else:
                        print("no carry")
                        print("   check ", eval(string_cont), " =? ", num_right[len(num_right) - (con_index)])
                        if eval(string_cont)>= 10:
                            # update const
                            next_str = constraints_add[len(constraints_add) - next_con]
                            next_str = str(next_str)
                            new_carry = str(int(eval(string_cont) / 10))
                            print("carry FWD check constraint ", next_str, " : " , new_carry + " + " + next_str[next_str.find('+')+2:])
                            constraints_add[(len(constraints_add) - next_con)] = new_carry + " + " + next_str[next_str.find('+')+2:]

                            if eval(string_cont)%10 == int(num_right[len(num_right) -con_index]):
                                print("          WORKS **** moving on")
                            else:
                                print(string_cont, "Constraint Violated try again-----")
                                works = False
                                break
                        else:
                            if eval(string_cont) == int(num_right[len(num_right) -con_index]):
                                print("          WORKS **** moving on")
                            else:
                                print(string_cont, "Constraint Violated try again-----")
                                works = False
                                break
                    carry_num +=1
                    con_index += 1



    orign = equation
    print(og_solutions)
    og_solutions = og_solutions.replace(' ', '')

    # print final output
    while len(og_solutions) != 0:
            char = og_solutions[0:1]
            og_solutions = og_solutions[1:]
            value = og_solutions[0:1]
            og_solutions = og_solutions[1:]
            equation = equation.replace(char.capitalize(), value)


    letters_left = letters
    # output solution
    print("\n")

    left, mid, right = equation.split('=')
    l1, l2 = left.split('*')
    m1, m2 = mid.split('+')
    print('%s' % (l1.rjust(9)))
    print('%s' % (l2.rjust(9)))
    print('------------')
    print('%s' % (m1.rjust(9)))
    print('%s' % (m2.rjust(8)))
    print('------------')
    print('%s' % (right.rjust(8)))


    print("\n")
    left, mid, right = orign.split('=')
    l1, l2 = left.split('*')
    m1, m2 = mid.split('+')
    print('%s' % (l1.rjust(9)))
    print('%s' % (l2.rjust(9)))
    print('------------')
    print('%s' % (m1.rjust(9)))
    print('%s' % (m2.rjust(8)))
    print('------------')
    print('%s' % (right.rjust(8)))

if __name__ == '__main__':
    choice =0
    while choice !=4:
        print("------------------------------------------------------\nChoose \n1)Addition \n2)Subtraction \n3)Multiplication\n4)Quit")
        choice = input("Enter Number: ")


        addition =["PUZZLES + TILES = PICTURE"
            , "I + BB = ILL"
            , "CROSS + ROADS = DANGER"
            , "COCA + COLA = OASIS"]

        multiply =['DID * TO = HDTE + ODOT = THOSE'
            ,'SEE * ME = HHOM + LTHL = KKOLM'
            ,'LET * IT = COOL + TALC = ISOSL'
            ,'ALL * OK = PALS + HLLO = PPASS']

        subtraction = ['ABCD - DCBA = BDAC'
                       ,'ONE - IS = OHH'
                       ,'TRAIL - ONE = TTLLP']

        if choice == '1' :
            addition_solve(random.choice(addition))
        if choice == '2' :
            subtraction_solve(random.choice(subtraction))
        if choice == '3':
            mult_slove(random.choice(multiply))
        if choice == '4':
            quit()

