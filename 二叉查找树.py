from structure import BinarySearchTree
from util import util



if __name__ == "__main__":
    data = [70,105,115,104,67,46,99,111,109]
    # search_tree = util.build_binary_search_tree(data)
    search_tree = BinarySearchTree(data)
    # print( util.inorder_traverse(search_tree) )

    search_tree.append(96)
    # print( util.inorder_traverse(search_tree) )
    print( util.floororder_traverse(search_tree) )
    # print(search_tree.have(96))
    
    search_tree.remove(70)
    # print( util.inorder_traverse(search_tree) )
    print( util.floororder_traverse(search_tree) )