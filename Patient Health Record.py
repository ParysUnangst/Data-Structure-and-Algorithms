class Node:
    def __init__(self, value):
        # Initialize a Node with the given value and set the next reference to None
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        # Initialize the head of the linked list to None
        self.head = None

    def append(self, value):
        # Create a new node with the given value
        new_node = Node(value)
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
        # Traverse the list and print each node's value
        current_node = self.head
        while current_node:
            print(current_node.value, end=" -> ")
            current_node = current_node.next
        print("None")

def reverse_list(head):
    # Reverse the linked list and return the new head
    prev = None
    current = head
    while current:
        # Store the next node
        next_node = current.next
        # Reverse the link
        current.next = prev
        # Move prev and current one step forward
        prev = current
        current = next_node
    # Return the new head of the reversed list
    return prev

def isHealthRecordSymmetric(head):
    if not head or not head.next:
        # An empty list or a list with one element is symmetric
        return True

    # Find the middle of the list using slow and fast pointers
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse the second half of the list
    second_half = reverse_list(slow)

    # Compare the first half and the reversed second half
    first_half = head
    while second_half:
        if first_half.value != second_half.value:
            # If values are not the same, the list is not symmetric
            return False
        first_half = first_half.next
        second_half = second_half.next

    # If all values matched, the list is symmetric
    return True

# Test cases to validate the solution
def test_isHealthRecordSymmetric():
    # Test case 1: Even number of symmetric metrics
    sll1 = SinglyLinkedList()
    sll1.append(70)
    sll1.append(80)
    sll1.append(80)
    sll1.append(70)
    print("Test case 1:", isHealthRecordSymmetric(sll1.head))  # Expected output: True

    # Test case 2: Odd number of symmetric metrics
    sll2 = SinglyLinkedList()
    sll2.append(90)
    sll2.append(100)
    sll2.append(110)
    sll2.append(100)
    sll2.append(90)
    print("Test case 2:", isHealthRecordSymmetric(sll2.head))  # Expected output: True

    # Test case 3: Not symmetric
    sll3 = SinglyLinkedList()
    sll3.append(120)
    sll3.append(130)
    sll3.append(125)
    print("Test case 3:", isHealthRecordSymmetric(sll3.head))  # Expected output: False

# Run test cases
test_isHealthRecordSymmetric()
