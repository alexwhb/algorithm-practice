import unittest

from BST.Node import Node

class TestNode(unittest.TestCase):

    def test_node_is_left_child_is_false(self):
        node = Node(5, 2)
        self.assertFalse(node.is_leaf())

    def test_node_is_left_child(self):
        parent_node = Node(5, 2)
        lef_child = Node(5, 2, parent=parent_node)
        parent_node.left_child = lef_child

        self.assertTrue(lef_child.is_left_child())

    def test_left_child_is_not_right_child(self):
        parent_node = Node(5, 2)
        lef_child = Node(5, 2, parent=parent_node)
        parent_node.left_child = lef_child

        self.assertFalse(lef_child.is_right_child())

    def test_right_child_is_right_child(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child

        self.assertTrue(right_child.is_right_child())

    def test_has_children_when_has_no_children(self):
        parent_node = Node(5, 2)
        self.assertFalse(parent_node.has_any_children())

    def test_has_children_when_there_is_a_left_child(self):
        parent_node = Node(5, 2)
        lef_child = Node(5, 2, parent=parent_node)
        parent_node.left_child = lef_child

        self.assertTrue(parent_node.has_any_children())

    def test_has_left_child_when_no_children(self):
        parent_node = Node(5, 2)
        self.assertIsNotNone(parent_node.has_left_child())
        self.assertFalse(parent_node.has_left_child())


    def test_has_left_child_when_left_child_exists(self):
        parent_node = Node(5, 2)
        left_child = Node(5, 2, parent=parent_node)
        parent_node.left_child = left_child

        self.assertTrue(parent_node.has_left_child())

    def test_has_right_child_when_right_child_exists(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child

        self.assertTrue(parent_node.has_right_child())
        self.assertFalse(parent_node.has_left_child())

    def test_has_right_child_when_right_child_does_not_exist(self):
        parent_node = Node(5, 2)
        self.assertIsNotNone(parent_node.has_right_child())
        self.assertFalse(parent_node.has_right_child())

    def test_has_both_children_when_one_is_missing(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child

        self.assertFalse(parent_node.has_both_children())
        self.assertIsNotNone(parent_node.has_both_children())

    def test_has_both_children_when_both_exist(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        left_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child
        parent_node.left_child = left_child

        self.assertTrue(parent_node.has_both_children())

    def test_is_root_when_node_has_parent(self):
        parent_node = Node(5, 2)
        child = Node(5, 2, parent=parent_node)

        self.assertFalse(child.is_root())
        self.assertIsNotNone(child.is_root())

    def test_is_root_when_node_has_no_parent(self):
        parent_node = Node(5,2)
        self.assertTrue(parent_node.is_root())

    def test_is_leaf_when_parent_does_not_exist(self):
        parent_node = Node(5,2)
        self.assertFalse(parent_node.is_leaf())
        self.assertIsNotNone(parent_node.is_leaf())

    def test_is_leaf_when_node_is_a_leaf(self):
        parent_node = Node(5, 2)
        child = Node(5, 2, parent=parent_node)

        self.assertTrue(child.is_leaf())

    def test_should_raise_assertion_error_when_no_children_exist_and_get_property_child(self):
        node = Node(5, 2)
        with self.assertRaises(AssertionError):
            node.get_only_child()

    def test_should_raise_assertion_error_when_two_children_exist(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        left_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child
        parent_node.left_child = left_child

        with self.assertRaises(AssertionError):
            parent_node.get_only_child()

    def test_should_return_right_only_child(self):
        parent_node = Node(5, 2)
        right_child = Node(5, 2, parent=parent_node)
        parent_node.right_child = right_child
        self.assertEqual(parent_node.get_only_child(), parent_node.right_child)

    def test_should_return_left_only_child(self):
        parent_node = Node(5, 2)
        left_child = Node(5, 2, parent=parent_node)
        parent_node.left_child = left_child

        self.assertEqual(parent_node.get_only_child(), parent_node.left_child)