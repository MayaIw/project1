# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info
# todo: return the part above to the conventions of the beginning and fill it

"""A class represnting a node in an AVL tree"""


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
        self.bf = 0

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
        return None

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
        pass
        # new_node = AVLNode(val)
        # new_node.setSize(1)
        # if self.size == 0:
        #     new_node.setLeft(AVLNode(None))
        #     new_node.setRight(AVLNode(None))
        #     new_node.setHeight(0)
        #     self.root = new_node
        #     return 0
        # if self.size == i:
        #     prev_node = self.retrieve_node_rec(self.root, self.size - 1)
        #     prev_node.right = new_node
        # else:
        #     prev_node = self.retrieve_node_rec(self.root, i)
        #     if not prev_node.left.isRealNode():
        #         prev_node.left = new_node
        #         prev_node.size += 1
        #
        #
        # return -1

    """deletes the i'th item in the list

    @type i: int
    @pre: 0 <= i < self.length()
    @param i: The intended index in the list to be deleted
    @rtype: int
    @returns: the number of rebalancing operation due to AVL rebalancing
    """

    def delete(self, i):
        return -1

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
        return None

    """returns an array representing list 

    @rtype: list
    @returns: a list of strings representing the data structure
    """

    def listToArray(self):
        return None

    """returns the size of the list 

    @rtype: int
    @returns: the size of the list
    """

    def length(self):
        return None

    """sort the info values of the list

    @rtype: list
    @returns: an AVLTreeList where the values are sorted by the info of the original list.
    """

    def sort(self):
        values_list = []
        self.sort_rec(self.root, values_list)  # todo: sort_rec is exactly listToArray
        sorted_values = sorted(values_list)
        sorted_tree = AVLTreeList()
        for i in range(len(values_list)):
            sorted_tree.insert(i, sorted_values[i])
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

    def permutation(self):
        return None

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
        return None
