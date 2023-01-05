# username - sharonsorin
# id1      - 322756156
# name1    - Sharon Sorin
# id2      - 322885203
# name2    - Maya Iwanir

"""A class represnting a node in an AVL tree"""
import math
import random


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type value: str
    @param value: data of your node
    """

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = -1
        self.size = 0

    """returns the left child
    @rtype: AVLNode
    @returns: the left child of self, None if there is no left child
    """

    def getLeft(self):
        return self.left

    """returns the right child

    @rtype: AVLNode
    @returns: the right child of self, None if there is no right child
    """

    def getRight(self):
        return self.right

    """returns the parent 

    @rtype: AVLNode
    @returns: the parent of self, None if there is no parent
    """

    def getParent(self):
        return self.parent

    """return the value

    @rtype: str
    @returns: the value of self, None if the node is virtual
    """

    def getValue(self):
        return self.value

    """returns the height

    @rtype: int
    @returns: the height of self, -1 if the node is virtual
    """

    def getHeight(self):
        return self.height

    """returns the size (represents the size of the subtree rooted at self)

    @rtype: int
    @returns: the size of self, 0 if the node is virtual
    """

    def getSize(self):
        return self.size

    """sets left child

    @type node: AVLNode
    @param node: a node
    """

    def setLeft(self, node):
        self.left = node

    """sets right child

    @type node: AVLNode
    @param node: a node
    """

    def setRight(self, node):
        self.right = node

    """sets parent

    @type node: AVLNode
    @param node: a node
    """

    def setParent(self, node):
        self.parent = node

    """sets value

    @type value: str
    @param value: data
    """

    def setValue(self, value):
        self.value = value

    """sets the height of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    """sets the size of the node

    @type s: int
    @param s: the size
    """

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is not None

    """returns the balance factor of the node

    @rtype: int
    @returns: the height of left child of self, minus the height of right child of self"""

    def getBF(self):
        return self.left.height - self.right.height

    """
    Updates self size and height from its sons.
    """

    def updateSizeHeight(self):
        self.size = self.left.size + self.right.size + 1
        self.height = max(self.left.height, self.right.height) + 1


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.
    """

    def __init__(self):
        self.root = None
        self.size = 0

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.length() == 0

    """retrieves the value of the i-th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i-th item in the list
    """

    def retrieve(self, i):
        if i < 0 or i >= self.length():
            return None
        return self.retrieve_node_rec(self.root, i).getValue()

    """
    Retrieves the (i+1)-th node in the subtree rooted at node.
    
    @type i: int
    @param i: index of the node to retrieve (desired rank - 1)
    @type node: AVLNode
    @param node: the node from which we want to search
    @pre: 1 <= i <= node.size
    @rtype: AVLNode
    @returns: the (i+1)-th node in the subtree rooted at node
    """

    def retrieve_node_rec(self, node, i):
        if node.getLeft().getSize() > i:
            return self.retrieve_node_rec(node.getLeft(), i)

        elif node.getLeft().getSize() < i:
            return self.retrieve_node_rec(node.getRight(), i - node.getLeft().getSize() - 1)
        else:
            return node

    """performs a right rotation on the edge from A to B, where B is an AVL criminal, and A is B's left child.
    after the rotation, A and B have balance factor of 0.

    @type A: AVLNode
    @param A: a node with balance factor of 1 or 0. 
    @type B: AVLNode
    @param B: a node with balance factor of 2. 
    @pre: A is B's left child
    """

    def right_rotate(self, A, B):
        B.setLeft(A.getRight())
        B.getLeft().setParent(B)
        A.setRight(B)
        A.setParent(B.getParent())
        if A.getParent() is not None:
            if A.getParent().getRight() is B:
                A.getParent().setRight(A)
            else:
                A.getParent().setLeft(A)
        else:
            self.root = A
        B.setParent(A)
        B.updateSizeHeight()
        A.updateSizeHeight()
        if A.getParent() is not None:
            A.getParent().updateSizeHeight()

    """performs a left rotation on the edge from A to B, where B is an AVL criminal, and A is B's right child.
    after the rotation, A and B have balance factor of 0.

    @type A: AVLNode
    @param A: a node with balance factor of -1 or 0. 
    @type B: AVLNode
    @param B: a node with balance factor of -2. 
    @pre: A is B's right child.
    """

    def left_rotate(self, A, B):
        B.setRight(A.getLeft())
        B.getRight().setParent(B)
        A.setLeft(B)
        A.setParent(B.getParent())
        if A.getParent() is not None:
            if A.getParent().getRight() is B:
                A.getParent().setRight(A)
            else:
                A.getParent().setLeft(A)
        else:
            self.root = A
        B.setParent(A)
        B.updateSizeHeight()
        A.updateSizeHeight()
        if A.getParent() is not None:
            A.getParent().setHeight(max(A.getParent().getRight().getHeight(), A.getParent().getLeft().getHeight()) + 1)
            A.getParent().setSize(A.getParent().getLeft().getSize() + A.getParent().getRight().getSize() + 1)

    """If B is A's right child, and A is C's left child, performs a left-right-rotation:
    first performs a left rotation on the edge from A to B, where B is A's right child, 
    and then a right rotation on the edge from B to C, where B is now C's left child.
    If C has a balance factor of 2 and A has a balance factor of -1, after the rotation, 
    all three nodes have a BF of 0 or -1.

    @type A: AVLNode
    @param A: a node with balance factor of -1. 
    @type B: AVLNode
    @param B: a node. 
    @type C: AVLNoLde
    @param C: a node with balance factor of 2.
    @pre: B is A's right child, A is C's left child
    """

    def left_right_rotate(self, A, B, C):
        A.setRight(B.getLeft())
        A.getRight().setParent(A)
        B.setLeft(A)
        C.setLeft(B.getRight())
        C.getLeft().setParent(C)
        B.setRight(C)
        B.setParent(C.getParent())
        if B.getParent() is not None:
            if B.getParent().getRight() is C:
                B.getParent().setRight(B)
            else:
                B.getParent().setLeft(B)
        else:
            self.root = B
        A.setParent(B)
        C.setParent(B)
        A.updateSizeHeight()
        B.updateSizeHeight()
        C.updateSizeHeight()
        if B.getParent() is not None:
            B.getParent().updateSizeHeight()

    """If B is A's left child, and A is C's right child, performs a right-left-rotation:
    first performs a right rotation on the edge from A to B, where B is A's left child, 
    and then a left rotation on the edge from B to C, where B is now C's right child.
    If C has a balance factor of -2 and A has a balance factor of 1, after the rotation, 
    all three nodes have a BF of 0 or 1.
    
    @type A: AVLNode
    @param A: a node with balance factor of 1. 
    @type B: AVLNode
    @param B: a node. 
    @type C: AVLNode
    @param C: a node with balance factor of -2.
    @pre: B is A's left child and A is C's right child.
    """

    def right_left_rotate(self, A, B, C):
        A.setLeft(B.getRight())
        A.getLeft().setParent(A)
        B.setRight(A)
        C.setRight(B.getLeft())
        C.getRight().setParent(C)
        B.setLeft(C)
        B.setParent(C.getParent())
        if B.getParent() is not None:
            if B.getParent().getRight() is C:
                B.getParent().setRight(B)
            else:
                B.getParent().setLeft(B)
        else:
            self.root = B
        A.setParent(B)
        C.setParent(B)
        A.updateSizeHeight()
        B.updateSizeHeight()
        C.updateSizeHeight()
        if B.getParent() is not None:
            B.getParent().updateSizeHeight()

    """balances the tree - there are no AVL criminals afterwards.
    @type node: AVLNode
    @param node: the first candidate to be an AVL criminal
    @returns: the number of rebalancing operation due to AVL rebalancing"""

    def tree_balance(self, node):
        r_counter = 0
        while node is not None:
            node.updateSizeHeight()
            if -2 < node.getBF() < 2:
                node = node.getParent()
            else:
                if node.getBF() == -2:
                    son_bf = node.getRight().getBF()
                    if son_bf == -1 or son_bf == 0:
                        self.left_rotate(node.getRight(), node)
                        r_counter += 1
                    elif son_bf == 1:
                        self.right_left_rotate(node.getRight(), node.getRight().getLeft(), node)
                        r_counter += 2
                elif node.getBF() == 2:
                    son_bf = node.getLeft().getBF()
                    if son_bf == -1:
                        self.left_right_rotate(node.getLeft(), node.getLeft().getRight(), node)
                        r_counter += 2
                    elif son_bf == 1 or son_bf == 0:
                        self.right_rotate(node.getLeft(), node)
                        r_counter += 1
                node = node.getParent()
        return r_counter

    """inserts val at position i in the list

    @type i: int
    @pre: 0 <= i <= self.length()
    @param i: The intended index in the list to which we insert val
    @type val: str
    @param val: the value we inserts
    @rtype: list
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def insert(self, i, val):
        self.size += 1
        new_node = AVLNode(val)
        new_node.setLeft(AVLNode(None))
        new_node.setRight(AVLNode(None))
        new_node.getRight().setParent(new_node)
        new_node.getLeft().setParent(new_node)
        new_node.setHeight(0)
        new_node.setSize(1)

        if self.length() == 0:
            self.root = new_node
            return 0

        if self.length() == i:
            prev_node = self.retrieve_node_rec(self.root, self.length() - 1)
            prev_node.setRight(new_node)
        else:
            prev_node = self.retrieve_node_rec(self.root, i)
            if not prev_node.getLeft().isRealNode():
                prev_node.setLeft(new_node)
            else:
                prev_node = self.retrieve_node_rec(self.root, i - 1)
                prev_node.setRight(new_node)

        new_node.setParent(prev_node)

        return self.tree_balance(prev_node)

    """deletes the i-th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        if self.empty():
            return -1
        if i < 0 or i > self.length():
            return -1
        self.size -= 1
        if self.length() == 1:
            self.root = None
            return 0
        to_remove = self.retrieve_node_rec(self.root, i)
        if not to_remove.getLeft().isRealNode():  # not a leaf, but has no left node
            prev_node = to_remove.getParent()
            self.replace_tree(to_remove, to_remove.getRight())
        elif not to_remove.getRight().isRealNode():
            prev_node = to_remove.getParent()
            self.replace_tree(to_remove, to_remove.getLeft())
        else:
            successor_node = self.successor(to_remove)
            if successor_node is not None:  # to_remove is not the last node
                if successor_node is not to_remove.getRight():
                    prev_node = successor_node.getParent()
                    self.replace_tree(successor_node, successor_node.getRight())
                    successor_node.setRight(to_remove.getRight())
                    successor_node.getRight().setParent(successor_node)
                else:
                    prev_node = successor_node
                self.replace_tree(to_remove, successor_node)
                successor_node.setLeft(to_remove.getLeft())
                successor_node.getLeft().setParent(successor_node)
                successor_node.updateSizeHeight()
            else:  # to_remove is the last node
                prev_node = to_remove.getParent()
                prev_node.setRight(AVLNode(None))

        return self.tree_balance(prev_node)

    """replaces the subrtree rooted at node A by the subtree rooted at node B. 
    @type A: AVLNode
    @param A: the root of the subtree that has to be replaced.
    @type B: AVLNode
    @param B: the root of the subtree that will replace the subtree rooted at A. B can be a virtual node."""

    def replace_tree(self, A, B):
        if A.getParent() is None:
            self.root = B
        elif A == A.getParent().getLeft():
            A.getParent().setLeft(B)
        else:
            A.getParent().setRight(B)
        if B is not None:
            B.setParent(A.getParent())
        if A.getParent() is not None:
            A.getParent().updateSizeHeight()

    """returns the successor of a given node.
    @type node: AVLNode
    @param node: a node in the list self. The index of node in the list is 0 <= i < self.length .
    @rtype: AVLNode
    @returns: the node in index i+1, or None if i = self.length - 1"""

    def successor(self, node):
        if node.getRight().isRealNode():
            curr = node.getRight()
            while curr.getLeft().isRealNode():
                curr = curr.getLeft()
            return curr
        parent = node.getParent()
        while parent is not None and node == parent.getRight():
            node = parent
            parent = node.getParent()
        return parent

    """returns the value of the first item in the list

    @rtype: str
    @returns: the value of the first item, None if the list is empty
    """

    def first(self):
        if not self.empty():
            first_node = self.root
            while first_node.getLeft().isRealNode():
                first_node = first_node.getLeft()
            return first_node.getValue()
        return None

    """returns the value of the last item in the list

    @rtype: str
    @returns: the value of the last item, None if the list is empty
    """

    def last(self):
        if not self.empty():
            last_node = self.root
            while last_node.getRight().isRealNode():
                last_node = last_node.getRight()
            return last_node.getValue()
        return None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        values_list = []
        fill_array_from_tree(self.root, values_list)
        return values_list

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        if self.root is None:
            return 0
        return self.root.getSize()

    """sort the values of the list

    @rtype: AVLTreeList
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        values_list = []
        fill_array_from_tree(self.root, values_list)
        sorted_values = mergesort(values_list)
        return build_tree_from_list(sorted_values)

    """permute the info values of the list 

    @rtype: AVLTreeList
    @returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
    """

    def permutation(self):
        values = self.listToArray()
        arr_shuffle(values)
        return build_tree_from_list(values)

    """concatenates lst to self

    @type lst: AVLTreeList
    @param lst: a list to be concatenated after self
    @rtype: int
    @returns: the absolute value of the difference between the height of the AVL trees joined
    """

    def concat(self, lst):
        self.size += lst.length()
        if lst.empty():
            if self.empty():
                return 0
            return self.root.getHeight() + 1
        if self.empty():
            self.root = lst.root
            return lst.root.getHeight() + 1
        if lst.length() == 1:
            height = self.root.getHeight()
            self.insert(self.length(), lst.root.getValue())
            return height

        lst_height = lst.root.getHeight()
        height_diff = lst_height - self.root.getHeight()

        x = lst.root
        while x.getLeft().isRealNode():
            x = x.getLeft()
        lst.delete(0)

        if -2 < height_diff < 2:
            x.setLeft(self.root)
            self.root.setParent(x)
            x.setRight(lst.root)
            lst.root.setParent(x)
            x.setParent(None)
            x.updateSizeHeight()
            self.root = x
        elif height_diff >= 2:
            x.setLeft(self.root)
            b = lst.root
            while b.getHeight() > self.root.getHeight():
                b = b.getLeft()
            c = b.getParent()
            x.setRight(b)
            b.setParent(x)
            x.updateSizeHeight()
            c.setLeft(x)
            x.setParent(c)
            lst.tree_balance(c)
            self.root = lst.root
        else:
            x.setRight(lst.root)
            b = self.root
            while b.getHeight() > lst.root.getHeight():
                b = b.getRight()
            c = b.getParent()
            x.setLeft(b)
            b.setParent(x)
            x.updateSizeHeight()
            c.setRight(x)
            x.setParent(c)
            self.tree_balance(c)

        return abs(height_diff)

    """searches for a *value* in the list

    @type val: str
    @param val: a value to be searched
    @rtype: int
    @returns: the first index that contains val, -1 if not found.
    """

    def search(self, val):
        if self.empty():
            return -1
        counter = [-1]
        i = self.search_rec(self.root, val, counter)
        return i

    """
    Find the index of the first appearance of val in the subtree of root, and return this index + counter[0].
    counter[0] represents how many elements we searched until now
    
    @type root: AVLNode
    @param root: the root of the subtree we are searching
    @type val: str
    @param val: the value we search for
    @type counter: lst
    @param counter: a list with one item representing how many nodes we visited so far
    @pre: root.isRealNode()
    @pre: len(counter) == 1
    @rtype: int
    @returns: -1 if val is not in the subtree of root, otherwise counter[0]+(first index of val in subtree of root)
    """

    def search_rec(self, root, val, counter):
        if root.getLeft().isRealNode():
            i = self.search_rec(root.getLeft(), val, counter)
            if i != -1:
                return i

        counter[0] = counter[0] + 1

        if root.getValue() == val:
            return counter[0]
        else:
            if root.getRight().isRealNode():
                i = self.search_rec(root.getRight(), val, counter)
                if i != -1:
                    return i
        return -1

    """returns the root of the tree representing the list

    @rtype: AVLNode
    @returns: the root, None if the list is empty
    """

    def getRoot(self):
        return self.root


