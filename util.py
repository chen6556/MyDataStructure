from node import BinaryTreeNode
from structure import BinarySearchTree

# 工具类

class util:

    @staticmethod
    def show_mat(mat:list) -> None:
        length = len(str(max([max(row) for row in mat])))
        print("--"*(len(mat)*length))
        for row in mat:
            for j in row:
                print(' '*(length-len(str(j))) , j, sep='', end=' ')
            print()
        print("--"*(len(mat)*length))

    @staticmethod
    def create_tree_preorder(data:list) -> BinaryTreeNode:
    
        def func(data, node):
            try:
                value = next(data)
            except StopIteration:
                return None
            
            if  value is None:
                return None
            else:
                node = BinaryTreeNode(value)
                node.left_node = func(data, node.left_node) 
                node.right_node = func(data, node.right_node)
                return node

        data_iter = iter(data)
        return func(data_iter, None)

    @staticmethod
    def create_tree_floororder(data:list) -> BinaryTreeNode:
        if not data or not data[0]: return None
        head_node = BinaryTreeNode(data.pop(0))
        lay = [head_node]
        next_lay = list()
        while data:
            for node in lay:   
                if data: 
                    value = data.pop(0)
                    if value is not None:
                        node.left_node = BinaryTreeNode(value)
                        next_lay.append( node.left_node)
                    else:
                        next_lay.append(None)
                else:
                    break
                if data: 
                    value = data.pop(0)
                    if value is not None:
                        node.right_node = BinaryTreeNode(value)
                        next_lay.append(node.right_node)
                    else:
                        next_lay.append(None)
                else:
                    break
            lay = next_lay[::]
            next_lay.clear()
        return head_node

    @staticmethod
    def preorder_traverse(tree:BinaryTreeNode) -> list:
    
        def func(node:BinaryTreeNode):
            nonlocal ans
            if node:
                ans.append(node.value)
                func(node.left_node)
                func(node.right_node)
        
        ans = list()    
        func(tree)
        return ans

    @staticmethod
    def inorder_traverse(tree:BinaryTreeNode) -> list:
    
        def func(node:BinaryTreeNode):
            nonlocal ans
            if node:
                func(node.left_node)
                ans.append(node.value)
                func(node.right_node)
        
        ans = list()    
        func(tree)
        return ans

    @staticmethod
    def postorder_traverse(tree:BinaryTreeNode) -> list:
    
        def func(node:BinaryTreeNode):
            nonlocal ans
            if node:
                func(node.left_node)
                func(node.right_node)
                ans.append(node.value)
        
        ans = list()    
        func(tree)
        return ans

    @staticmethod
    def floororder_traverse(tree:BinaryTreeNode) -> list:
        temp = [tree]
        ans = [[tree.value]] if tree else None
        while temp:
            lay = list()
            lay_values = list()
            for node in temp:
                if node.left_node:
                    lay.append(node.left_node)
                    lay_values.append(node.left_node.value)
                if node.right_node:
                    lay.append(node.right_node)
                    lay_values.append(node.right_node.value)
            temp = lay
            if lay_values:
                ans.append(lay_values)
        return ans

    @staticmethod
    def build_binary_search_tree(data:list) -> BinaryTreeNode:
        tree = BinarySearchTree(data[0])
        for d in data[1:]:
            node = tree.head_node
            while True:
                if d >= node.value:
                    if node.right_node:
                        node = node.right_node
                        continue
                    else:
                        node.right_node = BinaryTreeNode(d)
                        node.right_node.parent_node = node
                        break
                else:   
                    if node.left_node:
                        node = node.left_node
                        continue
                    else:
                        node.left_node = BinaryTreeNode(d)
                        node.left_node.parent_node = node
                        break
        return tree

