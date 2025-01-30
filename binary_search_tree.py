class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)

    def _insert(self, current, key, value):
        if key < current.key:
            if current.left is None:
                current.left = Node(key, value)
            else:
                self._insert(current.left, key, value)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key, value)
            else:
                self._insert(current.right, key, value)
        else:
            raise ValueError("Las claves duplicadas no están permitidas.")

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return None
        if key == current.key:
            return current.value
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, current, key):
        if current is None:
            return current
        if key < current.key:
            current.left = self._delete(current.left, key)
        elif key > current.key:
            current.right = self._delete(current.right, key)
        else:
            if current.left is None:
                return current.right
            elif current.right is None:
                return current.left
            min_larger_node = self._get_min(current.right)
            current.key, current.value = min_larger_node.key, min_larger_node.value
            current.right = self._delete(current.right, min_larger_node.key)
        return current

    def _get_min(self, current):
        while current.left is not None:
            current = current.left
        return current
