import math
from collections import Counter

def calculate_probabilities(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        total_characters = len(text)
        character_count = Counter(text)
        
        probabilities = {}
        for char, count in character_count.items():
            probabilities[char] = count / total_characters
        
        return probabilities

def count_entropy(character_probability):
    entropy = 0
    for char, probability in character_probability.items():
         entropy += probability*math.log2(probability)
    return entropy*-1
    
file_path = input("Enter the filename: ")
character_probability = calculate_probabilities(file_path)
print(character_probability)
entropy = count_entropy(character_probability)
print(entropy)



