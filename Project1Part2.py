from random import *
import sys

class newNode:
    def __init__(self, num, parent):
        self.num = num
        self.left = None
        self.right = None
        self.parent = parent
        self.height = None
        self.BF = None
        self.visited = None

def insertRecBST(root, num):
    if root is None:
        node = newNode(num, None)
        root = node
        return root
    else:
        if(num < root.num and root.left == None):
            root.left = insertRecBST(root.left, num)
            root.left.parent = root
        elif(num > root.num and root.right == None):
            root.right = insertRecBST(root.right, num)
            root.right.parent = root
        elif(num < root.num and root.left != None):
            insertRecBST(root.left, num)
        elif(num > root.num and root.right != None):
            insertRecBST(root.right, num)

def insertIterBST(root, num):
    if root == None:
        node = newNode(num, None)
        root = node
        return root
    elif(num < root.num and root.left != None):
        while num < root.num and root.left != None:
            root = root.left
        while num > root.num and root.right != None:
            root = root.right
    elif(num > root.num and root.right != None):
        while num > root.num and root.right != None:
            root = root.right
        while num < root.num and root.left != None:
            root = root.left
    if(num > root.num):
        insertNode = newNode(num, root)
        root.right = insertNode
    elif(num < root.num):
        insertNode = newNode(num, root)
        root.left = insertNode

def insertIterBSTCounter(root, num, counter):
    if root == None:
        node = newNode(num, None)
        root = node
        return (root, counter)
    elif(num < root.num and root.left != None):
        while num < root.num and root.left != None:
            root = root.left
            counter+=1
        while num > root.num and root.right != None:
            root = root.right
            counter+=1
    elif(num > root.num and root.right != None):
        while num > root.num and root.right != None:
            root = root.right
            counter+=1
        while num < root.num and root.left != None:
            root = root.left
            counter+=1
    if(num > root.num):
        insertNode = newNode(num, root)
        root.right = insertNode
    elif(num < root.num):
        insertNode = newNode(num, root)
        root.left = insertNode
    return(root, counter)

def insertIter(root, num):
    trueRoot = root
    if root == None:
        node = newNode(num, None)
        root = node
        return root
    elif(num < root.num and root.left != None):
        while num < root.num and root.left != None:
            root = root.left
        while num > root.num and root.right != None:
            root = root.right
    elif(num > root.num and root.right != None):
        while num > root.num and root.right != None:
            root = root.right
        while num < root.num and root.left != None:
            root = root.left
    if(num > root.num):
        insertNode = newNode(num, root)
        root.right = insertNode
    elif(num < root.num):
        insertNode = newNode(num, root)
        root.left = insertNode
    computeHeightIter(trueRoot)
    computeBalanceIter(trueRoot)
    root = rebalanceIter(trueRoot)
    treeReset(root)
    return root


def computeHeightIter(root):
    while(True):
        if(root.left != None and root.left.height is None):
            root = root.left
        elif(root.right != None and root.right.height is None):
            root = root.right
        else:
            if(root.left is None and root.right is None):
                root.height = 1
            elif(root.left != None and root.right != None):
                if(root.left.height > root.right.height):
                    root.height = root.left.height + 1
                else:
                    root.height = root.right.height + 1
            elif(root.left != None and root == root.left.parent):
                root.height = root.left.height + 1
            elif(root.right != None and root == root.right.parent):
                root.height = root.right.height + 1
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return

def treeReset(root):
    while(True):
        if(root.left != None and root.left.height != None):
            root = root.left
        elif(root.right != None and root.right.height != None):
            root = root.right
        else:
            if(root.left is None and root.right is None):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.left != None and root.right != None):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.left != None and root == root.left.parent):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.right != None and root == root.right.parent):
                root.height = None
                root.BF = None
                root.visited = None
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return

def computeBalanceIter(root):
    while(True):
        if(root.left != None and root.left.BF is None):
            root = root.left
        elif(root.right != None and root.right.BF is None):
            root = root.right
        else:
            if(root.left is None and root.right is None):
                root.BF = 0
            else:
                if(root.left is None):
                    root.BF = 0 - root.right.height
                elif(root.right is None):
                    root.BF = root.left.height - 0
                else:
                    root.BF = root.left.height - root.right.height
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return

def rebalanceIter(root):
    wasRoot = False
    tempNode = None
    tempNode2 = None
    tempnode3 = None
    nextRoot = None
    while(True):
        if(root.left != None and root.left.visited is None):
            root = root.left
        elif(root.right != None and root.right.visited is None):
            root = root.right
        else:
            if(root.BF > 1 or root.BF < -1):
                if(root.BF > 1):
                    if(root.left.BF == 1):     #Left-Left Case
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return root
                    elif(root.left.BF == -1):    #Left-Right Case
                        root = root.left
                        nextRoot = root.parent
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        tempNode = None
                        tempNode2 = None
                        root = nextRoot
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return root
                elif(root.BF < -1):
                    if(root.right.BF == -1):     #Right-Right Case
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return root
                    elif(root.right.BF == 1):   #Right-Left Case
                        root = root.right
                        nextRoot = root.parent
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        tempNode = None
                        tempNode2 = None
                        root = nextRoot
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return root
            if(root.parent != None):
                root.visited = True
                root = root.parent
            elif(root.parent is None and (root.BF >= -1 and root.BF <= 1)):
                return root

