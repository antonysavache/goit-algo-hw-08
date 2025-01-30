# Базова структура для двійкового дерева пошуку
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Завдання 1: Знаходження максимального значення
    def find_max(self):
        if not self.root:
            return None

        current = self.root
        while current.right:
            current = current.right
        return current.value

    # Завдання 2: Знаходження мінімального значення
    def find_min(self):
        if not self.root:
            return None

        current = self.root
        while current.left:
            current = current.left
        return current.value

    # Завдання 3: Знаходження суми всіх значень
    def sum_all(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if not node:
            return 0
        return node.value + self._sum_recursive(node.left) + self._sum_recursive(node.right)

# Завдання 4: Система коментарів
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання BST
def test_bst():
    bst = BinarySearchTree()
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        bst.insert(value)

    print("Максимальне значення:", bst.find_max())  # 8
    print("Мінімальне значення:", bst.find_min())   # 1
    print("Сума всіх значень:", bst.sum_all())      # 34

# Приклад використання системи коментарів
def test_comments():
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    print("\nСтруктура коментарів:")
    root_comment.display()

if __name__ == "__main__":
    test_bst()
    test_comments()