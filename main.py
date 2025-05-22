class HistogramNode:
    def __init__(self, key):
        self.key = key
        self.count = 1 # liczba węzłów w poddrzewie (na początku tylko ten węzeł)
        self.left = None
        self.right = None

class HistogramTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        inserted, self.root = self._insert_recursive(self.root, key)
        return inserted

    def _insert_recursive(self, node, key):
        # If the node is None, create a new node
        if node is None:
            return True, HistogramNode(key)

        # If the key already exists, do nothing
        # (each key appears only once in the tree)
        if node.key == key:
            return False, node

        # Insert into the left subtree
        if key < node.key:
            inserted, node.left = self._insert_recursive(node.left, key)
        # Insert into the right subtree
        else:  # key > node.key
            inserted, node.right = self._insert_recursive(node.right, key)

        # Update count (total nodes in this subtree)
        node.count = 1  # Count this node
        if node.left:
            node.count += node.left.count
        if node.right:
            node.count += node.right.count

        return inserted, node

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search_recursive(node.left, key)
        if key > node.key:
            return self._search_recursive(node.right, key)

    def count_in_range(self, start, end):
        return self.count_less_than(end+1) - self.count_less_than(start)

    def count_less_than(self, key):
        return self._count_less_than_recursive(self.root, key)

    def _count_less_than_recursive(self, node, key):
        if node is None:
            return 0
        if key > node.key:
            # If key is greater than current node, then current node and all nodes
            # in its left subtree are less than key
            left_count = node.left.count if node.left else 0
            return 1 + left_count + self._count_less_than_recursive(node.right, key)
        elif key <= node.key:
            # If key is less than or equal to current node, we only look in left subtree
            return self._count_less_than_recursive(node.left, key)

    def count_greater_than(self, key):
        return self._count_greater_than_recursive(self.root, key)

    def _count_greater_than_recursive(self, node, key):
        if node is None:
            return 0
        if key < node.key:
            # If key is less than current node, then current node and all nodes
            # in its right subtree are greater than key
            right_count = node.right.count if node.right else 0
            return 1 + right_count + self._count_greater_than_recursive(node.left, key)
        elif key >= node.key:
            # If key is greater than or equal to current node, we only look in right subtree
            return self._count_greater_than_recursive(node.right, key)

    def find_kth_smallest(self, k):
        """Znajduje k-ty najmniejszy element w drzewie. Złożoność: O(h)"""
        if k <= 0 or (self.root and k > self.root.count):
            return None  # Invalid k value

        return self._find_kth_smallest_recursive(self.root, k)

    def _find_kth_smallest_recursive(self, node, k):
        if node is None:
            return None

        # Count of nodes in left subtree
        left_count = node.left.count if node.left else 0

        if k == left_count + 1:
            # Current node is the k-th smallest
            return node.key
        elif k < left_count + 1:
            # k-th smallest is in the left subtree
            return self._find_kth_smallest_recursive(node.left, k)
        else:
            # k-th smallest is in the right subtree
            # Adjust k to account for nodes already counted
            return self._find_kth_smallest_recursive(node.right, k - left_count - 1)

    def inorder_traversal(self):
        """Returns in-order list as a string with extra spacing."""
        elements = []
        self._inorder_recursive(self.root, elements)
        return "[ " + ", ".join(map(str, elements)) + " ]"

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)

    def delete(self, key):
        """Usuwa element z drzewa. Złożoność: O(h)"""
        deleted, self.root = self._delete_recursive(self.root, key)
        return deleted

    def _delete_recursive(self, node, key):
        # Base case
        if node is None:
            return False, None

        # If key to be deleted is in a subtree
        if key < node.key:
            deleted, node.left = self._delete_recursive(node.left, key)
        elif key > node.key:
            deleted, node.right = self._delete_recursive(node.right, key)
        else:
            # If current node is the one to be deleted

            # Case 1: Node has 0 children or only right child
            # gdy ma 0 dzieci, to zwracamy node.right, ktory jest
            # nullem, i przypisujemy go do
            if node.left is None:
                return True, node.right

            # Case 2: Node has only left child
            if node.right is None:
                return True, node.left

            # Case 3: Node has both children
            # Find the inorder successor (smallest node in right subtree)
            successor = self._get_successor(node)
            node.key = successor.key
            # Delete the successor
            # nie bedzie miec lewego dziecka, wiec zadziala usuwanie
            # dla 1. przypadku
            deleted, node.right = self._delete_recursive(node.right, successor.key)

        # Update the count for this node
        # na kazdym updatujemy juz po usunieciu tuz przed zwroceniem samego
        # siebie, wiec dzieki rekurencji updatowanie po kolei bedzie
        # prawidlowe
        node.count = 1  # Count this node
        if node.left:
            node.count += node.left.count
        if node.right:
            node.count += node.right.count

        return deleted, node

    def _get_successor(self, node):
        """Helper method to find the minimum key node in a subtree"""
        current = node.right
        #wiemy, ze cos jest w prawym poddrzewie, wiec mozemy tak zrobic
        # Keep going left until we reach a leaf
        while current.left is not None:
            current = current.left
        return current


def main():
    tree = HistogramTree()

    while True:
        command = input().strip()
        parts = command.split()

        if parts[0] == "EXIT":
            break

        elif parts[0] == "INSERT":
            x = int(parts[1])
            if tree.insert(x):
                print(f"Added: {x}")
            else:
                print("Element already exists")

        elif parts[0] == "DELETE":
            x = int(parts[1])
            if tree.delete(x):
                print(f"Deleted: {x}")
            else:
                print("Element does not exist")

        elif parts[0] == "SEARCH":
            x = int(parts[1])
            result = tree.search(x)
            print("YES" if result else "NO")

        elif parts[0] == "COUNT_RANGE":
            x = int(parts[1])
            y = int(parts[2])
            result = tree.count_in_range(x, y)
            print(f"Elements in range [{x}, {y}]: {result}")

        elif parts[0] == "COUNT_LESS":
            x = int(parts[1])
            result = tree.count_less_than(x)
            print(f"Elements less than {x}: {result}")

        elif parts[0] == "COUNT_GREATER":
            x = int(parts[1])
            result = tree.count_greater_than(x)
            print(f"Elements greater than {x}: {result}")

        elif parts[0] == "FIND_KTH":
            k = int(parts[1])
            result = tree.find_kth_smallest(k)
            if result is None:
                print("Invalid index")
            else:
                print(result)

        elif parts[0] == "INORDER":
            print(tree.inorder_traversal())



if __name__ == "__main__":
    main()