def deleteIter(root, num):
    if root is None:
        return root
    else:
        while(root.left != None or root.right != None):
            if(num > root.num and root.right != None):
                root = root.right
            elif(num < root.num and root.left != None):
                root = root.left
            elif(num == root.num):
                break
        if root.left is None and root.right is None:
            if(root.parent.left is root):
                root.parent.left = None
                root = None
                return root
            elif(root.parent.right is root):
                root.parent.right = None
                root = None
                return root
        if root.left != None and root.right is None:
            root.parent.left = root.left
            return root
        elif root.left is None and root.right != None:
            root.parent.right = root.right
            return root
        elif root.left != None and root.right != None:
            temp = findMaxIter(root.left)
            root.num = temp.num
            if(temp.parent.left is temp):
                temp.parent.left = temp.right
            elif(temp.parent.right is temp):
                temp.parent.right = temp.left

def findNextIter(root,num):
    if root is None:
        return root
    else:
        while(root.left != None or root.right != None):
            if(num > root.num and root.right != None):
                root = root.right
            elif(num < root.num and root.left != None):
                root = root.left
            elif(num == root.num):
                break
            elif(num < root.num and root.left == None):
                return root
            elif(num > root.num and root.right == None):
                return root.parent
        if(num == root.num and root.right != None):
            root = findMinIter(root.right)
        elif(num == root.num and root.right is None):
            if(root is root.parent.left):
                return root.parent
            elif(root is root.parent.right):
                return root.parent.parent
        elif(num > root.num and root.right == None):
            return root.parent
    return root

def findPrevIter(root, num):
    if root is None:
        return root
    else:
        while(root.left != None or root.right != None):
            if(num > root.num and root.right != None):
                root = root.right
            elif(num < root.num and root.left != None):
                root = root.left
            elif(num == root.num):
                break
            elif(num < root.num and root.left == None and root is root.parent.left):
                return root.parent.parent
            elif(num < root.num and root.left == None):
                return root.parent
            elif(num > root.num and root.right is None):
                return root
        if(num == root.num and root.left != None):
            root = findMaxIter(root.left)
        elif(num == root.num and root.left is None):
            if(root is root.parent.right):
                return root.parent
            elif(root is root.parent.left):
                return root.parent.parent
        elif(num < root.num):
            return root.parent
    return root



def findMinIter(root):
    if root is None:
        return root
    else:
        while(root.left != None):
            root = root.left
        return root

def findMaxIter(root):
    if root is None:
        return root
    else:
        while(root.right != None):
            root = root.right
        return root

def getRandomArray(size):
    randArray = []
    randNum = 0
    for i in range(0, size):
        randNum = randint(-100000, 100000)
        #randNum = randint(0,100)
        if randNum not in randArray:
            randArray.append(randNum)
    return randArray

def questionFiveA():
    iterRoot = None
    array = getRandomArray(10000)
    for num in array:
        iterRoot = insertIter(iterRoot,num)
    print("Iterative Approach Insertion on AVL Tree Worked.")
    print()
    recRoot = None
    for num in array:
        if(recRoot is None):
            recRoot = insertRecBST(recRoot, num)
        else:
            insertRecBST(recRoot, num)
    print("Recursive Approach Insertion on BST Worked.")

def questionFiveC():
    iterRoot = None
    array = getRandomArray(10000)
    for num in array:
        iterRoot = insertIter(iterRoot,num)
    print("Iterative Approach Insertion on AVL Tree Worked.")
    print()
    iterBSTRoot = None
    for num in array:
        if(iterBSTRoot is None):
            iterBSTRoot = insertIterBST(iterBSTRoot, num)
        else:
            insertIterBST(iterBSTRoot, num)
    print("Iterative Approach Insertion on BST Worked.")

def insertIterCounter(root, counter, num):
    trueRoot = root
    if root == None:
        node = newNode(num, None)
        root = node
        return (root, counter)
    elif(num < root.num and root.left != None):
        while num < root.num and root.left != None:
            root = root.left
            counter+=1
        while num > root.num and root.right != None:
            root = root.right
            counter+=1
    elif(num > root.num and root.right != None):
        while num > root.num and root.right != None:
            root = root.right
            counter+=1
        while num < root.num and root.left != None:
            root = root.left
            counter+=1
    if(num > root.num):
        insertNode = newNode(num, root)
        root.right = insertNode
    elif(num < root.num):
        insertNode = newNode(num, root)
        root.left = insertNode
    counter = computeHeightIterCounter(trueRoot, counter)
    counter = computeBalanceIterCounter(trueRoot, counter)
    root, counter = rebalanceIterCounter(trueRoot, counter)
    counter = treeResetCounter(root, counter)
    return (root, counter)


