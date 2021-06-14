import os
import openai
key = open("C:/Users/paw472/OneDrive - AFRY/Documents/Projects/nlp_interact/Keys/key_gpt3.txt", "r")
openai.api_key = key.read()
#print(openai.Engine.retrieve("davinci"))