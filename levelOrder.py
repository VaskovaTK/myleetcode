# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        way = self.passOfTheTree(root,[])
        if way == []:
            return way
        retList = []
        levelList = []
        level = -1
        for i in range(len(way)):
            if level<way[i][1]:
                if levelList !=[]:
                    retList.append(levelList)
                level+=1
                levelList = []
                levelList.append(way[i][0].val)
            else:
                levelList.append(way[i][0].val)
        if levelList !=[]:
            retList.append(levelList)
        return retList



    def passOfTheTree(self, root: TreeNode, queuePass: list):
        queue = deque()
        level = 0
        if root is not None:
            queue.append((root,level))
            queuePass.append((root,level))
        while len(queue)>0:
            fromQueue = queue.pop()
            rootFromQueue = fromQueue[0]
            level = fromQueue[1]+1
            if rootFromQueue.left is not None:
                queue.append((rootFromQueue.left,level))
                queuePass.append((rootFromQueue.left,level))
            if rootFromQueue.right is not None:
                queue.append((rootFromQueue.right,level))
                queuePass.append((rootFromQueue.right,level))
        return queuePass

def createTree (root,node1,node2,node3,node4,node5,node6):
    savedRoot = TreeNode(root)
    savedRoot.left = TreeNode(node1)
    savedRoot.right = TreeNode(node2)
    savedRoot.left.left = TreeNode(node3)
    savedRoot.left.right = TreeNode(node4)
    savedRoot.right.left = TreeNode(node5)
    savedRoot.right.right = TreeNode(node6)
    return savedRoot

tree = createTree(3,8,6,7,2,4,5)

sol = Solution()
# print(sol.levelOrder(tree))
print(sol.levelOrder(TreeNode()))