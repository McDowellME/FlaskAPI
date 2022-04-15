#!/usr/bin/env python3

import requests
from pprint import pprint

URL = "http://127.0.0.1:2224/spaceballs-api"

resp = requests.get(URL).json()

question = resp[0]["question"]
gif = resp[0]["gif"]
correct_answer = resp[0]["correct_answer"]
incorrect_answers = resp[0]["incorrect_answers"]
all_answers = resp[0]["all_answers"]

print(f"Question: {question}")
print(f"gif: {gif}")
print(f"Correct Answer: {correct_answer}")
i = 1 
for inc in incorrect_answers:       
    print(f"Incorrect Answer {i}: {inc}")
    i += 1
print(f"All Answers: {all_answers}")