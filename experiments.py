from AVLTreeList import AVLTreeList
import random
import pandas as pd
from tqdm import tqdm

def test1(n):
    total = 0
    tree = AVLTreeList()
    for t in range(n):
        i = random.randrange(tree.length() + 1)
        total += tree.insert(i, str(i))
    return total

def test2(n):
    total = 0
    tree = AVLTreeList()
    for t in range(n // 2):
        i = random.randrange(tree.length() + 1)
        tree.insert(i, str(i))
    for t in range(n // 2):
        i = random.randrange(tree.length())
        total += tree.delete(i)
    return total 

def test3(n):
    total1 = 0
    tree = AVLTreeList()
    for t in range(n // 2):
        i = random.randrange(tree.length() + 1)
        total1 += tree.insert(i, str(i))
    total2 = 0
    for t in range(n // 4):
        i = random.randrange(tree.length() + 1)
        total2 += tree.insert(i, str(i))
        i = random.randrange(tree.length())
        total2 += tree.delete(i)

    return total1, total2

ns = [1500 * (2 ** i) for i in range(1, 11)]
df = pd.DataFrame(
    {
        '1': [test1(n) for n in tqdm(ns)],
        '2': [test2(n) for n in tqdm(ns)],
        '3': [test3(n) for n in tqdm(ns)]
    }
)
df['3a'], df['3b'] = df['3'].str
df.to_csv('ExperimentResults.csv')

print(df)
