from node import LinkedListNode, BinaryTreeNode, HuffmanNode, AdjacencyNode, OrthogonalNode, OrthogonalLink, RBTreeNode
# 结构
class LinkedList:
    def __init__(self, items=None) -> None:
        self.__head_node = LinkedListNode()
        self.__tail_node = self.__head_node
        self.__length = 0
        self.__iter_node = self.__head_node
        if hasattr(items, "__iter__"):
            for item in items:
                self.append(item)

    def __len__(self) -> int:
        return self.__length

    def append(self, value) -> None:
        self.__tail_node.next_node = LinkedListNode(value)
        self.__tail_node.next_node.last_node = self.__tail_node
        self.__tail_node = self.__tail_node.next_node
        self.__length += 1

    def insert(self, index:int, value) -> None:
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length:
            raise IndexError("索引超出LinkedList范围")
        elif index < 0:
            raise ValueError("只允许正向插入")
        temp:LinkedListNode = self.__head_node
        for _ in range(index):
            temp = temp.next_node
        temp.next_node.last_node = LinkedListNode(value)
        temp.next_node.last_node.next_node = temp.next_node
        temp.next_node.last_node.last_node = temp
        temp.next_node = temp.next_node.last_node
        self.__length += 1

    def at(self, index:int):
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length or -index > self.__length:
            raise IndexError("索引超出LinkedList范围")
        if index > self.__length // 2:
            index -= self.__length
        elif index < self.__length // -2:
            index += self.__length
        if index >= 0:
            temp:LinkedListNode = self.__head_node.next_node
            for _ in range(index):
                temp = temp.next_node
        else:
            temp:LinkedListNode = self.__tail_node
            for _ in range(-index-1):
                temp = temp.last_node
        return temp.value

    def index(self, value) -> int or None:
        temp:LinkedListNode = self.__head_node.next_node
        index = 0
        while temp is not None and temp.value != value:
            temp = temp.next_node
            index += 1
        return None if index == self.__length else index 

    def __iter__(self):
        temp:LinkedListNode = self.__head_node.next_node
        while temp is not None:
            yield temp.value
            temp = temp.next_node

    def __next__(self):
        if self.__iter_node.next_node is not None:
            self.__iter_node = self.__iter_node.next_node
            return self.__iter_node.value
        else:
            self.__iter_node = self.__head_node
            raise StopIteration

    def __getitem__(self, index:int):
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length or -index > self.__length:
            raise IndexError("索引超出LinkedList范围")
        if index > self.__length // 2:
            index -= self.__length
        elif index < self.__length // -2:
            index += self.__length
        if index >= 0:
            temp:LinkedListNode = self.__head_node.next_node
            for _ in range(index):
                temp = temp.next_node
        else:
            temp:LinkedListNode = self.__tail_node
            for _ in range(-index-1):
                temp = temp.last_node
        return temp.value

    def __setitem__(self, index:int, value) -> None:
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length or index < 0:
            raise IndexError("索引超出LinkedList范围")
        if index > self.__length // 2:
            index -= self.__length
        elif index < self.__length // -2:
            index += self.__length
        if index >= 0:
            temp:LinkedListNode = self.__head_node.next_node
            for _ in range(index):
                temp = temp.next_node
        else:
            temp:LinkedListNode = self.__tail_node
            for _ in range(-index-1):
                temp = temp.last_node
        temp.value = value

    def __delitem__(self, index:int)->None:
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length or -index > self.__length:
            raise IndexError("索引超出LinkedList范围")
        if index > self.__length // 2:
            index -= self.__length
        elif index < self.__length // -2:
            index += self.__length
        if index >= 0:
            temp:LinkedListNode = self.__head_node
            for _ in range(index):
                temp = temp.next_node
        else:
            temp:LinkedListNode = self.__tail_node
            for _ in range(-index):
                temp = temp.last_node
        temp.next_node = temp.next_node.next_node
        t = temp.next_node.last_node
        temp.next_node.last_node = None
        del t
        if temp.next_node is not None:
            temp.next_node.last_node = temp
        else:
            self.__tail_node = temp
        self.__length -= 1

    def remove(self, index:int) -> None:
        if not isinstance(index, int):
            raise TypeError("索引必须是int")
        if index >= self.__length or -index > self.__length:
            raise IndexError("索引超出LinkedList范围")
        if index > self.__length // 2:
            index -= self.__length
        elif index < self.__length // -2:
            index += self.__length
        if index >= 0:
            temp:LinkedListNode = self.__head_node
            for _ in range(index):
                temp = temp.next_node
        else:
            temp:LinkedListNode = self.__tail_node
            for _ in range(-index):
                temp = temp.last_node
        temp.next_node = temp.next_node.next_node  
        if temp.next_node is not None:
            t = temp.next_node.last_node
            temp.next_node.last_node = None
            del t
            temp.next_node.last_node = temp
        else:
            self.__tail_node = temp
        self.__length -= 1

    def reverse(self) -> None:
        if self.__length == 0:
            return
        temp_node = self.__head_node.next_node
        while temp_node is not None and temp_node.next_node is not None:
            next_node = temp_node.next_node
            temp_node.next_node = temp_node.last_node
            temp_node.last_node = next_node
            temp_node = next_node
        self.__tail_node = self.__head_node.next_node
        self.__tail_node.next_node = None
        temp_node.last_node.last_node = temp_node
        temp_node.next_node = temp_node.last_node
        temp_node.last_node = self.__head_node
        self.__head_node.next_node = temp_node

    def __reversed__(self):
        node = self.__tail_node.last_node
        while node is not None:
            yield node.next_node.value
            node = node.last_node

    def clear(self) -> None:
        while self.__tail_node.last_node is not None:
            self.__tail_node = self.__tail_node.last_node
            temp = self.__tail_node.next_node
            self.__tail_node.next_node = None
            del temp
        self.__length = 0

    def copy(self):
        ls = LinkedList()
        temp:LinkedListNode = self.__head_node.next_node
        while temp is not None:
            ls.append(temp.value)
            temp = temp.next_node
        return ls

    def __str__(self) -> str:
        return str(list(self))


