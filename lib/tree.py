class Tree:
    def __init__(self, root):
        self.root = root

    def get_element_by_id(self, target_id):
        # Use DFS with an explicit stack
        stack = [self.root]

        while stack:
            node = stack.pop()  # Get the last added node (LIFO)
            
            # Check if the current node has the target ID
            if node.get('id') == target_id:
                return node
            
            # Add children to the stack (reverse to maintain order)
            stack.extend(reversed(node.get('children', [])))
        
        return None  # Return None if not found
