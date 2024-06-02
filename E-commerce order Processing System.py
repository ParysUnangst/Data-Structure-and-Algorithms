class Order:
    def __init__(self, order_id, customer_details, order_details):
        # Initialize an Order with id, customer details, and order details
        self.order_id = order_id
        self.customer_details = customer_details
        self.order_details = order_details
    
    def __repr__(self):
        # Provide a string representation of the Order for easy display
        return f"Order(ID: {self.order_id}, Customer: {self.customer_details}, Details: {self.order_details})"

class Node:
    def __init__(self, order):
        # Initialize a Node with an Order and set the next reference to None
        self.order = order
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # Initialize the head of the linked list to None
        self.head = None

    def append(self, order):
        # Create a new node with the given order
        new_node = Node(order)
        if not self.head:
            # If the list is empty, set the new node as the head
            self.head = new_node
            return
        # Otherwise, traverse to the end of the list and append the new node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        # Traverse the list and print each order
        current_node = self.head
        while current_node:
            print(current_node.order)
            current_node = current_node.next

    def reverse(self):
        # Reverse the linked list
        prev_node = None
        current_node = self.head
        while current_node:
            # Store the next node
            next_node = current_node.next
            # Reverse the link
            current_node.next = prev_node
            # Move prev_node and current_node one step forward
            prev_node = current_node
            current_node = next_node
        # Set the new head of the list
        self.head = prev_node

if __name__ == "__main__":
    # Create some orders with sample data
    order1 = Order(1, "Customer A", "Item 1, Item 2")
    order2 = Order(2, "Customer B", "Item 3, Item 4")
    order3 = Order(3, "Customer C", "Item 5, Item 6")

    # Initialize the singly linked list
    orders_list = SinglyLinkedList()

    # Append orders to the list
    orders_list.append(order1)
    orders_list.append(order2)
    orders_list.append(order3)

    # Display the orders in the order they were added
    print("Orders in the order they were added:")
    orders_list.display()

    # Reverse the linked list
    orders_list.reverse()

    # Display the orders after reversing
    print("\nOrders after reversing:")
    orders_list.display()
