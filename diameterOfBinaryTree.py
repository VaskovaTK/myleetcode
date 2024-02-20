from collections import deque
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def diameterOfBinaryTree(self, root) -> int:
        if root.left:
            left = self.findDiameter(root.left, 1)
        else:
            left = 0
        if root.right:
            right = self.findDiameter(root.right, 1)
        else:
            right = 0
        return left + right


    def findDiameter(self, leftRoot, level):
        if leftRoot == None:
            return level-1
        else:
            return max(self.findDiameter(leftRoot.left, level+1), self.findDiameter(leftRoot.right,level+1))


def example():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    return root

def exampleTwo():
    root = TreeNode(4)
    root.left = TreeNode(-7)
    root.right = TreeNode(-3)
    root.left.left = None
    root.left.right = None









def createNode(vals: list, idx: int):
    if len(vals)-1 < idx:
        return None
    # if vals[idx] <0:
    #     return None
    ret = TreeNode(vals[idx])
    ret.left = createNode(vals, idx*2+1)
    ret.right = createNode(vals, idx * 2 + 2)
    return ret

# listOfNodes = [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
listOfNodes =   [4,-7,-3,None,None,-9,-3,9,-7,-4,None,6,None,-6,-6,None,None,0,6,5,None,9,None,None,-1,-4,None,None,None,-2]
realTree = createNode(listOfNodes,0)


sol = Solution()
# print(sol.diameterOfBinaryTree(example()))
print(sol.diameterOfBinaryTree(realTree))


# private static void check(TreeDiameter td, int expected, int[] tree) {
#         TreeNode root = createNode(tree);
#         int actual = td.diameterOfBinaryTree(root);
#         if (actual != expected) {
#             System.out.println("Expected [" + expected + "], actual [" + actual + "], tree " + Arrays.toString(tree));
#         }
#     }
#
#     private static TreeNode createNode(int[] vals) {
#         return createNode(vals, 0);
#     }
#
#     private static TreeNode createNode(int[] vals, int idx) {
#         if (vals.length - 1 < idx) return null;
#         if (vals[idx] < 0) return null;
#         TreeNode ret = new TreeNode(vals[idx]);
#         ret.left = createNode(vals, idx * 2 + 1);
#         ret.right = createNode(vals, idx * 2 + 2);
#         return ret;
#     }
#
# TreeDiameter td = new TreeDiameter();
#         check(td, 1, new int[]{1, 2});
#         check(td, 2, new int[]{1, 2, 3});
#         check(td, 3, new int[]{1, 2, 3, 4, 5});







