from node import BinaryTreeNode
    

def create_tree(data:list) -> BinaryTreeNode:
    
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
    

def inorder_threading(tree:BinaryTreeNode) -> BinaryTreeNode:

    def threading(node:BinaryTreeNode):
        nonlocal pre_node
        # 访问二叉树结点的具体操作
        if node:
            threading(node.left_node)
            if node.left_node is None:
                node.left_tag = True
                node.left_node = pre_node
            if pre_node.right_node is None:
                pre_node.right_tag = True
                pre_node.right_node = node
            pre_node = node
            threading(node.right_node)

    head_node = BinaryTreeNode()
    head_node.right_tag = True
    head_node.right_node = head_node
    if tree is None:
        head_node.left_node = head_node
    else:
        head_node.left_node = tree
        pre_node = head_node
        threading(tree)
        pre_node.right_tag = True
        pre_node.right_node = head_node
        head_node.right_node = pre_node
    return head_node


def inorder_traverse(tree:BinaryTreeNode) -> list:

    def visit(node:BinaryTreeNode):
        nonlocal nodes
        nodes.append(node)
        print("value:{}".format(node))
    
    nodes = list()
    node = tree.left_node
    while node is not tree:
        while not node.left_tag :
            node = node.left_node
        visit(node)
        while node.right_tag and node.right_node is not tree:
            node = node.right_node
            visit(node)
        node = node.right_node
    return nodes


if __name__ == "__main__":
    data0 = ['A','B',None,'D',None,'C','E',None,None,None]
    data1 = ['A','B','C',None,None,'D',None,None,'E',None,'F',None,None]
    tree = create_tree(data1)
    # preorder_traverse(tree, 1)
    tree = inorder_threading(tree)
    
    nodes = inorder_traverse(tree)
    for node in nodes:
        print("value:{}".format(node.value))
