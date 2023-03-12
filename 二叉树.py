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
    
        
def preorder_traverse(tree:BinaryTreeNode) -> list:
    
    def func(node:BinaryTreeNode):
        nonlocal ans
        if node:
            ans.append(node.value)
            # print("value:{}".format(node))
            func(node.left_node)
            func(node.right_node)
    
    ans = list()    
    func(tree)
    return ans

def floororder_traverse(tree:BinaryTreeNode):
    
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



if __name__ == "__main__":
    data0 = ['A','B',None,'D',None,'C','E',None,None,None]
    data1 = ['A','B','C',None,None,'D',None,None,'E',None,'F','G',None,None,'H',None,None]
    tree = create_tree(data1)
    print(preorder_traverse(tree))
    print(floororder_traverse(tree))