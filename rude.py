import time
import os
import random

def insult(num):
    adj = open("adj.txt", "r")
    ver = open("ver.txt", "r")
    nou = open("nou.txt", "r")
    x = adj.read().splitlines()
    y = ver.read().splitlines()
    z = nou.read().splitlines()
        
return ("you're a" + random.choice(x).lower() + " " + random.choice(y).lower() + " " + random.choice(z).lower() + ".")

