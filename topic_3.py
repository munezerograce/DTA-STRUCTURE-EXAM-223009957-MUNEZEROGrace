class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, root, key, value):
        if not root:
            return AVLNode(key, value)

        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            return root  

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.rotate_right(root)
        if balance < -1 and key > root.right.key:
            return self.rotate_left(root)
        if balance > 1 and key > root.left.key:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and key < root.right.key:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root

        if key < root.key:
            return self.search(root.left, key)
        return self.search(root.right, key)



class DeliveryHistory:
    def __init__(self):
        self.history = []

    def add_delivery(self, delivery):
        self.history.append(delivery)

    def get_deliveries(self):
        return self.history


class DeliveryNode:
    def __init__(self, order_id, order_details):
        self.order_id = order_id
        self.order_details = order_details
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_order(self, order_id, order_details):
        new_node = DeliveryNode(order_id, order_details)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def remove_order(self, order_id):
        current = self.head
        while current:
            if current.order_id == order_id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return True
            current = current.next
        return False

    def list_orders(self):
        orders = []
        current = self.head
        while current:
            orders.append((current.order_id, current.order_details))
            current = current.next
        return orders



if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None

  
    root = avl_tree.insert(root, 101, {"order": "Pizza", "customer": "Bahati"})
    root = avl_tree.insert(root, 103, {"order": "Burger", "customer": "olivier"})
    root = avl_tree.insert(root, 102, {"order": "udushaza dutogosheje", "customer": "grace"})

    
    order = avl_tree.search(root, 102)
    print("Order found:", order.value if order else "Not found")

    
    history = DeliveryHistory()
    history.add_delivery("Delivered Pizza to bahati")
    history.add_delivery("Delivered udushaza dutogosheje to grace")
    print("Delivery History:", history.get_deliveries())

    dll = DoublyLinkedList()
    dll.add_order(201, {"order": "agatoki", "customer": "Diana"})
    dll.add_order(202, {"order": "Sandwich", "customer": "murungi"})
    dll.add_order(203, {"order": "amata", "customer": "Frank"})
    print("Current Orders:")
    for order in dll.list_orders():
        print(order)

    dll.remove_order(202)
    print("Orders after removal:")
    for order in dll.list_orders():
        print(order)
