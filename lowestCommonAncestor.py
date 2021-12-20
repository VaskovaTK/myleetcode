# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     firstSavedRoot = root
    #     secondSavedRoot = root
    #     firstList = self.passOfTheTree(firstSavedRoot,list(),p)
    #     secondList = self.passOfTheTree(secondSavedRoot,list(),q)
    #     # if q in firstList:
    #     #     return q
    #     # if p in secondList:
    #     #     return p
    #     # else:
    #     dictionary ={}
    #     for i in range(len(firstList)):
    #         dictionary[firstList[i][0]] =firstList[i][1]
    #     for j in range(-1,-len(secondList)-1,-1):
    #         if secondList[j][0] in dictionary and dictionary[secondList[j][0]] < secondList[j][1]:
    #             return secondList[j][0]
    #
    #     return TreeNode(None)
    #
    #
    #
    # def passOfTheTree(self, root:TreeNode,queuePass:list,searchRoot:TreeNode):
    #     queue = deque()
    #     level = 0
    #     if root is not None:
    #         queue.append((root,level))
    #         queuePass.append((root,level))
    #         if root == searchRoot:
    #             return queuePass
    #     while len(queue)>0:
    #         fromQueue = queue.pop()
    #         rootFromQueue = fromQueue[0]
    #         level = fromQueue[1]+1
    #         if rootFromQueue.right is not None:
    #             queue.append((rootFromQueue.right,level))
    #             queuePass.append((rootFromQueue.right,level))
    #             if rootFromQueue.right == searchRoot:
    #                 return queuePass
    #         if rootFromQueue.left is not None:
    #             queue.append((rootFromQueue.left,level))
    #             queuePass.append((rootFromQueue.left,level))
    #             if rootFromQueue.left == searchRoot:
    #                 return queuePass
    #     return queuePass
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

def createTree (root,node1,node2,node3,node4,node5,node6):
    savedRoot = TreeNode(root)
    savedRoot.left = TreeNode(node1)
    savedRoot.right = TreeNode(node2)
    savedRoot.left.left = TreeNode(node3)
    savedRoot.left.right = TreeNode(node4)
    savedRoot.right.left = TreeNode(node5)
    savedRoot.right.right = TreeNode(node6)
    return savedRoot

sol = Solution()
tree = createTree(3,8,6,7,2,4,5)
print(sol.lowestCommonAncestor(tree,tree.left,tree.left.left).val)



