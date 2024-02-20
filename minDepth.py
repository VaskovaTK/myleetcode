# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        array = list()
        array.append(99999)
        array = self.recursion(root,1,1,array)
        return array[0]


    def recursion(self, root, depthR, depthL,array):
        if root.right:
            array = self.recursion(root.right, depthR+1, depthL,array)
        else:
            if depthL> 1:
                array[0] = min(depthR, depthL, array[0])
                return array
            else:
                array[0] = min(depthR, array[0])
                return array
        if root.left:
            array = self.recursion(root.left, depthR, depthL+1,array)
        else:
            if depthR>1:
                array[0] = min(depthR, depthL, array[0])
                return array
            else:
                array[0] = min(depthL,array[0])
                return array




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
sol.minDepth(sol.createTree([3,9,20,None,None,15,7]))