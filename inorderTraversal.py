# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        queue = deque()
        if root != None:
            queue.append(root)
        else:
            return list()
        retList = []
        while len(queue)>0:
            elFromQueue = queue.popleft()
            if elFromQueue.left != None:
                queue.append(elFromQueue.left)
            if elFromQueue.right != None:
                queue.append(elFromQueue.right)
            retList.append(elFromQueue.val)
        print(retList)
        return retList






    def createTree(self,array):
        root = None
        signRoot = None
        i = 0
        while i < len(array):
            if root == None:
                root =TreeNode(array[i])
                signRoot = root
                i+=1
            else:
                if root.left== None:
                    root.left = TreeNode(array[i])
                    i+=1
                elif root.right == None:
                    root.right = TreeNode(array[i])
                    i+=1
                else:
                    root = root.left
                    continue

        return signRoot


sol = Solution()
sol.inorderTraversal(sol.createTree([1,2,3,4,5]))