""" merging two lists into a sorted list. A and B must be sorted. 
@type A: list
@param A: a sorted list.
@type B: list
@param B: a sorted list.
@rtype: list
@returns: a sorted list (from smallest to largest) containing both A's and B's members."""


def merge(A, B):
    n = len(A)
    m = len(B)
    C = [None for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


""" recursive sorting of the list lst, using merge.
@type lst: list
@param lst: a list that will be sorted.
@rtype: list
@returns: a sorted list (from smallest to largest) containing the original members of lst."""


def mergesort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    else:  # two recursive calls, then merge
        return merge(mergesort(lst[0:n // 2]),
                     mergesort(lst[n // 2:n]))


""" shuffles an array of n elements. after the shuffling, arr's members will be in a random order.
@type arr: list
@param arr: a list that will be shuffled in place."""


def arr_shuffle(arr):
    n = len(arr)
    for i in range(n - 1):
        j = random.randrange(i, n)
        tmp = arr[i]  # exchange arr[i] and arr[j]
        arr[i] = arr[j]
        arr[j] = tmp


"""builds an AVL tree recursively from a given array, taking only the elements between the given indices (arr[i:j]).

@type arr: list
@param arr: array of values that will be inserted to an AVL tree.
@type i: int
@param i: the first index from which we take elements to the tree
@type j: int
@param j: one more than the last index until which we take element to the tree
@pre: i <= j
@rtype: AVLNode
@returns: a node which is the root of the tree
"""


def get_root_of_tree_from_list(arr, i, j):
    if j - i == 1:
        node = AVLNode(arr[i])
        node.setLeft(AVLNode(None))
        node.setRight(AVLNode(None))
        node.setHeight(0)
        node.setSize(1)
        return node
    if j - i == 0:
        return AVLNode(None)
    middle = (i + j) // 2
    root = AVLNode(arr[middle])
    root.setLeft(get_root_of_tree_from_list(arr, i, middle))  # builds an AVL tree from the left half
    root.setRight(get_root_of_tree_from_list(arr, middle + 1, j))  # builds an AVL tree from the right half
    root.getRight().setParent(root)
    root.getLeft().setParent(root)
    root.updateSizeHeight()
    return root


"""builds an AVL tree recursively from a given array.

@type arr: list
@param arr: array of values that will be inserted to an AVL tree.
@rtype: AVLTreeList
@returns: AVLTreeList representing the tree
"""


def build_tree_from_list(arr):
    tree = AVLTreeList()
    if len(arr) == 0:
        return tree
    tree.root = get_root_of_tree_from_list(arr, 0, len(arr))
    tree.size = len(arr)
    return tree


"""Appends the in-order traversal of the subtree of the given node to the given list

@type root: AVLNode
@param root: an AVLNode from which to start the traversal
@type values_list: list
@param values_list: the list to which we append the values
"""


def fill_array_from_tree(node, values_list):
    if node is None or not node.isRealNode():
        return
    if node.getLeft().isRealNode():
        fill_array_from_tree(node.getLeft(), values_list)

    values_list.append(node.getValue())

    if node.getRight().isRealNode():
        fill_array_from_tree(node.getRight(), values_list)
