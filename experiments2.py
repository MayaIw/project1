from AVLTreeList import AVLTreeList
import random
import pandas as pd
import time
from tqdm import tqdm

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, i, value):
        if self.head is None:
            self.head = Node(value)
            return
        if i == 0:
            self.head = Node(value, next=self.head)
            self.head.next.prev = self.head
        else:
            curr = self.head
            for t in range(i - 1):
                curr = curr.next
            new_node = Node(value, next=curr.next, prev=curr)
            if curr.next is not None:
                curr.next.prev = new_node
            curr.next = new_node

def test1(n, lst):
    total = 0
    for t in range(n):
        start = time.time()
        lst.insert(0, str(t))
        total += time.time() - start
    return total/n

def test2(n, lst):
    total = 0
    for t in range(n):
        i = random.randrange(0, t + 1)
        start = time.time()
        lst.insert(i, str(t))
        total += time.time() - start
    return total/n

def test3(n, lst):
    total = 0
    for t in range(n):
        start = time.time()
        lst.insert(t, str(t))
        total += time.time() - start
    return total/n

ns = [1500 * i for i in range(1, 11)]

for i, func in enumerate([test1, test2, test3]):
    df = pd.DataFrame({
        'AVL': [func(n, AVLTreeList()) for n in tqdm(ns)],
        'LinkedList': [func(n, LinkedList()) for n in tqdm(ns)],
        'Array': [func(n, []) for n in tqdm(ns)]
    })
    df.to_csv(f'Experiment2_{i}.csv')

    print(df)


