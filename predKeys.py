import torch
import argparse
from fastai.text.all import *
from fastbook import load_learner
import trainModel

# Format the output
def format(a, b, length_a, length_b):
    str = a + " " * (length_a - len(a)) + "|" + b + " " * (length_b - len(b)) + "\n"
    str += "-" * length_a + "|" + "-" * length_b + "\n"
    return str

print("Loading model...")

# load the trained model
learner = load_learner('keyWordExtracter.pkl')

print("Model loaded." + "\n")
wLength = 0
while True:
    # take user input
    user_input = input("Enter a patent abstract: ")
    
    if user_input == "":
        break
    
    
    print("\n" + "Extracting keywords..." + "\n")

    # get the predicted labels
    input = 'ABSTRACT: ' + user_input
    predTensor, a, certaintyTensor = learner.predict(input)


    # get the length of the longest word
    if wLength == 0:
        for w in list(predTensor):
            if len(w) > wLength:
                wLength = len(w)


    cert_length = 4

    output = format("Keyword", " %", wLength, cert_length)
    for word, certainty in list(zip(predTensor, certaintyTensor)):
        # Print keyword if it is in the user input and the certainty is above 80%
        if float(certainty) > 0.8 and word in user_input.split():
            output += format(word, str(certainty), wLength, cert_length)
        
    print(output)
    print("\n")