def computeHeightIterCounter(root, counter):
    while(True):
        if(root.left != None and root.left.height is None):
            root = root.left
            counter+=1
        elif(root.right != None and root.right.height is None):
            root = root.right
            counter+=1
        else:
            if(root.left is None and root.right is None):
                root.height = 1
            elif(root.left != None and root.right != None):
                if(root.left.height > root.right.height):
                    root.height = root.left.height + 1
                else:
                    root.height = root.right.height + 1
            elif(root.left != None and root == root.left.parent):
                root.height = root.left.height + 1
            elif(root.right != None and root == root.right.parent):
                root.height = root.right.height + 1
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return counter

def treeResetCounter(root, counter):
    while(True):
        if(root.left != None and root.left.height != None):
            root = root.left
            counter+=1
        elif(root.right != None and root.right.height != None):
            root = root.right
            counter+=1
        else:
            if(root.left is None and root.right is None):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.left != None and root.right != None):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.left != None and root == root.left.parent):
                root.height = None
                root.BF = None
                root.visited = None
            elif(root.right != None and root == root.right.parent):
                root.height = None
                root.BF = None
                root.visited = None
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return counter

def computeBalanceIterCounter(root, counter):
    while(True):
        if(root.left != None and root.left.BF is None):
            root = root.left
            counter+=1
        elif(root.right != None and root.right.BF is None):
            root = root.right
            counter+=1
        else:
            if(root.left is None and root.right is None):
                root.BF = 0
            else:
                if(root.left is None):
                    root.BF = 0 - root.right.height
                elif(root.right is None):
                    root.BF = root.left.height - 0
                else:
                    root.BF = root.left.height - root.right.height
            if(root.parent != None):
                root = root.parent
            elif(root.parent is None):
                return counter

def rebalanceIterCounter(root, counter):
    wasRoot = False
    tempNode = None
    tempNode2 = None
    tempnode3 = None
    nextRoot = None
    while(True):
        if(root.left != None and root.left.visited is None):
            root = root.left
            counter+=1
        elif(root.right != None and root.right.visited is None):
            root = root.right
            counter+=1
        else:
            if(root.BF > 1 or root.BF < -1):
                if(root.BF > 1):
                    if(root.left.BF == 1):     #Left-Left Case
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return (root, counter)
                    elif(root.left.BF == -1):    #Left-Right Case
                        root = root.left
                        nextRoot = root.parent
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        tempNode = None
                        tempNode2 = None
                        root = nextRoot
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.left = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return (root, counter)
                elif(root.BF < -1):
                    if(root.right.BF == -1):     #Right-Right Case
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return (root, counter)
                    elif(root.right.BF == 1):   #Right-Left Case
                        root = root.right
                        nextRoot = root.parent
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.left.right != None):
                            tempNode = root.left.right
                        root.left.right = root
                        root.parent = root.left
                        root.left = tempNode
                        if(tempNode != None):
                            root.left.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        tempNode = None
                        tempNode2 = None
                        root = nextRoot
                        if(root.parent is None):
                            wasRoot = True
                        else:
                            tempNode2 = root.parent
                        if(root.right.left != None):
                            tempNode = root.right.left
                        root.parent = root.right
                        root.right.left = root
                        root.right = tempNode
                        if(tempNode != None):
                            root.right.parent = root
                        if(wasRoot):
                            root.parent.parent = None
                        else:
                            root.parent.parent = tempNode2
                            root.parent.parent.right = root.parent
                        while(root.parent != None):
                            root = root.parent
                        return (root, counter)
            if(root.parent != None):
                root.visited = True
                root = root.parent
            elif(root.parent is None and (root.BF >= -1 and root.BF <= 1)):
                return (root, counter)

def question6B():
    counterBST = 0
    counterAVL = 0
    array = getRandomArray(10000)
    BSTRoot = None
    for num in array:
        if BSTRoot is None:
            BSTRoot, counterBST = insertIterBSTCounter(BSTRoot, num, counterBST)
        else:
            uselessRoot, counterBST = insertIterBSTCounter(BSTRoot, num, counterBST)
    print("Levels traversed in BST Iterative Insertion: " + str(counterBST))
    print()
    AVLRoot = None
    for num in array:
        AVLRoot, counterAVL = insertIterCounter(AVLRoot, num, counterAVL)
    print("Levels Traversed in AVL Iterative Insertion: " + str(counterAVL))
    print()

def getSortedArray(size):
    sortedArray = []
    for i in range(0,size):
        sortedArray.append(size-i)
    return sortedArray

def question6C():
    counterBST = 0
    counterAVL = 0
    array = getSortedArray(10000)
    BSTRoot = None
    for num in array:
        if BSTRoot is None:
            BSTRoot, counterBST = insertIterBSTCounter(BSTRoot, num, counterBST)
        else:
            uselessRoot, counterBST = insertIterBSTCounter(BSTRoot, num, counterBST)
    print("Levels traversed in BST Iterative Insertion: " + str(counterBST))
    print()
    AVLRoot = None
    for num in array:
        AVLRoot, counterAVL = insertIterCounter(AVLRoot, num, counterAVL)
    print("Levels Traversed in AVL Iterative Insertion: " + str(counterAVL))
    print()
