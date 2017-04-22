from BST.Node import Node


class BasicBst(object):
    def __init__(self):
        self.root = None
        self.size = 0

    def __delitem__(self, key):
        pass

    def __len__(self):
        return self.size

    def __contains__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __iter__(self):
        pass

    def __getitem__(self, key):
        return self.get(key)

    def put(self, key, value):
        self.size += 1
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._put(key, value, self.root)

    def _put(self, key, value, current_node: Node):
        if key < current_node.key:
            if current_node.has_left_child():
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = Node(key, value, parent=current_node)
        else:
            if current_node.has_right_child():
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = Node(key, value, parent=current_node)

    def get(self, key) -> Node:
        return self._get(key, self.root)

    def _get(self, key, current_node: Node) -> Node:
        if current_node is None:
            return None
        else:
            if key == current_node.key:
                return current_node

            elif key < current_node.key:
                return self._get(key, current_node.left_child)
            else:
                return self._get(key, current_node.right_child)

    def remove(self, node: Node):
        if not node.has_any_children():
            if node is self.root:
                self.root = None
            else:
                if node.is_left_child():
                    node.parent.left_child = None
                else:
                    node.parent.right_child = None
        else:
            # this node does have children. this is the more complex case
            if node.has_both_children():
                self.find_successor_node(node)


                pass
            else:
                if node.has_right_child():
                    node.parent.right_child = node.get_only_child()
                else:
                    node.parent.left_child = node.get_only_child()

    def find_successor_node(self, node: Node) -> Node:
        if node.has_any_children():
            if node.has_right_child():
                return self.find_min(node.right_child)
            else:
                return self.find_min(node.left_child)
        else:
            return Node

    def find_min(self, node: Node) -> Node:
        current_node = node
        while current_node.has_left_child():
            current_node = current_node.left_child
        return current_node


