# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info
# todo: return the part above to the conventions of the beginning and fill it

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
        self.size = -1

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

    """sets the balance factor of the node

    @type h: int
    @param h: the height
    """

    def setHeight(self, h):
        self.height = h

    def setSize(self, s):
        self.size = s

    """returns whether self is not a virtual node 

    @rtype: bool
    @returns: False if self is a virtual node, True otherwise.
    """

    def isRealNode(self):
        return self.value is not None

    def getBF(self):
        return self.left.height - self.right.height


"""
A class implementing the ADT list, using an AVL tree.
"""


class AVLTreeList(object):
    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.size = 0
        self.root = None

    # add your fields here

    """returns whether the list is empty

    @rtype: bool
    @returns: True if the list is empty, False otherwise
    """

    def empty(self):
        return self.size == 0

    """retrieves the value of the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: index in the list
    @rtype: str
    @returns: the the value of the i'th item in the list
    """

    def retrieve(self, i):
        return self.retrieve_node_rec(self.root, i).value

    def retrieve_node_rec(self, node, i):
        if node.left.size > i:
            return self.retrieve_node_rec(node.left, i)

        elif node.left.size < i:
            return self.retrieve_node_rec(node.right, i - node.left.size)
        else:
            return node

    """right rotation
    A is B's left child
    before rotation: B.BF = +2, A.BF = +1 or 0
    after rotation: B.BF = 0, A.BF = 0"""

    def right_rotate(self, A, B):
        B.setLeft(A.right)
        B.left.setParent(B)
        A.setRight(B)
        A.setParent(B.parent)
        if A.parent.right is B:
            A.parent.setRight(A)
        else:
            A.parent.setLeft(A)
        B.setParent(A)
        B.height -= 2
        A.parent.height = max(A.parent.right.height, A.parent.left.height) + 1
        s = B.size
        B.size = A.size - 1
        A.size = s

    """left rotation
    A is B's right child
    before rotation: B.BF = -2, A.BF = -1 or 0
    after rotation: B.BF = 0, A.BF = 0"""

    def left_rotate(self, A, B):
        B.setRight(A.left)
        B.right.setParent(B)
        A.setLeft(B)
        A.setParent(B.parent)
        if A.parent.right is B:
            A.parent.setRight(A)
        else:
            A.parent.setLeft(A)
        B.setParent(A)
        B.height -= 2
        A.parent.height = max(A.parent.right.height, A.parent.left.height) + 1
        s = B.size
        B.size = A.size - 1
        A.size = s

    """left then right rotation
    A is C's left child
    B is A's right child
    before rotation: C.BF = +2, A.BF = -1 
    after rotation: C.BF = 0, A.BF = 0"""

    def left_right_rotate(self, A, B, C):
        A.setRight(B.left)
        A.right.setParent(A)
        B.setLeft(A)
        C.setLeft(B.right)
        C.left.setParent(C)
        B.setParent(C.parent)
        if C.parent.right is C:
            C.parent.setRight(B)
        else:
            C.parent.setLeft(B)
        A.setParent(B)
        C.setParent(B)
        A.height = B.height
        B.height = C.height - 1
        C.height -= 2
        C.parent.height = max(C.parent.right.height, C.parent.left.height) + 1
        B.size = C.size
        A.size = A.left.size + B.right.size + 1
        C.size = C.right.size + C.left.size + 1

    """right then left rotation
       A is C's right child
       B is A's left child
       before rotation: C.BF = -2, A.BF = +1 
       after rotation: C.BF = 0, A.BF = 0"""

    def right_left_rotate(self, A, B, C):
        A.left = B.right
        A.left.setParent(A)
        B.right = A
        C.right = B.left
        C.right.setParent(C)
        B.setParent(C.parent)
        if C.parent.right is C:
            C.parent.setRight(B)
        else:
            C.parent.setLeft(B)
        A.setParent(B)
        C.setParent(B)
        A.height = B.height
        B.height = C.height - 1
        C.height -= 2
        C.parent.height = max(C.parent.right.height, C.parent.left.height) + 1
        B.size = C.size
        A.size = A.left.size + B.right.size + 1
        C.size = C.right.size + C.left.size + 1

    """balances the tree, and counts the total number of rotations"""

    def tree_balance(self, node, r_counter):
        while node is not None:
            prev_height = node.getHeight()
            node.setHeight(min(node.left.getHeight(), node.right.getHeight()) + 1)
            if -2 < node.getBF() < 2:
                if node.getHeight() == prev_height:
                    return r_counter
                else:
                    node = node.getParent()
            else:
                if node.getBF() == -2:
                    son_bf = node.getRight().getBF()
                    if son_bf == -1 or son_bf == 0:
                        self.left_rotate(node.getRight(), node)
                        r_counter += 1
                    elif son_bf == 1:
                        self.right_left_rotate(node.getRight(), node.getRight().getLeft(), node)
                        r_counter += 1
                elif node.getBF() == 2:
                    son_bf = node.getLeft().getBF()
                    if son_bf == -1:
                        self.left_right_rotate(node.getLeft(), node.getLeft().getRight(), node)
                        r_counter += 1
                    elif son_bf == 1 or son_bf == 0:
                        self.right_rotate(node.getLeft(), node)
                        r_counter += 1
                    node = node.getParent()

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
        r_counter = 0

        new_node = AVLNode(val)
        new_node.setSize(1)

        if self.size == 0:
            new_node.setLeft(AVLNode(None))
            new_node.setRight(AVLNode(None))
            new_node.setHeight(0)
            self.root = new_node
            return r_counter

        if self.size == i:
            prev_node = self.retrieve_node_rec(self.root, self.size - 1)
            prev_node.right = new_node
        else:
            prev_node = self.retrieve_node_rec(self.root, i)
            if not prev_node.left.isRealNode():
                prev_node.left = new_node
            else:
                prev_node = self.retrieve_node_rec(self.root, i - 1)
                prev_node.right = new_node

        new_node.setParent(prev_node)

        return self.tree_balance(prev_node, r_counter)
        # while prev_node is not None:
        #     prev_height = prev_node.getHeight()
        #     prev_node.setHeight(min(prev_node.left.getHeight(), prev_node.right.getHeight()) + 1)
        #     if -2 < prev_node.getBF() < 2:
        #         if prev_node.getHeight() == prev_height:
        #             return r_counter
        #         else:
        #             prev_node = prev_node.getParent()
        #     else:
        #         if prev_node.getBF() == -2:
        #             son_bf = prev_node.getRight().getBF()
        #             if son_bf == -1:
        #                 self.left_rotate(prev_node.getRight(), prev_node)
        #                 r_counter += 1
        #             elif son_bf == 1:
        #                 self.right_left_rotate(prev_node.getRight(), prev_node.getRight().getLeft(), prev_node)
        #                 r_counter += 2
        #         elif prev_node.getBF() == 2:
        #             son_bf = prev_node.getLeft().getBF()
        #             if son_bf == -1:
        #                 self.left_right_rotate(prev_node.getLeft(), prev_node.getLeft().getRight(), prev_node)
        #                 r_counter += 2
        #             elif son_bf == 1:
        #                 self.right_rotate(prev_node.getLeft(), prev_node)
        #                 r_counter += 1

        #        prev_node = prev_node.getParent().getParent()

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        r_counter = 0

        if self.empty(self):
            return -1
        to_remove = self.retrieve_node_rec(self, i)
        if to_remove.getLeft() is None:
            y = to_remove.getParent()
            self.replace_tree(to_remove, to_remove.getRight())
        elif to_remove.getRight() is None:
            y = to_remove.getParent()
            self.replace_tree(to_remove, to_remove.getLeft())
        else:
            successor_node = self.successor(to_remove)
            y = successor_node.getParent()
            if successor_node is not to_remove.getRight():
                self.replace_tree(successor_node, successor_node.getRight())
                successor_node.setRight(to_remove.getRight())
                successor_node.getRight().setParent(successor_node)
            self.replace_tree(to_remove, successor_node)
            successor_node.setLeft(to_remove.getLeft())
            successor_node.getLeft().setParent(successor_node)

        return self.tree_balance(y, r_counter)

    """replaces the subrtree rooted at node A by the subtree rooted at node B.
    B can be a virtual node"""

    def replace_tree(self, A, B):
        if A.getParent() is None:
            self.root = B
        elif A == A.getParent.getLeft():
            A.getParent().setLeft(B)
        else:
            A.getParent().setRight(B)
        if B is not None:
            B.setParent(A.getParent())


