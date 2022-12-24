from avl_template_new import AVLTreeList
import random
import pandas as pd

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
        total += tree.insert(i, str(i))
    for t in range(n // 2):
        i = random.randrange(tree.length())
        total += tree.delete(i)
    return total

def test3(n):
    total = 0
    tree = AVLTreeList()
    for t in range(n // 2):
        i = random.randrange(tree.length() + 1)
        total += tree.insert(i, str(i))
    for t in range(n // 4):
        i = random.randrange(tree.length() + 1)
        total += tree.insert(i, str(i))
        i = random.randrange(tree.length())
        total += tree.delete(i)

    return total

ns = [1500 * (2 ** i) for i in range(1, 11)]
df = pd.DataFrame(
    {
        '1': [test1(n) for n in ns],
        '2': [test2(n) for n in ns],
        '3': [test3(n) for n in ns]
    }
)
df.to_csv('ExperimentResults.csv')

print(df)