class Huffman():

    def __init__(self, s:str) -> None:
        self.__weights = self.__get_weights(s)
        self.__buffer = [b' ' for _ in range(round(len(self.__weights)))]
        self.__tree = self.__build_huffman_tree(self.__weights)
        self.__code = self.__build_code(self.__tree)

    @property
    def weights(self):
        return self.__weights

    @property
    def tree(self):
        return self.__tree

    @property
    def code(self):
        return self.__code

    def __get_weights(self, s:str) -> dict:
        weights = dict()
        for i in s:
            weights[i] = weights.get(i, 0)+1
        return weights
    
    def __build_huffman_tree(self, weights:dict):
        nodes = [HuffmanNode(value, weight) for value,weight in weights.items()]
        while len(nodes) > 1:
            nodes.sort(key=lambda node:node.weight, reverse=True)
            c = HuffmanNode(value=None, weight=(nodes[-1].weight+nodes[-2].weight))
            c.left_node = nodes.pop()
            c.right_node = nodes.pop()
            nodes.append(c)
        return nodes[0]

    def __build_code(self, tree):
        
        def func(tree:HuffmanNode, length:int):
            nonlocal code, self
            node = tree
            if not node:
                return
            elif node.value:
                code[node.value] = b''.join( self.__buffer[:length] )
                return
            self.__buffer[length] = b'0'
            func(node.left_node, length+1)
            self.__buffer[length] = b'1'
            func(node.right_node, length+1)
        
        code = dict()
        func(tree, 0)
        return code


