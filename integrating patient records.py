class Node:
    def __init__(self, ssn, age, full_name):
        self.ssn = ssn
        self.age = age
        self.full_name = full_name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, ssn, age, full_name):
        new_node = Node(ssn, age, full_name)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(f"SSN: {current.ssn}, Age: {current.age}, Name: {current.full_name}")
            current = current.next

def merge_sorted_lists(head1, head2):
    dummy = Node(0, 0, "")
    tail = dummy

    while head1 and head2:
        if head1.ssn <= head2.ssn:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    elif head2:
        tail.next = head2

    return dummy.next

# Example usage:

# Creating the first linked list for HealthMerge Inc.
ll1 = LinkedList()
ll1.append("123-45-6789", 30, "John Doe")
ll1.append("123-45-6790", 25, "Jane Smith")
ll1.append("123-45-6791", 40, "Alice Johnson")

# Creating the second linked list for CarePlus
ll2 = LinkedList()
ll2.append("123-45-6788", 35, "Robert Brown")
ll2.append("123-45-6789", 30, "John Doe")
ll2.append("123-45-6792", 50, "Emily Davis")

print("List 1:")
ll1.print_list()
print("\nList 2:")
ll2.print_list()

# Merging the linked lists
merged_head = merge_sorted_lists(ll1.head, ll2.head)

# Printing the merged list
merged_list = LinkedList()
merged_list.head = merged_head

print("\nMerged List:")
merged_list.print_list()
