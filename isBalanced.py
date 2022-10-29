from _collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        result = self.check(root,True,1)
        return result

    def check (self, root:TreeNode,beforeResult,level):
        if root.right:
            levelRight = self.bypass(root.right,level)
            beforeResult = self.check(root.right,beforeResult,level+1)
        else:
            levelRight = 0
        if root.left:
            levelLeft = self.bypass(root.left,level)
            beforeResult = self.check(root.left,beforeResult,level+1)
        else:
            levelLeft = 0
        if levelLeft == levelRight or levelLeft + 1 == levelRight or levelLeft - 1 == levelRight:
            if beforeResult == False:
                return False
            else:
                return True
        else:
            return False



    def bypass (self, root:TreeNode,level:int):
        newQueue = deque()

        newQueue.append((root,level))
        while len(newQueue)>0:
            node,level = newQueue.pop()
            if node.left:
                newQueue.append((node.left,level+1))
            if node.right:
                newQueue.append((node.right,level+1))
        return level


def example (root, node1,node2,node3,node4,node5):
    rootNew = TreeNode(root)
    rootNew.right = TreeNode(node2)
    rootNew.left = TreeNode(node1)
    rootNew.right.left = TreeNode(node3)
    rootNew.right.right = TreeNode(node4)
    rootNew.right.right.right = TreeNode(node5)
    return rootNew

sol = Solution()
print(sol.isBalanced(example(2,1,4,3,5,6)))

# [1,2,2,3,null,null,3,4,null,null,4] не сработал, ввести такой пример дерева и посмотреть что идет не так, сначала нарисовать это дерево на бумаге чтобы понять как расположены узлы
# почитать теорию поиска сбалансированных бинарных деревьев