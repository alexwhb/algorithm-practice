import unittest
from BST.BasicBst import BasicBst


class TestBasicBst(unittest.TestCase):
    def test_should_add_first_node_as_root(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        self.assertEqual(bst.root.value, 'this is cool')

    def test_should_have_size_of_three(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        bst[15] = 'another test'
        self.assertEqual(bst.size, 3)

    def test_should_put_smaller_keys_on_left(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        self.assertIsNotNone(bst.root.left_child)
        self.assertEqual(bst.root.left_child.key, 10)

    def test_should_put_bigger_keys_on_right(self):
        bst = BasicBst()
        bst[50] = 'this is cool'
        bst[55] = 'test'

        self.assertEqual(bst.root.right_child.key, 55)

    def test_should_get_node_by_key(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        bst[15] = 'another test'

        self.assertIsNotNone(bst.get(15))
        self.assertEqual(bst.get(15).value, 'another test')

    def test_contains_some_key_should_return_true(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        bst[15] = 'another test'

        self.assertTrue(15 in bst)

    def test_not_contains(self):
        bst = BasicBst()
        bst[55] = 'this is cool'
        bst[10] = 'test'
        bst[15] = 'another test'

        self.assertFalse(8 in bst)

    # def test_delete_removes_node(self):
    #     bst = BasicBst()
    #     bst[55] = 'this is cool'
    #     bst[10] = 'test'
    #     bst[15] = 'another test'

    def test_gets_successor_node(self):
        bst = BasicBst()
        bst[18] = 0
        bst[5] = 0
        bst[35] = 0
        bst[2] = 0
        bst[10] = 0
        bst[4] = 0
        bst[7] = 0
        bst[8] = 0

        self.assertEqual(bst.find_successor_node(bst.get(5)).key, 7)

    def test_delete_node_with_no_children_and_is_root(self):
        bst = BasicBst()
        bst[18] = 0
        bst.remove(bst[18])
        self.assertIsNone(bst.root)

    def test_delete_node_with_no_children_that_is_not_root(self):
        bst = BasicBst()
        bst[18] = 0
        bst[16] = 0
        bst[20] = 0

        bst.remove(bst[16])

        self.assertIsNone(bst.root.left_child)

    def test_delete_node_with_one_child(self):
        bst = BasicBst()
        bst[18] = 0
        bst[16] = 0
        bst[20] = 0
        bst[15] = 0

        bst.remove(bst[16])

        self.assertIsNone(bst[16])
        self.assertEqual(bst.root.left_child.key, 15)

    def test_delete_node_with_two_children(self):
        bst = BasicBst()
        bst[18] = 0
        bst[5] = 0
        bst[35] = 0
        bst[2] = 0
        bst[10] = 0
        bst[4] = 0
        bst[7] = 0
        bst[8] = 0

        bst.remove(bst[5])

        self.assertEqual(bst.root.left_child.key, 7)
        self.assertEqual(bst.root.left_child.left_child.key, 2)
        self.assertEqual(bst.root.left_child.right_child.key, 11)


        # three deletion possiblities
        # one no children
        # one child
        # two children
