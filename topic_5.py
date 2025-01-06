from collections import deque

class Order:
    def __init__(self, order_id, business_name, customer_name, delivery_address, status):
        self.order_id = order_id
        self.business_name = business_name
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.status = status 

    def __repr__(self):
        return f"Order({self.order_id}, {self.business_name}, {self.customer_name}, {self.status})"

class OrderQueue:
    def __init__(self, max_orders):
        self.max_orders = max_orders
        self.orders = deque()
    
    def add_order(self, order):
        if len(self.orders) < self.max_orders:
            self.orders.append(order)
            print(f"Order {order.order_id} added.")
        else:
            print(f"Order queue is full. Cannot add order {order.order_id}.")
    
    def process_order(self):
        if self.orders:
            order = self.orders.popleft()
            order.status = "Delivered"
            print(f"Order {order.order_id} has been delivered.")
        else:
            print("No orders to process.")
    
    def cancel_order(self, order_id):
        for order in self.orders:
            if order.order_id == order_id:
                self.orders.remove(order)
                print(f"Order {order_id} has been cancelled.")
                return
        print(f"Order {order_id} not found.")
    
    def view_orders(self):
        return list(self.orders) 


order_queue = OrderQueue(max_orders=5)


order1 = Order(order_id=1, business_name="UMUCYO RESTO", customer_name="DIANE", delivery_address="123 butare-madina", status="Pending")
order2 = Order(order_id=2, business_name="OBINA", customer_name="GRACE", delivery_address="456 butare-cyarwa", status="Pending")

order_queue.add_order(order1)
order_queue.add_order(order2)


print(order_queue.view_orders())

order_queue.process_order()


print(order_queue.view_orders())

order_queue.cancel_order(2)

print(order_queue.view_orders())
