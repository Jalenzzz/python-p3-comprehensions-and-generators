#!/usr/bin/env python3

def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

def make_exclamation(sentence_list):
    return [sentence + '!' for sentence in sentence_list]

print(return_evens([1,2,3,4,5,6])) #returns the even numbers in the list
print(make_exclamation(["Hello", "Ugali is life", "Testing the function"])) #adds exclamations to the end of the examples
