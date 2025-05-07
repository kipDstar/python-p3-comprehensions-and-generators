#!/usr/bin/env python3

def return_evens(num_list):
    # Corrected the logic to return even numbers instead of boolean values
    evens_list = [num for num in num_list if num % 2 == 0]
    return evens_list

def make_exclamation(sentence_list):
    exclamation_list = [sentence + "!" for sentence in sentence_list]
    return exclamation_list