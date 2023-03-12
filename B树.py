from os import chdir
from node import BTreeNode

class BTree:

    def __init__(self, m=3) -> None:
        # B树的最小度数
        self.m = m
        # 结点包含关键字的最大个数
        self.key_max = 2*self.m-1
        # 非根结点包含关节子的最小个数
        self.key_min = self.m - 1
        # 子结点的最大个数
        self.child_max = self.key_max+1
        # 子结点的最小个数
        self.child_min = self.key_min+1
        # 根结点
        self.root:BTreeNode = None

    def __new_node(self):
        return BTreeNode.allocate_node(self.key_max)

    def append(self, key):
        if self.contain(key): return False
        if self.root is None:
            self.root = self.__new_node()
            self.root.disk_write()
        elif self.root.n == self.key_max:
            parent = self.__new_node()
            parent.isleaf = False
            parent.children[0] = self.root
            self.__split_child(parent, 0, self.root)
            self.root = parent
        self.__append_non_full(self.root, key)
        return True

    def remove(self, key):
        if not self.search(self.root, key): return False
        # 特殊情况处理
        if self.root.n == 1:
            if self.root.isleaf: 
                self.clear()
            else:
                child_1 = self.root.children[0]
                child_2 = self.root.children[1]
                if child_1.n == self.key_min and child_2.n == self.key_min:
                    self.__merge_child(self.root, 0)
                    self.__delete_node(self.root)
                    self.root = child_1
        self.__recursive_remove(self.root, key)
        return True

    def display(self):
        self.__display_in_concavo(self.root, self.key_max*10)
    
    def contain(self, key) -> bool:
        return self.__search(self.root, key)

    def clear(self):
        self.__recursive_clear(self.root)
        del self.root
        self.root = None

    def __recursive_clear(self, node:BTreeNode):
        if node is not None:
            if not node.isleaf:
                for i in range(node.n):
                    self.__recursive_clear(node.children[i]) 
            self.__delete_node(node)
    
    def __delete_node(self, node:BTreeNode):
        if node is not None:
            del node
            node = None

    def __search(self, node:BTreeNode, key):
        if node is None:
            return False
        else:
            i = 0
            while i<node.n and key>node.keys[i]:
                i += 1
            if i<node.n and key == node.keys[i]:
                return True
            else:
                if node.isleaf:
                    return False
                else:
                    return self.__search(node.children[i], key)

    def __split_child(self, parent:BTreeNode, child_index:int, child:BTreeNode):
        # 将child分裂成child和right_node两个结点
        right_node = self.__new_node()
        right_node.isleaf = child.isleaf
        right_node.n = self.key_min
        # 拷贝关键字的值
        for i in range(self.key_min):
            right_node.keys[i] = child.keys[i+self.child_min]
        # 如果不是叶子结点,就拷贝孩子结点的指针
        if not child.isleaf:
            for i in range(self.child_min):
                right_node.children[i] = child.children[i+self.child_min]
        # 更新左子树的关键字个数
        child.n = self.key_min
        # 将父节点中的child_index后的所有关键字的值和子树指针向后移动一位
        for i in range(child_index, parent.n):
            j = parent.n + child_index - i
            parent.children[j+1] = parent.children[i]
            parent.keys[j] = parent.keys[j-1]
        # 更新父结点的关键字个数
        parent.n += 1
        # 存储右子树指针
        parent.children[child_index+1] = right_node
        # 把结点的中间值提到父结点
        parent.keys[child_index] = child.keys[self.key_min]
        child.disk_write()
        right_node.disk_write()
        parent.disk_write()

    def __append_non_full(self, node:BTreeNode, key):
        i = node.n
        if node.isleaf: # node是叶子结点
            while i>0 and key<node.keys[i-1]:
                node.keys[i] = node.keys[i-1]
                i -= 1
            node.keys[i] = key
            node.n += 1
            node.disk_write()
        else: # node是内结点
            while i>0 and key<node.keys[i-1]:
                i -= 1
            child = node.children[i]
            child.disk_read() 
            if child.n == self.key_max:
                self.__split_child(node, i, child)
                if key > node.keys[i]:
                    child = node.children[i-1]
            self.__append_non_full(child, key)

    def __display_in_concavo(self, node:BTreeNode, count):
        if node is not None:
            for i in range(node.n):
                if not node.isleaf:
                    self.__display_in_concavo(node.children[i], count-2)
                for j in range(-1, count):
                    # k = count - j - 1
                    print('-', end='')
                print(node.keys[i])
            if not node.isleaf:
                self.__display_in_concavo(node.children[i], count-2)

    def __merge_child(self, parent:BTreeNode, index:int):
        child_1:BTreeNode = parent.children[index]
        child_2:BTreeNode = parent.children[index+1]
        # 将child_2合并到child_1
        child_1.n = self.key_max
        # 将父结点index的值下移
        child_1.keys[self.key_min] = parent.keys[index]
        for i in range(self.key_min):
            child_1.keys[i+self.key_min+1] = child_2.keys[i]
        if not child_1.isleaf:
            for i in range(self.child_min):
                child_1.children[i+self.child_min] = child_2.children[i]
        # 父结点删除index的key,index后的往前移一位
        parent.n -= 1
        for i in range(index, parent.n):
            parent.keys[i] = parent.keys[i+1]
            parent.children[i+1] = parent.children[i+2]
        self.__delete_node(child_2)

    def __recursive_remove(self, node:BTreeNode, key):
        i = 0
        while i<node.n and key>node.keys[i]:
            i += 1
        # 关键字key在结点node
        if i<node.n and key==node.keys[i]:
            if node.isleaf: # node是叶结点
                for j in range(i, node.n):
                    node.keys[j] = node.keys[j+1]
                node.keys[j+1] = None
                return
            else: # node是内结点
                prev_child = node.children[i] # 结点node中前于key的子结点
                next_child = node.children[i+1] # 结点node中后于key的子结点
                if prev_child.n >= self.child_min:
                    # 获取key的前驱关键字
                    prev_key = self.predecessor(prev_child)
                    self.__recursive_remove(prev_child, prev_key)
                    # 替换成key的前驱关键字
                    node.keys[i] = prev_key
                    return
                elif next_child.n >= self.child_min:
                    next_key = self.successor(next_child)
                    self.__recursive_remove(next_child, next_key)
                    node.keys[i] = next_key
                    return
                else:
                    self.__merge_child(node, i)
                    self.__recursive_remove(prev_child, key)
        # 关键字key不在结点node中
        else:
            # 包含key的子树根结点
            child:BTreeNode = node.children[i]
            if child.n == self.key_max:
                left:BTreeNode = node.children[i-1] if i>0 else None
                right:BTreeNode = node.children[i+1] if i<node.n else None
                if left is not None and left.n >= self.child_min:
                    # 父结点中i-1的关键字下移至child中
                    for j in range(child.n):
                        k = child.n - j
                        child.keys[k] = child.keys[k-1]
                    child.keys[0] = node.keys[i-1]
                    if not left.isleaf:
                        # left结点中合适的孩子指针移到child中
                        for j in range(child.n+1):
                            k = child.n + 1 - j
                            child.children[k] = child.children[k-1]
                        child.children[0] = left.children[left.n]
                    child.n += 1
                    node.keys[i] = left.keys[left.n-1]
                    left.n -= 1
                elif right is not None and right.n >= self.child_min:
                    # 父结点中i的关键字下移至child中
                    child.keys[child.n] = node.keys[i]
                    child.n += 1
                    node.keys[i] = right.keys[0]
                    right.n -= 1
                    for j in range(right.n):
                        right.keys[j] = right.keys[j+1]
                    if not right.isleaf:
                        # right结点中合适的孩子指针移到child中
                        child.children[child.n] = right.children[0]
                        for j in range(right.n):
                            right.children[j] = right.children[j+1]
                # 左右兄弟结点都只包含child_min-1个结点
                elif left is not None:
                    self.__merge_child(node, i-1)
                    child = left
                elif right is not None:
                    self.__merge_child(node, i)
            self.__recursive_remove(child, key)

    def predecessor(self, node:BTreeNode):
        while not node.isleaf:
            node = node.children[node.n]
        return node.keys[node.n-1]

    def successor(self, node:BTreeNode):
        while not node.isleaf:
            node = node.children[0]
        return node.keys[0]


if __name__ == "__main__":
    tree = BTree(3)
    tree.append(11)
    tree.append(3)
    tree.append(1)
    tree.append(4)
    tree.append(33)
    tree.append(13)
    tree.append(63)
    tree.append(43)
    tree.append(2)
    print(tree.root)
    tree.display()
    tree.clear()
    tree = BTree(2)
    tree.append(11)
    tree.append(3)
    tree.append(1)
    tree.append(4)
    tree.append(33)
    tree.append(13)
    tree.append(63)
    tree.append(43)
    tree.append(2)
    print(tree.root)
    tree.display()