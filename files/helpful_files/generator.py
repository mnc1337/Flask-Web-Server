# KEY GENERATOR

import random

def generate_key():
    key = ""
    symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for symbol in range(8):
        key += random.choice(symbols)

    return key

# print(generate_key())