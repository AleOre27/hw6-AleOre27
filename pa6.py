# -*- coding: utf-8 -*-
"""
Created on Thu May  2 16:27:56 2024

@author: aorel
"""

def make_change(total, coins=[1, 5, 10, 25, 100]):
    def helper(n, i, combo, result):
        if n == 0:
            result.append(combo)
            return
        elif n < 0 or i == len(coins):
            return
        else:
            helper(n - coins[i], i, combo + [coins[i]], result)
            helper(n, i + 1, combo, result)

    result = []
    helper(total, 0, [], result)
    return result

def dict_filter(func, dictionary):
    new_dict = {}
    for key, value in dictionary.items():
        if func(key, value):
            new_dict[key] = value
    return new_dict

example = {"Illinois": "IL", "Pennsylvania": "PA", "Indiana": "IN"}

def checker(name, abbrev):
    return abbrev[0] == "I" and name[1] == "l"

print(dict_filter(checker, example))

class KVTree:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, child):
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
    def __init__(self, variable=None, threshold=None, lessequal=None, greater=None, outcome=None):
        if (variable is None and threshold is None and lessequal is None and greater is None and outcome is None) or \
           (variable is not None and threshold is not None and lessequal is not None and greater is not None and outcome is None):
            self.variable = variable
            self.threshold = threshold
            self.lessequal = lessequal
            self.greater = greater
            self.outcome = outcome
        else:
            raise ValueError("Invalid arguments")

    def tuple_atleast(self):
        if self.outcome is not None:
            return 0
        else:
            return max(self.variable + 1, self.lessequal.tuple_atleast(), self.greater.tuple_atleast())

    def find_outcome(self, observations):
        if self.outcome is not None:
            return self.outcome
        elif observations[self.variable] <= self.threshold:
            return self.lessequal.find_outcome(observations)
        else:
            return self.greater.find_outcome(observations)

    def no_repeats(self):
        def helper(node, seen):
            if node.outcome is not None:
                return True
            if node.variable in seen:
                return False
            seen.add(node.variable)
            return helper(node.lessequal, seen.copy()) and helper(node.greater, seen.copy())

        return helper(self, set())