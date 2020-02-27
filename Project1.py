from random import *
import sys

class newNode:
    def __init__(self, num, parent):
        self.num = num
        self.left = None
        self.right = None
        self.parent = parent

def insertRec(root, num):
    if root is None:
        node = newNode(num, None)
        root = node
        return root
    else:
        if(num < root.num and root.left == None):
            root.left = insertRec(root.left, num)
            root.left.parent = root
        elif(num > root.num and root.right == None):
            root.right = insertRec(root.right, num)
            root.right.parent = root
        elif(num < root.num and root.left != None):
            insertRec(root.left, num)
        elif(num > root.num and root.right != None):
            insertRec(root.right, num)

def deleteRec(root, num):
    if root is None:
        return root
    if(num < root.num):
        root.left = deleteRec(root.left, num)
    elif(num > root.num):
        root.right = deleteRec(root.right, num)
    else:
        if(root.left == None and root.right == None):
            root = None
            return root
        elif(root.left == None):
            right = root.right
            root = None
            return right
        elif(root.right == None):
            left = root.left
            root = None
            return left
        temp = findMinRec(root.right)
        root.num = temp.num
        root.right = deleteRec(root.right, temp.num)
    return root

def findNextRec(root, num):
    if(num < root.num and root.left is None):
        return root
    elif(num > root.num and root.right is None):
        if(num <= root.parent.num):
            return root.parent
        else:
            return None
    elif(num == root.num and root.right == None and root.parent != None):
        return root.parent
    elif(num == root.num and root.right != None):
        return root.right
    elif(num < root.num and root.left != None):
        return findNextRec(root.left, num)
    elif(num > root.num and root.right != None):
        return findNextRec(root.right, num)

def findPrevRec(root, num):
    if(num > root.num and root.right is None):
        return root
    elif(num < root.num and root.left is None):
        if(num >= root.parent.num):
            return root.parent
        else:
            return None
    elif(num == root.num and root.left == None and root.parent != None):
        return root.parent
    elif(num == root.num and root.left != None):
        return root.left
    elif(num > root.num and root.right != None):
        return findPrevRec(root.right, num)
    elif(num < root.num and root.left != None):
        return findPrevRec(root.left, num)

def findMinRec(root):
    if(root.left != None):
        return findMinRec(root.left)
    else:
        return root

def findMaxRec(root):
    if(root.right != None):
        return findMinRec(root.right)
    else:
        return root

def insertIter(root, num):
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


def sort(array):
    root = None
    sortedArray = []
    root = insertRec(root, array[0])
    for i in range(1, len(array)):
        insertRec(root, array[i])
    for i in range(0,len(array)):
        sortedArray.append(findMinRec(root).num)
        root = deleteRec(root, findMinRec(root).num)
    return sortedArray

def getRandomArray(size):
    randArray = []
    randNum = 0
    for i in range(0, size):
        randNum = randint(-sys.maxsize, sys.maxsize)
        if randNum not in randArray:
            randArray.append(randNum)
    return randArray

def getSortedArray(size):
    sortedArray = []
    for i in range(0,size):
        sortedArray.append(size-i)
    return sortedArray
