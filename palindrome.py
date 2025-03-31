#For this assignment use the words.txt file.
#Read in all the words. Count how many are palindromes, or words that are spelled the same forwads and backwards.
#For example, wow is a paldindrome.
#A different file wile be used for grading.
#Correct answer for this file: 

import random

rndOutput = open("words.txt")
random.seed()

palindromes = 0

palin_list = palindromes("words.txt")
print(f"There are {len(palin_list)} palindrome words in the list")