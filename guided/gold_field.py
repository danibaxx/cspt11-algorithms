'''After escaping the pirate's cave without drowning, you stumble upon a
field where it's rumored a lot of gold can be found. You even have a map that
shows where all of the biggest hauls are located!Unfortunately, the sun is going down, so you don't have a ton of time to
search. You decide to take one quick pass through the field. You choose
only to move one of three ways:
-diagonally northeast
-diagonally southeast
-straight eastIf you start at the northwest corner of the field, how should you move to
maximize the gold you collect?Can you write a function that finds the best path through a square
field of any size?Ex.
                N
Input =    [[2, 4, 1],
        W   [0, 3, 2],    E
            [1, 2, 6]
            ]
                SOutput = '11 can be acquired by moving
['se', 'se']'(based on the Gold Mine Problem at
https://www.geeksforgeeks.org/gold-mine-problem/?ref=lbp)

# what is the input? 'matrix' -- list of lists [[2,4,1], [0,3,2], [1,2,6]]
'''
import itertools
import random
import time
from itertools import product

# go in the direction with the most gold --> greedy
# brute force: calculate every possible path and the amount of gold we can get and then we choose the one that gives us the max gold

def naive_scavenging(field):
    '''This solution generates all possible sequences of directions we may
    move. Then, it sums up the values, counts how many sequences produce the
    target sum, and calculates the odds that someone rolling `n` dice will
    end up with a sum equal to 3 times the number of dice.'''
    # generate all possible permutations of 'ne', 'e' or 'se' movements
    # that get a person across the field  
    #   
    # TODO - which function in Python's `itertools` module can we use
    # to generate all possible paths?    
    all_paths = list(itertools.product(['ne', 'e', 'se'], repeat=len(field) - 1))
    # TODO - evaluate each permutation to find the path
    # with the most gold along it
    max_gold = 0
    best_path = None   
    # iterate through all paths (loop with for)
    for path in all_paths:
        # where do we start?
        row = 0
        column = 0
        # 'walk along the path in each direction
        current_gold = field[row][column]
        for direction in path:
            if direction == 'ne':
                row = row - 1
                column = row + 1
            if direction == 'e':
                row = row + 1
                column = column + 1
            if direction == 'se':
                column = column + 1
        # check if out of bounds
        if column < 0 or column >= len(field) or row < 0 or row >= len(field):
            break
        # keeping track of the amount of gold we've collected on that path
        current_gold = current_gold + field[row][column]
        # figure out which one returns the maximum number of gold
        if current_gold > max_gold:
            max_gold = current_gold
            best_path = path
     
    return f'{max_gold} can be acquired by moving {best_path}'

    def dp_scavenging(field):
        '''This function utilizes dynamic programming to reduce the number of
        duplicate calculations that are performed (compared to the naive
        approach). After a coordinate is visited, we save both i) the max
        amount of gold that can be picked up from that coordinate and ii) the
        path you'd have to travel to pick up maximum gold from that point.    Subpaths on the eastern side of the field that we visited multiple times
        in the naive approach are only visited once using dynamic programming.
        '''    
        # cache of max mount of gold we can get starting at that position
        gold_cache = [[0] * len(field)] * len(field)

        # work backwards to fill in gold_cache
        for column in range(len(field) - 1, -1, -1):
            for row in range(len(field)):
                # gold_cache[row][column] (max amount of gold we can get) is equal to current amount of gold at that position in the field
                gold_at_location = field[row][column]
                # adn the max of the possible gold from paths we can take from that position
                ne_gold = 0
                se_gold = 0
                e_gold = 0
                # check if you can go directions
                if column + 1 < len(field) and row - 1 >= 0:
                    ne_gold = gold_cache[row - 1][column + 1]
                if column + 1 < len(field) and row + 1 < len(field):
                    se_gold = gold_cache[row + 1][column + 1]
                if column + 1 < len(field):
                    e_gold = gold_cache[row][column + 1]
                max_gold_along_paths = max(ne_gold, se_gold, e_gold)

                gold_cache[row][column] = gold_at_location + max_gold_along_paths
        max_gold = 0

        return f'{max_gold} gold can be acquired'

    def print_field(field, label):
        '''Helper function to display 2D fields
        with gold at different coordinates
        '''
    print(label)
    for row in field:
        output = ''
        for r in row:
            output += f' {r}'
        print(f'{output}\n')
    print()

# TESTS -
# Below are a series of tests that can be utilized to demonstrate the
# improvements achieved through dynamic programming. Timing is included
# to give students an idea of how poorly some approaches scale.
# However, efficiency should also be formalized using Big O notation.tiny_field = [[2, 4, 1],
              [0, 3, 2],
              [1, 2, 6]
              ]
print_field(tiny_field, "Tiny field")print(naive_scavenging(tiny_field))
#
# small_field = []
# size = 5
# for _ in range(size):
#     row = []
#     for _ in range(size):
#         row.append(round(random.random() * random.randint(1, 9), 3))
#     small_field.append(row)
# print_field(small_field, 'Small field')
#
# large_field = []
# size = 16
# for _ in range(size):
#     row = []
#     for _ in range(size):
#         row.append(round(random.random() * random.randint(1, 9), 3))
#     large_field.append(row
#                        )
# # print_field(large_field, 'Large field')
#
# # Test 1 - Naive
# print('Starting test 1, naive approach...\ncrossing small field...\n')
# start = time.time()
# print(f'{naive_scavenging(small_field)}')
# print(f'\nResult calculated in {time.time() - start:.5f} seconds')
# print('\n--------------------------------\n')
#
# # # Test 2 - Naive
# # print('Starting test 2, naive approach...\ncrossing large field...\n')
# # start = time.time()
# # print(f'\n{naive_scavenging(large_field)}')
# # print(f'\nResult calculated in {time.time() - start:.5f} seconds')
# # print('\n--------------------------------\n')
#
# # Test 3 - Dynamic Programming
# print('Starting test 3, dynamic programming...\ncrossing small field...\n')
# start = time.time()
# print(f'\n{dp_scavenging(small_field)}')
# print(f'\nResult calculated in {time.time()-start:.5f} seconds')
# print('\n--------------------------------\n')
#
# # Test 4 - Dynamic Programming
# print('Starting test 4, dynamic programming...\ncrossing large field...\n')
# start = time.time()
# print(f'\n{dp_scavenging(large_field)}')
# print(f'\nResult calculated in {time.time()-start:.5f} seconds')
# print('\n--------------------------------\n')