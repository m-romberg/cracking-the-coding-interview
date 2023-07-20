class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def create_linked_list_with_duplicates():
    linked_list = LinkedList()
    values = [1, 2, 3, 4, 2]  # Ensure a duplicate value (2) is present
    for value in values:
        linked_list.append(value)
    return linked_list

def remove_dupes (linked_list):
    node = linked_list.head
    unique_values = set([node.value])
    while (node.next is not None):
        if node.next.value in unique_values:
            node.next = node.next.next
        else:
            unique_values.add(node.value)
            node = node.next
    return linked_list

if __name__ == "__main__":
    linked_list = create_linked_list_with_duplicates()
    print("Linked List with Duplicates:")
    print_linked_list(linked_list)
    no_duplicates = remove_dupes(linked_list=linked_list)
    print("Linked List with No Duplicates:")
    print_linked_list(no_duplicates)