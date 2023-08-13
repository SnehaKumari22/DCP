"""
Serialize deserialize binary tree
Geiven root of binary tree serialize the tree to a string and deserialize the string back to tree
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]
Input: root = []
Output: []
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        stack=[root]
        while(len(stack)>0):
            node = stack.pop(0)
            if node is None:
                res.append('#')
            else:
                res.append(str(node.val))
                stack.append(node.left)
                stack.append(node.right)
        # print(res)
        return ','.join(res)

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        node =data.pop(0)
        if node is '#':
            return None
        mainnode = TreeNode(node)
        root =[mainnode]
        while(len(data)!=0):
            left = data.pop(0)
            right = data.pop(0)
            node = root.pop(0)
            if left is '#': 
                node.left=None
            else: 
                node.left=TreeNode(left)
                root.append(node.left)
            if right is '#': node.right=None
            else: 
                node.right=TreeNode(right)
                root.append(node.right)
        
        return mainnode
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))