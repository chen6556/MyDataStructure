from node import BinaryTreeNode
from util import util


class AVLTree:

    def __init__(self, value=[None]) -> None:
        self.__head_node = BinaryTreeNode()
        if isinstance(value, list):
            self.build_from_data(value)
        else:
            raise TypeError("BinarySearchTree初始化值必须是list")
    
    @property
    def head_node(self):
        return self.__head_node

    @head_node.setter
    def head_node(self, node):
        if isinstance(node, BinaryTreeNode) or node == None:
            self.__head_node = node
        else:
            raise TypeError
        
    @property
    def value(self):
        return self.__head_node.value

    @property
    def left_node(self):
        return self.__head_node.left_node 

    @property
    def right_node(self):
        return self.__head_node.right_node

    def get_height(self, node:BinaryTreeNode) -> int:
        if node is None:
            return 0
        elif isinstance(node, BinaryTreeNode):
            return max(self.get_height(node.left_node), self.get_height(node.right_node))+1
        else:
            raise TypeError("必须是BinaryTreeNode")

    def __right_rotate(self, node:BinaryTreeNode): # 向右旋转 
        parent = node.parent_node
        left = node.left_node    
        node.left_node = left.right_node
        left.right_node = node
        if node is self.__head_node: 
            self.__head_node = left 
        elif parent.left_node is node:
            parent.left_node = left
        else:
            parent.right_node = left

    def __left_rotate(self, node:BinaryTreeNode): # 向左旋转 
        parent = node.parent_node
        right = node.right_node    
        node.right_node = right.left_node
        right.left_node = node
        if node is self.__head_node: 
            self.__head_node = right
        elif parent.left_node is node:
            parent.left_node = right
        else:
            parent.right_node = right

    def __minimum_unbalanced_tree(self, begin:BinaryTreeNode) -> BinaryTreeNode:
        temp = begin.parent_node
        if temp is None: 
            return None
        elif self.get_height(temp.left_node) - self.get_height(temp.right_node) > 1 or self.get_height(temp.right_node) - self.get_height(temp.left_node) > 1:
            return temp
        else:
            temp = temp.parent_node
        if temp is None : 
            return None
        elif self.get_height(temp.left_node) - self.get_height(temp.right_node) > 1 or self.get_height(temp.right_node) - self.get_height(temp.left_node) > 1:
            return temp
        else:
            return None

    def __balance(self, node:BinaryTreeNode):
        if node is None: return
        if self.get_height(node.right_node) - self.get_height(node.left_node) > 1: # 右子树高于左子树
            # 如果当前结点的 右子树的左子树 高于 右子树的右子树
            if node.right_node and self.get_height(node.right_node.left_node) > self.get_height(node.right_node.right_node):
                # 先对当前结点的右子树进行右旋转
                self.__right_rotate(node.right_node)
                # 再对当前结点进行左旋转
                self.__left_rotate(node)
            else:
                # 直接进行左旋转
                self.__left_rotate(node)
        elif self.get_height(node.left_node) - self.get_height(node.right_node) > 1: # 左子树高于右子树
            # 如果当前结点的 左子树的右子树 高于 左子树的左子树
            if node.left_node and self.get_height(node.left_node.right_node) > self.get_height(node.left_node.left_node):
                # 先对当前结点的左子树进行左旋转
                self.__left_rotate(node.left_node)
                # 再对当前结点进行右旋转
                self.__right_rotate(node)
            else:
                # 直接进行右旋转
                self.__right_rotate(node)

    def build_from_data(self, data:list):
        self.__head_node.value = data[0]
        for d in data[1:]:
            node = self.__head_node
            while True:
                if d > node.value:
                    if node.right_node:
                        node = node.right_node
                        continue
                    else:
                        node.right_node = BinaryTreeNode(d)
                        break
                elif d < node.value:   
                    if node.left_node:
                        node = node.left_node
                        continue
                    else:
                        node.left_node = BinaryTreeNode(d)
                        break
            check_node = self.__minimum_unbalanced_tree(node)
            self.__balance(check_node)

    def have(self, value) -> bool:
        node = self.__head_node
        while node:
            if node.value < value:
                node = node.right_node
            elif node.value > value:
                node = node.left_node 
            else:
                return True
        return False

    def find(self, value) -> BinaryTreeNode:
        node = self.__head_node
        while node:
            if node.value < value:
                node = node.right_node
            elif node.value > value:
                node = node.left_node 
            else:
                return node
        return None

    def append(self, value) -> bool:
        node = self.__head_node
        while node:
            temp = node
            if node.value < value:
                node = node.right_node
            elif node.value > value:
                node = node.left_node 
            else:
                return False
        if temp.value > value:
            temp.left_node = BinaryTreeNode(value)            
        else:
            temp.right_node = BinaryTreeNode(value)
        check_node = self.__minimum_unbalanced_tree(temp)
        self.__balance(check_node)
        return True

    def remove(self, value) -> bool:
        node = self.__head_node
        while node:
            if node.value < value:
                node = node.right_node
            elif node.value > value:
                node = node.left_node 
            else:
                break
        if node == None: return False
        if node.right_node == None:
            if node is node.parent_node.left_node:
                node.parent_node.left_node = node.left_node
            else:
                node.parent_node.right_node = node.left_node
            check_node = self.__minimum_unbalanced_tree(node)
            self.__balance(check_node)
            del node    
        elif node.left_node == None:
            if node.parent_node.left_node is node:
                node.parent_node.left_ndoe = node.right_node
            else:
                node.parent_node.right_ndoe = node.right_node
            check_node = self.__minimum_unbalanced_tree(node)
            self.__balance(check_node)
            del node
        else:
            temp = node.left_node
            while temp.right_node:
                temp = temp.right_node 
            node.value = temp.value
            if temp.parent_node is node:
                node.left_node = temp.left_node
            else:
                temp.parent_node.right_node = temp.left_node
            check_node = self.__minimum_unbalanced_tree(node)
            self.__balance(check_node)
            del temp
        return True



if __name__ == "__main__":
    data = [3,2,1,4,5,6,7,10,9,8]
    avl = AVLTree(data)
    avl.append(11)
    avl.append(0)
    avl.append(-1)
    avl.remove(8)
    print( util.floororder_traverse(avl) )
