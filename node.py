# 结点

class LinkedListNode:
    def __init__(self, value = None) -> None:
        self.value = value
        self.__last_node = None
        self.__next_node = None

    @property
    def last_node(self):
        return self.__last_node

    @last_node.setter
    def last_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__last_node = node
        else:
            raise TypeError("必须是LinkedListNode")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__next_node = node
        else:
            raise TypeError("必须是LinkedListNode")

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, self.__class__):
            return __o.value == self.value
        else:
            return __o == self.value

    def __str__(self) -> str:
        return "{}".format(self.value)


class BinaryTreeNode:
    
    def __init__(self, value=None) -> None:
        self.value = value
        self.__parent_node = None
        self.__left_node = None
        self.__left_tag = False # False为孩子,True为线索
        self.__right_node = None
        self.__right_tag = False 

    @property
    def parent_node(self):
        return self.__parent_node

    @parent_node.setter
    def parent_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__parent_node = node
        else:
            raise TypeError("必须是BinaryTreeNode")
        
    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__left_node = node
            if node:
                node.parent_node = self
        else:
            raise TypeError("必须是BinaryTreeNode")

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__right_node = node
            if node:
                node.parent_node = self
        else:
            raise TypeError("必须是BinaryTreeNode")
    
    @property
    def left_tag(self):
        return self.__left_tag

    @left_tag.setter
    def left_tag(self, tag):
        if tag in (True, False):
            self.__left_tag = tag
        else:
            raise TypeError("必须是bool")
    
    @property
    def right_tag(self):
        return self.__right_tag

    @right_tag.setter
    def right_tag(self, tag):
        if tag in (True, False):
            self.__right_tag = tag
        else:
            raise TypeError("必须是bool")

    def __str__(self) -> str:
        return "{}".format(self.value)


class HuffmanNode():

    def __init__(self, value=None, weight=0) -> None:
        self.value = value
        self.code = None
        self.__weight = weight
        self.__left_node = None
        self.__right_node = None

    @property
    def weight(self):
        return self.__weight
    
    @property
    def left_node(self):
        return self.__left_node
    
    @left_node.setter
    def left_node(self, node):
        if isinstance(node, self.__class__):
            self.__left_node = node
        else:
            raise TypeError("必须是HuffmanNode")

    @property
    def right_node(self):
        return self.__right_node
    
    @right_node.setter
    def right_node(self, node):
        if isinstance(node, self.__class__):
            self.__right_node = node
        else:
            raise TypeError("必须是HuffmanNode")

    
class AdjacencyNode:

    def __init__(self, value=None, weight=0) -> None:
        self.__value = value
        self.__next_node = None
        self.__weight = weight

    @property
    def value(self):
        return self.__value
    
    @property
    def weight(self):
        return self.__weight
    
    @property
    def next_node(self):
        return self.__next_node
    
    @next_node.setter
    def next_node(self, node):
        if isinstance(node, self.__class__):
            self.__next_node = node
        else:
            raise TypeError("必须是AdjacencyNode")

    def __str__(self) -> str:
        return str(self.value)


class OrthogonalNode:

    def __init__(self, value=None) -> None:
        self.value = value
        self.__tlink = None
        self.__hlink = None

    @property
    def tlink(self):
        return self.__tlink

    @tlink.setter
    def tlink(self, link):
        if isinstance(link, OrthogonalLink):
            self.__tlink = link
        else:
            raise TypeError("必须是OrthogonalLink")
    
    @property
    def hlink(self):
        return self.__hlink

    @hlink.setter
    def hlink(self, link):
        if isinstance(link, OrthogonalLink):
            self.__hlink = link
        else:
            raise TypeError("必须是OrthogonalLink")

    def __str__(self) -> str:
        return str(self.value)


class OrthogonalLink:

    def __init__(self, tail:OrthogonalNode, head:OrthogonalNode, weight:int=0) -> None:
        if isinstance(tail, OrthogonalNode) and isinstance(head, OrthogonalNode):
            self.__tnode = tail
            self.__hnode = head
        else:
            raise TypeError("弧首尾应为OrthogonalNode")
        
        self.__hlink = None
        self.__tlink = None
        self.__weigth = weight

    @property
    def tnode(self):
        return self.__tnode

    @property
    def hnode(self):
        return self.__hnode
    
    @property
    def tlink(self):
        return self.__tlink 

    @tlink.setter
    def tlink(self, link):
        if isinstance(link, self.__class__):
            self.__tlink = link
        else:
            raise TypeError("弧尾指向的边应为OrthogonalLink")

    @property
    def hlink(self):
        return self.__hlink

    @hlink.setter
    def hlink(self, link):
        if isinstance(link, self.__class__):
            self.__hlink = link
        else:
            raise TypeError("弧首指向的边表应为OrthogonalLink")

    @property
    def weight(self):
        return self.__weigth

    def __str__(self) -> str:
        return str(self.__weigth)


class BTreeNode:

    def __init__(self, n=0, isleaf=True) -> None:
        # n:结点包含关键字的数量 isleaf:是否为叶子结点
        self.n = n
        self.keys = list()
        self.children = list()
        self.isleaf = isleaf

    def __str__(self) -> str:
        return_str = "keys:["
        for i in range(self.n):
            return_str += str(self.keys[i]) + ' '
        return_str += "];children:["
        for child in self.children:
            return_str += str(child) + ';'
        return_str += ']\r\n'
        return return_str

    @staticmethod
    def allocate_node(key_max:int):
        node = BTreeNode()
        for i in range(key_max):
            node.keys.append(None)
        for i in range(key_max+1):
            node.children.append(None)
        return node

    def disk_read(self):
        pass

    def disk_write(self):
        pass


class RBTreeNode:

    def __init__(self, value=None, color=True) ->None:
        self.value = value
        self.__parent_node = None
        self.__color = color # True:Red,Fasle:Black
        self.__left_node = None
        self.__right_node = None

    @property
    def parent_node(self):
        return self.__parent_node

    @parent_node.setter
    def parent_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__parent_node = node
        else:
            raise TypeError("必须是RBTreeNode")
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value:bool):
        if isinstance(value, bool):
            self.__color = value
        else:
            raise TypeError("必须是bool")
        
    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__left_node = node
            if node:
                node.parent_node = self
        else:
            raise TypeError("必须是RBTreeNode")

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        if isinstance(node, self.__class__) or node is None:
            self.__right_node = node
            if node:
                node.parent_node = self
        else:
            raise TypeError("必须是RBTreeNode")

    def __str__(self) -> str:
        return "{}".format(self.value)

