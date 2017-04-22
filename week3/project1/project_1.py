#Project 1 - CS325
#Victor Ness, Philip Chang, Brandon Lo

import algo1, algo2, algo3, algo4
import random

input_size = 100
input_arr = []
for x in range(0, input_size):
    input_arr.append(random.randint(-50, 50))

algo1.mss()
algo2.process_input()
algo3.convertAnswer()
algo4.convertAnswer()