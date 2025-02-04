from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class NodeBinaryTree:
    def __init__(self, root: Node):
        if root is None:
            raise ValueError()
        
        self.root = root
        self.size = 1

    def __len__(self):
        return self.size
    
    def set_root(self, val):
        new_root = Node(val)
        new_root.left = self.root.left
        new_root.right = self.root.right
        self.root = new_root
    
    def append_node(self, val):
        q = deque()
        q.append(self.root)

        while q:
            curr_node: Node = q.popleft()

            if not curr_node.left:
                curr_node.left = Node(val)
                self.size += 1
                return
            else:
                q.append(curr_node.left)

            if not curr_node.right:
                curr_node.right = Node(val)
                self.size += 1
                return
            else:
                q.append(curr_node.right)

    def delete_node(self, val):
        if self.root.val == val:
            raise ValueError()

        q = deque()
        q.append(self.root)

        while q:
            curr_node: Node = q.popleft()
            curr_node_val = curr_node.val

            if curr_node_val == val:
                if not curr_node.left and not curr_node.right:
                    deepest_node_val = self.delete_deepest_node()
                    if deepest_node_val == curr_node_val:
                        return
                    curr_node.val = deepest_node_val
                    return
                
                deepest_node_val = self.delete_deepest_node()
                curr_node.val = deepest_node_val
                return

            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)

        raise ValueError()
                
    def delete_deepest_node(self):
        q = deque()
        q.append((self.root, None))

        while q:
            curr_node, parents_node = q.popleft()
            curr_node: Node
            parents_node: Node

            if not curr_node.left and not curr_node.right:
                ret_val = curr_node.val
                if parents_node is None:
                    raise ValueError("deepest node is root node")
                if parents_node.right.val == ret_val:
                    parents_node.right = None
                else:
                    parents_node.left = None
                self.size -= 1
                return ret_val
            else:
                if curr_node.right:
                    q.append((curr_node.right, curr_node))
                if curr_node.left:
                    q.append((curr_node.left, curr_node))

    def preorder(self):
        self._preorder(self.root)

    def inorder(self):
        self._inorder(self.root)

    def postorder(self):
        self._postorder(self.root)

    def _preorder(self, node: Node):
        if node is None:
            return
        print(node.val, end=" ")
        self._preorder(node.left)
        self._preorder(node.right)

    def _inorder(self, node: Node):
        if node is None:
            return
        self._inorder(node.left)
        print(node.val, end=" ")
        self._inorder(node.right)

    def _postorder(self, node: Node):
        if node is None:
            return
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.val, end=" ")