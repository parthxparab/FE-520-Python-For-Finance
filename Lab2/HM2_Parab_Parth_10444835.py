# You can import packages from standard library if necessary
# Import them here
import string
import collections
from math import sqrt

# Q1
# A ball falls freely from a certain height. After each landing, it bounces back to 1/4 of
# its original height, then it falls again. Define a function(name: Ball_Drop) with two
# parameters, one is the original height, another one is the number of landing (Set this is
# a default value with 5). Return the meters of Total traveling distance when it bounces
# after the number of specific landing.
#
# Example:
# Input:
#   OriginalHeight = 100
#   NumLanding = 2
# Output:
#   Total traveling distance = 100+25+25+6.25=156.25

# Now you need to do any necessary changes to the following function.
# Note that parameter drop_num should have default value of 5


def Ball_Drop(Heights, drop_num=5):
    # modify this function
    far = []
    for i in range(drop_num+1):
        if (i == 0 or i == drop_num):
            far.append(Heights)
        else:
            far.append(Heights)
            far.append(Heights)
        Heights = Heights/4
    return sum(far)


# -------------------------------------
# Q2
# You are required to write a function (name: Get_Token) which can take a string as its
# argument, and return a dictionary. 1) This function will split this string by blank space
# into a list of sub-string, 2) then turn each element in this list into lower case without
# any punctuation (including special characters like ’\n’, ’\t’, etc.) and empty string. 3)
# if a token starts with or ends with a punctuation, remove the punctuation, e.g. ”world!”
# to ”world”, ”’hello’”to ”hello”. (Hint: you may need to use string.punctuation method
# by importing string). 4) After this, compute the frequency of each element in this list,
# and make a dictionary whose key is the element (sub-string) and value is the frequency.
# 5) Use string formatting to print out a sentence describing the most frequent word and
# its frequency in this string. 6) Return the dictionary you created in step 4.

def Get_Token(Given_str_1):
    # modify this function
    s = [i.lower() for i in Given_str_1.split()]
    exclude = set(string.punctuation)
    new = []
    for word in s:
        if '\n' in word:
            word.replace('\n', '')
        if '\t' in word:
            word.replace('\t', '')
        word = ''.join(ch for ch in word if ch not in exclude)
        new.append(word)

    frequency = {}
    for item in new:
        if (item in frequency):
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


# -------------------------------------
# Q3
# Define a function (name: Step_2_Fibo) that, given an integer X and a
# default-value parameter isIncrement = True, returns an integer that corresponds to the minimum
# number of steps required to change X to a Fibonacci number.
# In each step, you can either increment or decrement the current number depending on the parameter isIncrement
# i.e. you can change X to X+1 if isIncrement = True or X-1 if isIncrement = False.
# X will be between 0 and 1,000,000 inclusive.
#
# The Fibonacci sequence is defined as follows:
# F[0]=0
# F[1]=1
# for each i >= 2: F[i]=F[i-1]+F[i-2]
# The elements of the Fibonacci sequence are called Fibonacci numbers. The following
# sequence shows some elements at the head of this sequence:
# [0, 1, 1, 2, 3, 5, 8, 13, 21, · · · ]
#
# For example, for X=15 and isIncrement= False the function should return 2,
# because the closest Fibonacci number on the left is 13, thus 15−13 = 2;
# If X = 15 and isIncrement=True
# then the result should be 6 because 21 − 15 = 6;
# For X=1 or X=13 the function should return 0.

def Step_2_Fibo(Given_num, isIncrement=True):
    n = Given_num
    if sqrt(5*n**2+4) % 1 == 0 or sqrt(5*n**2-4) % 1 == 0:
        return 0
    c = 0
    while 1:
        c += 1
        if (isIncrement):
            if sqrt(5*(n+c)**2+4) % 1 == 0 or sqrt(5*(n+c)**2-4) % 1 == 0:
                return c
        else:
            if sqrt(5*(n-c)**2+4) % 1 == 0 or sqrt(5*(n-c)**2-4) % 1 == 0:
                return c


# -------------------------------------
# Q4
# Write a function (name: identi_Substring) that, given a string S,
# returns an integer that represents the numbers of ways in which we
# can select a non-empty substring of S where all of the characters of
# the substring are identical. Two substrings with the sameletters but
# different in locations are still considered different.For  example,
# the  string  ”zzzyz”  contains  8  such  substrings.
# Four  instances  of  ”z”,two of ”zz”, one of ”zzz” and one instance of ”y”.
# String ”k” contains only one suchsubstring:”k”.The length of S will be between 1 and 100, inclusive.
# You can assume that each character in S will be a lowercase letter (a-z)


def identi_Substring(x):
    test = [x[i: j] for i in range(len(x)) for j in range(i + 1, len(x) + 1)]
    s = []
    for i in test:
        if(len(set(i)) == 1):
            s.append(i)
    return(len(s))


# Test block
if __name__ == "__main__":
    print("\nQ1")
    ans_ls = []
    try:
        ans_ls.append(Ball_Drop(100, 2) == 156.25)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Ball_Drop(10, 1) == 12.5)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Ball_Drop(20) == 33.30078125)
    except:
        ans_ls.append(False)

    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')

    print("\nQ2")
    ans_ls = []

    Given_str_1 = '''
    "No need to light a Night light on a Light night,\t like tonight!"
    '''
    Given_str_2 = '''
    How any good cookies could a good cook cook, if a good cook could cook as many good cookies\n as a good cook could cook?
    '''
    try:
        res_dict_1 = Get_Token(Given_str_1)
        ans_ls.append(res_dict_1 == {'no': 1, 'need': 1, 'to': 1, 'light': 3,
                                     'a': 2, 'night': 2, 'on': 1, 'like': 1, 'tonight': 1})
    except:
        ans_ls.append(False)

    try:
        res_dict_2 = Get_Token(Given_str_2)
        ans_ls.append(res_dict_2 == {'how': 1, 'any': 1, 'good': 5, 'cookies': 2,
                                     'could': 3, 'a': 3, 'cook': 6, 'if': 1, 'as': 2, 'many': 1})
    except:
        ans_ls.append(False)

    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')

    print("\nQ3")
    ans_ls = []
    try:
        ans_ls.append(Step_2_Fibo(15, False) == 2)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Step_2_Fibo(15) == 6)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(Step_2_Fibo(21, True) == 0)
    except:
        ans_ls.append(False)
    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')

    print("\nQ4")
    ans_ls = []
    try:
        ans_ls.append(identi_Substring('zzzz') == 10)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(identi_Substring('zzzyz') == 8)
    except:
        ans_ls.append(False)

    try:
        ans_ls.append(identi_Substring('zzxyzzz') == 11)
    except:
        ans_ls.append(False)
    print(f'Correct/Total: {sum(ans_ls)}/{len(ans_ls)}')
