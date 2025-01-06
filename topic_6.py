class Order:
    def __init__(self, order_id, customer_name, delivery_address, status="Pending"):
        self.order_id = order_id
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.status = status

    def __repr__(self):
        return f"Order({self.order_id}, {self.customer_name}, {self.status})"

class TreeNode:
    def __init__(self, name, data=None):
        self.name = name  
        self.data = data  
        self.children = []  

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode({self.name}, {self.data}, Children: {len(self.children)})"

class BusinessTree:
    def __init__(self, business_name):
        self.root = TreeNode(business_name) 
    
    def add_zone(self, business_name, zone_name):
      
        business_node = self._find_node(self.root, business_name)
        if business_node:
            zone_node = TreeNode(zone_name)  
            business_node.add_child(zone_node)  
            print(f"Delivery zone {zone_name} added under {business_name}.")
        else:
            print(f"Business {business_name} not found.")

    def add_order(self, business_name, zone_name, order):
      
        zone_node = self._find_node(self.root, zone_name, parent_name=business_name)
        if zone_node:
            zone_node.add_child(TreeNode(order.order_id, order)) 
            print(f"Order {order.order_id} added to zone {zone_name}.")
        else:
            print(f"Zone {zone_name} under business {business_name} not found.")
    
    def process_order(self, business_name, zone_name, order_id):
       
        zone_node = self._find_node(self.root, zone_name, parent_name=business_name)
        if zone_node:
            for child in zone_node.children:
                if isinstance(child.data, Order) and child.data.order_id == order_id:
                    child.data.status = "Delivered"
                    print(f"Order {order_id} processed and delivered.")
                    return
            print(f"Order {order_id} not found in zone {zone_name}.")
        else:
            print(f"Zone {zone_name} under business {business_name} not found.")

    def _find_node(self, start_node, node_name, parent_name=None):
      
        if start_node.name == node_name and (parent_name is None or start_node.name == parent_name):
            return start_node
        for child in start_node.children:
            result = self._find_node(child, node_name, parent_name)
            if result:
                return result
        return None

    def view_hierarchy(self):
        
        self._print_tree(self.root, level=0)

    def _print_tree(self, node, level):
        print("  " * level + f"{node.name} ({len(node.children)} children)")
        for child in node.children:
            self._print_tree(child, level + 1)


business_tree = BusinessTree("UMUCYO RESTO")


business_tree.add_zone("UMUCYO RESTO", "MADINA")
business_tree.add_zone("OBINA RESTO", "ITUMBA")


order1 = Order(order_id=1, customer_name="GRACE", delivery_address="123 butare-mukoni")
order2 = Order(order_id=2, customer_name="DIANE", delivery_address="456 butare-madina")
business_tree.add_order("UMUCYO RESTO", "MADINA", order1)
business_tree.add_order("OBINA RESTO", "ITUMBA", order2)

business_tree.view_hierarchy()


business_tree.process_order("UMUCYO RESTO", "MADINA", 1)

business_tree.view_hierarchy()