class AdjacencyList():
    def __init__(self, ls=list()) -> None:
        if isinstance(ls, list):
            self.node_list = ls
        else:
            raise TypeError("AdjacencyList初始化值必须是list")


    def build_from_adjacency_mat(self, mat):
        for i in range(len(mat)):
            temp = self.node_list[i]
            for j in range(len(mat)):
                if mat[i][j] > 0:
                    temp.next_node = AdjacencyNode(self.node_list[j], mat[i][j])
                    temp = temp.next_node

    @property
    def adjacencu_mat(self) -> list:
        mat = [[0 for _ in range(len(self.node_list))] for _ in range(len(self.node_list))]
        for node in self.node_list:
            temp = node.next_node
            while temp:
                mat[self.node_list.index(node)][self.node_list.index(temp.value)] = 1
                temp = temp.next_node
        return mat

    def show(self):
        print("--"*len(self.node_list))
        for node in self.node_list:
            print("{}:".format(node), end=' ')
            temp = node.next_node
            if temp:
                while temp:
                    print("({},{})".format(temp,temp.weight), end=' ')
                    temp = temp.next_node
            else:
                print("None", end=' ')
            print()
        print("--"*len(self.node_list))

    def dfs(self, start:int) -> list:
    
        def func(node:AdjacencyNode):
            nonlocal marks
            temp = node.next_node
            while temp:
                if temp.value not in marks:
                    marks.append(temp.value)
                    func(temp.value)
                temp = temp.next_node

        marks = [self.node_list[start]]
        func(self.node_list[start])
        return [node.value for node in marks]

    def bfs(self, start:int) -> list:
        temp1 = [self.node_list[start]]
        marks = [self.node_list[start]]
        while temp1:
            lay = list()
            for node in temp1:
                temp2 = node.next_node
                while temp2: 
                        if temp2.value not in marks:
                            lay.append( temp2.value )
                            marks.append( temp2.value )
                        temp2 = temp2.next_node
            temp1 = lay
        return [ node.value for node in marks]

    def __len__(self):
        return len(self.node_list)

    def __contains__(self, item):
        return item in self.node_list

    def __getitem__(self, item) -> list or AdjacencyNode:
        if isinstance(item, slice) or isinstance(item, int):
            return self.node_list[item]
        else:
            raise ValueError

    def __iter__(self):
        return iter(self.node_list)
    
    def __str__(self) -> str:
        return str([node.__str__() for node in self.node_list])


class OrthogonalList:

    def __init__(self, nodes:list) -> None:
        if isinstance(nodes, list): 
            self.node_list = nodes
        else:
            raise TypeError("OrthogonlList初始化值必须是list")
        self.__link_list = list()

    def build_from_mat(self, m:list):
        shape = len(m)
        for i in range(shape):
            temp = self.node_list[i]
            for j in range(shape):
                if m[i][j] > 0 : 
                    self.__link_list.append(OrthogonalLink(self.node_list[i], self.node_list[j], m[i][j]))
                    temp.tlink = self.__link_list[-1]
                    temp = temp.tlink
        for j in range(shape):
            temp = self.node_list[j]
            for i in range(shape):
                if m[i][j] > 0:
                    for link in self.__link_list:
                        if link.tnode is self.node_list[i] and link.hnode is self.node_list[j]:
                            temp.hlink = link
                            temp = temp.hlink
                            break
    
    def dfs(self, start:int) -> list:
      
        def func(node:OrthogonalNode):
                nonlocal marks
                temp = node.tlink
                while temp:
                    if temp.hnode not in marks:
                        marks.append(temp.hnode)
                        func(temp.hnode)
                    temp = temp.tlink

        marks = [ self.node_list[start] ]
        func(self.node_list[start])
        return [ node.value for node in marks ]

    def bfs(self, start:int) -> list:
        temp0 = [ self.node_list[start] ]
        marks = [ self.node_list[start] ]
        while temp0:
            lay = list()
            for node in temp0:
                temp1 = node.tlink
                while temp1:
                    if temp1.hnode not in marks:
                        lay.append( temp1.hnode )
                        marks.append( temp1.hnode )
                    temp1 = temp1.tlink
            temp0 = lay    
        return [ node.value for node in marks ]

    @property
    def link_list(self):
        return self.__link_list

    @property
    def adjacencu_mat(self) -> list:
        mat = [[0 for _ in range(len(self.node_list))] for _ in range(len(self.node_list))]
        for node in self.node_list:
            temp = node.tlink
            while temp:
                mat[self.node_list.index(node)][self.node_list.index(temp.hnode)] = temp.weight
                temp = temp.tlink
        return mat

    def __len__(self):
        return len(self.node_list)

    def __contains__(self, item):
        return item in self.node_list

    def __getitem__(self, item) -> list or AdjacencyNode:
        if isinstance(item, slice) or isinstance(item, int):
            return self.node_list[item]
        else:
            raise ValueError("必须是索引")

    def __iter__(self):
        return iter(self.node_list)
    
    def __str__(self) -> str:
        return str([node.__str__() for node in self.node_list])


