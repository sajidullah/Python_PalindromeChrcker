# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 17:04:35 2018

@author: sajid Ullah
"""

 
samplePhrase = "14541"

givenPhrase = input("\nPlease input a phrase:(Press ENTER to use the sample phrase) ")

if givenPhrase == "" or not givenPhrase.strip():
    print("\nThe sample phrase is: {0}".format(samplePhrase))
    phrase = samplePhrase
else:
    phrase = givenPhrase
    

string = phrase.lower()

if string == string[::-1]:
    print("\nWow!, The phrase is a Palindrome!")
else:
    print("\nSorry, The given phrase is not a Palindrome.")
