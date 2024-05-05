class Pair:
    def _init_(self,key,value):
        self.key=key
        self.value=value
class Node:
    def _init_(self, Pair):
        self.left = None
        self.right = None
        self.Pair = Pair

def insert(root, pair):
    # Start at the root node
    current_node = root
    while True:
        # If the key is more important (higher priority), it goes to the right
        if pair.value < current_node.Pair.value:
            # If no right child, place it here
            if not current_node.right:
                current_node.right = Node(pair)
                #print(f"current node {pair.key}, its parent is {current_node.Pair.key}")
                break
            else:
                current_node = current_node.right
        # If the key is less important (lower priority), it goes to the left
        else:
            # If no left child, place it here
            if not current_node.left:
                current_node.left = Node(pair)
                #print(f"current node {pair.key}, its parent is {current_node.Pair.key}")
                break
            else:
                current_node = current_node.left

def inorder_traversal(node, graph_lines):
    # Base case
    if node is not None:
        # Visit right subtree
        if node.right:
            inorder_traversal(node.right, graph_lines)
            graph_lines.append(f'    "{node.Pair.key}" -> "{node.right.Pair.key}";')
        else:
            # If left child is missing, add it
            
            right_key = f"R{node.Pair.key}"
            node.right = Node(Pair(right_key, 0))
            graph_lines.append(f'    "{node.Pair.key}" -> "{right_key}";')
        # Visit left subtree
        if node.left:
            graph_lines.append(f'    "{node.Pair.key}" -> "{node.left.Pair.key}";')
            inorder_traversal(node.left, graph_lines)
        else:
            # If right child is missing, add it
            left_key = f"L{node.Pair.key}"
            node.left = Node(Pair(left_key, 0))
            graph_lines.append(f'    "{node.Pair.key}" -> "{left_key}";')


def generate_graphviz_code(new_req):
    # Start with the first requirement as the root
    root = Node(new_req[0])
    # Insert remaining requirements
    for pair in new_req[1:]:
        insert(root, pair)

    # Generate Graphviz code
    graph_lines = ['digraph BST {']
    graph_lines1=[]
    inorder_traversal(root, graph_lines)
    for str_val in graph_lines[1:len(graph_lines)+1]:
        graph_lines1.append(str_val)
    graph_lines1.reverse()
    graph_lines=graph_lines1
    graph_lines.insert(0,'digraph BST {')
    graph_lines.append('}')
    return '\n'.join(graph_lines)

# Example usage: 
#Note: change this with your requirements priority list
requirements = [6,8,10,9,3,5,4,7,2,1]
lenny=len(requirements)
new_req=[]
for i in range(1,lenny+1):
    # new_req.append(Pair(i,lenny-requirements.index(i)))
    new_req.append(Pair(i,requirements[i-1]))
graphviz_code = generate_graphviz_code(new_req)
print(graphviz_code)