class AOENetwork(AdjacencyList):

    def __init__(self, ls=list()) -> None:
        super().__init__(ls=ls)
        self.__indegree_list = [0 for _ in range(len(self.node_list))]
        self.__sorted_nodes = list()
        self.__critical_path_weights = None

    def build_from_adjacency_mat(self, mat) -> list:
        for i in range(len(mat)):
            temp = self.node_list[i]
            for j in range(len(mat)):
                if mat[i][j] > 0:
                    temp.next_node = AdjacencyNode(self.node_list[j], mat[i][j])
                    temp = temp.next_node
                    self.__indegree_list[j] += 1

    @property
    def indegree_list(self):
        return self.__indegree_list

    @property
    def critical_path_weights(self):
        if self.__critical_path_weights is None:
            self.critical_path()
        return self.__critical_path_weights

    def topological_sort(self) -> list:
        indegrees = [degree for degree in self.indegree_list]
        self.__sorted_nodes.clear()
        length = len(self.node_list)
        while len(self.__sorted_nodes) < length:
            for i in range(length):
                if indegrees[i] == 0 and self.node_list[i] not in self.__sorted_nodes:
                    self.__sorted_nodes.append(self.node_list[i])
                    node = self.node_list[i].next_node
                    break
            while node:
                indegrees[ self.node_list.index(node.value) ] -= 1
                node = node.next_node
        return [node.value for node in self.__sorted_nodes]

    def critical_path(self) -> list:
        if not self.__sorted_nodes :
            self.topological_sort()
        length = len(self.node_list)
        
        etv = [0] * length
        for i in range(length):
            edge = self.__sorted_nodes[i].next_node
            while edge:
                if etv[i] + edge.weight  > etv[self.__sorted_nodes.index(edge.value)]:
                    etv[self.__sorted_nodes.index(edge.value)] = etv[i] + edge.weight
                edge = edge.next_node
        
        ltv = [etv[-1]] * length
        for i in range(length-2,-1,-1):
            edge = self.__sorted_nodes[i].next_node
            while edge:
                if ltv[self.__sorted_nodes.index(edge.value)] - edge.weight  < ltv[i]:
                    ltv[i] = ltv[self.__sorted_nodes.index(edge.value)] - edge.weight
                edge = edge.next_node
        
        nodes = [self.__sorted_nodes[0]] # 存放某一条关键路径上的结点
        self.__critical_path_weights = 0
        paths = list() # 存放可视化的关键路径
        for i in range(length):
            edge = self.__sorted_nodes[i].next_node
            while edge:
                ete = etv[i]
                lte = ltv[self.__sorted_nodes.index(edge.value)] - edge.weight
                if ete == lte:
                    paths.append((self.__sorted_nodes[i].value, edge.value.value, edge.weight))
                if nodes[-1] is self.__sorted_nodes[i]:
                    nodes.append(nodes)
                    self.__critical_path_weights += edge.weight
                edge = edge.next_node
        return paths


class BinarySearchTree:

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
        if isinstance(node, BinaryTreeNode) or node is None:
            self.__head_node = node
        else:
            raise TypeError("必须是BinaryTreeNode")
        
    @property
    def value(self):
        return self.__head_node.value

    @property
    def left_node(self):
        return self.__head_node.left_node 

    @property
    def right_node(self):
        return self.__head_node.right_node

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
        if node is None: return False
        if node.right_node is None:
            if node is node.parent_node.left_node:
                node.parent_node.left_node = node.left_node
            else:
                node.parent_node.right_node = node.left_node
            del node    
        elif node.left_node is None:
            if node.parent_node.left_node is node:
                node.parent_node.left_ndoe = node.right_node
            else:
                node.parent_node.right_ndoe = node.right_node
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
            del temp
        return True


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
        if isinstance(node, BinaryTreeNode) or node is None:
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
        if node is None: return False
        if node.right_node is None:
            if node is node.parent_node.left_node:
                node.parent_node.left_node = node.left_node
            else:
                node.parent_node.right_node = node.left_node
            check_node = self.__minimum_unbalanced_tree(node)
            self.__balance(check_node)
            del node    
        elif node.left_node is None:
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