"""returns the successor of a given node"""


def successor(self, node):
    if node.right is not None:
        return node.right.first()
    y = node.getParent()
    while y is not None and node == y.right:
        node = y
        y = node.getParent()
    return y


"""returns the value of the first item in the list

@rtype: str
@returns: the value of the first item, None if the list is empty
"""


def first(self):
    if not self.empty():
        first_node = self.root
        while first_node.left.isRealNode():
            first_node = first_node.left
        return first_node.value
    return None


"""returns the value of the last item in the list

@rtype: str
@returns: the value of the last item, None if the list is empty
"""


def last(self):
    if not self.empty():
        first_node = self.root
        while first_node.right.isRealNode():
            first_node = first_node.right
        return first_node.value
    return None


"""returns an array representing list 

@rtype: list
@returns: a list of strings representing the data structure
"""


def listToArray(self):
    values_list = []
    self.sort_rec(self.root, values_list)
    return values_list


"""returns the size of the list 

@rtype: int
@returns: the size of the list
"""


def length(self):
    return self.root.size


"""sort the info values of the list

@rtype: list
@returns: an AVLTreeList where the values are sorted by the info of the original list.
"""


def sort(self):
    values_list = []
    self.sort_rec(self.root, values_list) 
    sorted_values = sorted(values_list)
    sorted_tree = AVLTreeList()
    # for i in range(len(values_list)):
    #     sorted_tree.insert(i, sorted_values[i])
    n = len(sorted_values)
    sorted_tree.build_tree_rec(sorted_values, n)
    return sorted_tree


