from node import HuffmanNode


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


if __name__ == "__main__":
    s = "aabbccdddeefgenajojfonadkjfwqnioaerweggrefdsfassasdfgr"

    huffman = Huffman(s)

    print(huffman.weights)
    print(huffman.code)