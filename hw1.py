#
# CS 196 Data Hackerspace
# Assignment 1: Data Parsing and NumPy
# Due September 24th, 2018
#

import json
import csv
import numpy as np
import requests

def histogram_times(filename):
    with open(filename) as file:
        csv_reader = csv.reader(file)
        file_data = list(csv_reader)
    hours = [0 for i in range (0, 24)]
    for event in file_data[1: ]:
        tempHour = event[1][0 : 2]
        if not tempHour.isdigit():
            continue
        tempHour = int(tempHour)
        hours[tempHour] = hours[tempHour] + 1

    return hours

print(histogram_times('airplane_crashes.csv'))

def weigh_pokemons(filename, weight):
    weight_match = []
    with open(filename) as file:
        poke = json.load(file)
        for count in poke["pokemon"]:
            if (float(count["weight"][:-2]) == weight):
                weight_match.append(count["name"])
    return weight_match
    
def single_type_candy_count(filename):
    candies = 0
    with open(filename) as file:
        poke = json.load(file)
        for count in poke["pokemon"]:
            if len(count["type"]) == 1 and "candy_count" in count:
                candies = candies + count["candy_count"]
    return candies

def reflections_and_projections(points):
    for count in points:
        points[count] = 2 - points[count]
    points = np.matmul([[0,-1],[1,0]], points)
    points = np.matmul([[1,3][3,9], points]) / 10
    return points
    
def normalize(image):
    flattened = a.flatten()
    max = np.amax(flattened)
    min = np.amin(flattened)
    for i in range(len(image)):
        for j in range(len(image)):
            j = (255/(max-min)) * (j - min)
    return image

def sigmoid_normalize(image):
    pass