class RBTree:

    def __init__(self, value=[None]) -> None:
        self.__head_node = RBTreeNode(color=False)
        if isinstance(value, list):
            self.build_from_data(value)
        else:
            raise TypeError("BinarySearchTree初始化值必须是list")
    
    @property
    def head_node(self):
        return self.__head_node

    @head_node.setter
    def head_node(self, node):
        if isinstance(node, RBTreeNode) or node is None:
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

    def __right_rotate(self, node:RBTreeNode): # 向右旋转 
        parent:RBTreeNode = node.parent_node
        left:RBTreeNode = node.left_node    
        node.left_node = left.right_node
        left.right_node = node
        if node is self.__head_node: 
            self.__head_node = left 
        elif parent.left_node is node:
            parent.left_node = left
        else:
            parent.right_node = left

    def __left_rotate(self, node:RBTreeNode): # 向左旋转 
        parent:RBTreeNode = node.parent_node
        right:RBTreeNode = node.right_node    
        node.right_node = right.left_node
        right.left_node = node
        if node is self.__head_node: 
            self.__head_node = right
        elif parent.left_node is node:
            parent.left_node = right
        else:
            parent.right_node = right

    def append(self, value) -> bool:
        node = self.__head_node
        while node:
            temp:RBTreeNode = node
            if node.value < value:
                node = node.right_node
            elif node.value > value:
                node = node.left_node 
            else:
                return False
        if temp.value > value:
            temp.left_node = RBTreeNode(value, True) 
            if temp.parent_node.color: self.__insert_fixup(temp.left_node)           
        else:
            temp.right_node = RBTreeNode(value, True)
            if temp.parent_node.color: self.__insert_fixup(temp.right_node)
        return True

    def __insert_fixup(self, node:RBTreeNode):
        while node.parent_node.color:
            # 父结点是祖父结点的左孩子
            if node.parent_node is node.parent_node.parent_node.left_node:
                uncle:RBTreeNode = node.parent_node.parent_node.right_node
                if uncle and uncle.color:
                    node.parent_node.color = False
                    uncle.color = False
                    node.parent_node.parent_node.color = True
                    node = node.parent_node.parent_node
                elif (not uncle or not uncle.color) and node is node.parent_node.right_node: # LR
                    node = node.parent_node
                    self.__left_rotate(node)
                elif (not uncle or not uncle.color) and node is node.parent_node.left_node: # LL
                    node.parent_node.color = False
                    node.parent_node.parent_node.color = True
                    self.__right_rotate(node.parent_node.parent_node)
            else: # 父结点是祖父结点的右孩子
                uncle:RBTreeNode = node.parent_node.parent_node.left_node
                if uncle and uncle.color:
                    node.parent_node.color = False
                    uncle.color = False
                    node.parent_node.parent_node.color = True
                    node = node.parent_node.parent_node
                elif (not uncle or not uncle.color) and node is node.parent_node.right_node: # RL
                    node = node.parent_node
                    self.__left_rotate(node)
                elif (not uncle or not uncle.color) and node is node.parent_node.left_node: # RR
                    node.parent_node.color = False
                    node.parent_node.parent_node.color = True
                    self.__right_rotate(node.parent_node.parent_node)
        self.__head_node.color = False

    def __delete_fixup(self, node:RBTreeNode):
        while node is not self.__head_node and not node.color:
            if node is node.parent_node.left_node:
                uncle:RBTreeNode = node.parent_node.right_node
                if uncle.color:
                    uncle.color = False
                    node.parent_node.color = True
                    self.__left_rotate(node.parent_node)
                else:
                    if not uncle.left_node.color and not uncle.right_node.color:
                        uncle.color = True
                        node = node.parent_node
                    elif uncle.left_node.color and not uncle.right_node.color:
                        uncle.left_node.color = False
                        uncle.color = True
                        self.__right_rotate(uncle)
                    else:
                        uncle.color = node.parent_node.color
                        node.parent_node.color = False
                        uncle.right_node.color = False
                        self.__left_rotate(node.parent_node)
                        node = self.__head_node     
            else:
                uncle:RBTreeNode = node.parent_node.left_node
                if uncle.color:
                    uncle.color = False
                    node.parent_node.color = True
                    self.__right_rotate(node.parent_node)
                else: 
                    if not uncle.left_node.color and not uncle.right_node.color:
                        uncle.color = True
                        node = node.parent_node
                    elif uncle.left_node.color and not uncle.right_node.color:
                        uncle.right_node.color = False
                        uncle.color = True
                        self.__left_rotate(uncle)
                    else:
                        uncle.color = node.parent_node.color
                        node.parent_node.color = False
                        uncle.left_node.color = False
                        self.__right_rotate(node.parent_node)
                        node = self.__head_node 
        node.color = False


