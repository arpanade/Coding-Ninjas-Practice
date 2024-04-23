from os import *
from sys import *
from collections import *
from math import *

# Binary Tree node structure.
class   TreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    def __del__(self):
        if self.left:
            del self.left
        if self.right:
            del self.right

def preorderToBST(preorder):
    preorder.sort()
    for i in preorder:
        print(i,end=" ")
        

n=[5,6,3,1,8]

preorderToBST(n)