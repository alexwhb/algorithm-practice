class Node(object):
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.right_child = right
        self.left_child = left
        self.balance_factor = 0

    def has_right_child(self):
        return self.right_child is not None

    def has_left_child(self):
        return self.left_child is not None

    def is_right_child(self):
        return self.parent is not None and self.parent.right_child == self

    def is_left_child(self):
        return self.parent is not None and self.parent.left_child == self

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.is_root()

    def has_any_children(self):
        return self.left_child is not None or self.right_child is not None

    def has_both_children(self):
        return self.has_right_child() and self.has_left_child()

    def get_only_child(self):
        # quick note:
        # assertions are supposed to be used in this context.
        # their purpose is to make my assumptions about the use of this api known to outsiders
        assert self.has_any_children() and not self.has_both_children()
        if self.right_child is not None:
            return self.right_child
        else:
            return self.left_child

    def __repr__(self):
        return "<Node key: {}>".format(self.key)
