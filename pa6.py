# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:27:56 2024

@author: aorel
"""


def make_change(total, coins=[1, 5, 10, 25, 100]):
    '''Returns a llist of all distinct combination of coins for total'''
    def helper(num, i, combo, result):
        if num == 0:
            result.append(combo)
            return
        elif num < 0 or i == len(coins):
            return
        else:
            helper(num - coins[i], i, combo + [coins[i]], result)
            helper(num, i + 1, combo, result)

    result = []
    helper(total, 0, [], result)
    return result


def dict_filter(func, dictionary):
    '''Takes function and dict to produce a new dict'''
    new_dict = {}
    for key, value in dictionary.items():
        if func(key, value):
            new_dict[key] = value
    return new_dict


example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}


def checker(name, abbrev):
    '''Checks for I and l'''
    return abbrev[0] == "I" and name[1] == "l"


print(dict_filter(checker, example))


class KVTree:
    '''Representing countries, states, or cities'''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
        '''Adds child to node'''
        self.children.append(child)


def treemap(func, tree):
    tree.key, tree.value = func(tree.key, tree.value)
    for child in tree.children:
        treemap(func, child)


samplekv = KVTree("us", 4.6)
pa = KVTree("pa", 1.9)
samplekv.add_child(pa)
pa.add_child(KVTree("Pittsburgh", 0.3))
pa.add_child(KVTree("Philadelphia", 1.6))
il = KVTree("il", 2.7)
samplekv.add_child(il)
il.add_child(KVTree("Chicago", 2.7))

treemap(lambda x, y: (x.upper(), y * 1000000), samplekv)


class DTree:
    def __init__(self, variable, threshold, lessequal, greater, outcome):
        if (variable is None and threshold is None and lessequal is None and greater is None and outcome is not None) or \
           (variable is not None and threshold is not None and lessequal is not None and greater is not None and outcome is None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("Invalid arguments."
                             "Either all four of the first four "
                             "arguments should be not None, or the last argument "
                             "should be not None, but not both.")

    def tuple_atleast(self):
        '''Determines how many entries needed for tuple'''
        if self.variable is not None:
            return max(self.variable + 1, self.lessequal.tuple_atleast(), self.greater.tuple_atleast())
        else:
            # If this is a leaf node, return 0
            return 0

    def find_outcome(self, observations):
        '''takes tuple and navs through tree for outcome'''
        if self.variable is not None:
            if observations[self.variable] <= self.threshold:
                return self.lessequal.find_outcome(observations)
            else:
                return self.greater.find_outcome(observations)
        else:
            return self.outcome

    def no_repeats(self):
        '''analyzes tree to return True if no repeats'''
        def helper(node, seen):
            if node.variable is not None:
                if node.variable in seen:
                    return False
                else:
                    seen.add(node.variable)
                    return helper(node.lessequal, seen) and helper(node.greater, seen)
            else:
                return True

        return helper(self, set())