def sort_rec(self, root, values_list):
    if root.left.isRealNode():
        self.sort_rec(root.left, values_list)

    values_list.append(root.value)

    if root.right.isRealNode():
        self.sort_rec(root.right, values_list)


"""permute the info values of the list 

@rtype: list
@returns: an AVLTreeList where the values are permuted randomly by the info of the original list. ##Use Randomness
"""


# def permutation(self):
#     values = self.listToArray()
#     random.shuffle(values)
#     self.switch_tree_vals(values, 0)

    def permutation(self):
        values = self.listToArray()
        random.shuffle(values)  #todo: shuffle without this function
        n = self.size
        new_tree = AVLTreeList()
        new_tree.build_tree_rec(values, n)
        return new_tree

    """builds an AVL tree recursively from a given array"""

    def build_tree_rec(self, arr, n):
        m = math.floor(n / 2)
        self.root = AVLNode(arr(m))
        self.root.right.build_tree_rec(arr[0:m], m)  # builds an AVL tree from the right half
        self.root.left.build_tree_rec(arr[m + 1:n], n - m)  # builds an AVL tree from the left half


"""switches the values from an AVL tree with the values of a given array
0<= i < arr.length
arr.length = self.size"""


# def switch_tree_vals(self, arr, i):
#     if self.root is not None:
#         switch_tree_vals(self.root.getRight(), arr, i + 1)
#         self.root.setValue(arr(i))
#         switch_tree_vals(self.root.getLeft(), arr, i + 1)


"""concatenates lst to self

@type lst: AVLTreeList
@param lst: a list to be concatenated after self
@rtype: int
@returns: the absolute value of the difference between the height of the AVL trees joined
"""


def concat(self, lst):
    return None


"""searches for a *value* in the list

@type val: str
@param val: a value to be searched
@rtype: int
@returns: the first index that contains val, -1 if not found.
"""


def search(self, val):
    counter = [-1]
    i = self.search_rec(self.root, val, counter)
    return i


def search_rec(self, root, val, counter):
    if root.left.isRealNode():
        i = self.search_rec(root.left, val, counter)
        if i != -1:
            return i

    counter[0] = counter[0] + 1

    if root.value == val:
        return counter[0]
    else:
        if root.right.isRealNode():
            i = self.search_rec(root.right, val, counter)
            if i != -1:
                return i
    return -1


"""returns the root of the tree representing the list

@rtype: AVLNode
@returns: the root, None if the list is empty
"""


def getRoot(self):
    return self.root
