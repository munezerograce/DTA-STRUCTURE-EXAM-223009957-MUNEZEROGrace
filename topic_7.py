class Order:
    def __init__(self, order_id, customer_name, delivery_address, priority, status="Pending"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.priority = priority 
        self.status = status

    def __repr__(self):
        return f"Order({self.order_id}, {self.customer_name}, Priority: {self.priority}, Status: {self.status})"


def bubble_sort(orders):
  
    n = len(orders)
    for i in range(n):
       
        for j in range(0, n-i-1):
            if orders[j].priority > orders[j+1].priority:
               
                orders[j], orders[j+1] = orders[j+1], orders[j]
    return orders



order1 = Order(order_id=1, customer_name="DIANE", delivery_address="123 butare St", priority=2)
order2 = Order(order_id=2, customer_name="BAHATI", delivery_address="456 tumba St", priority=1)
order3 = Order(order_id=3, customer_name="BARAKA", delivery_address="789 mukoni St", priority=3)
order4 = Order(order_id=4, customer_name="MUSEMAKWELI", delivery_address="101 cyarwa St", priority=1)


orders = [order1, order2, order3, order4]

print("Before sorting:")
for order in orders:
    print(order)

sorted_orders = bubble_sort(orders)


print("\nAfter sorting by priority:")
for order in sorted_orders:
    print(order)
