from node_linkedlist import LinkedList
def print_linked_list(linked_list):
    """Given a linked list, it will print the value"""
    current = linked_list.head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

def create_linked_list_with_duplicates():
    """Initialie linkedlist with two values that are duplicates"""
    linked_list = LinkedList()
    values = [1, 2, 3, 4, 2]  # Ensure a duplicate value (2) is present
    for value in values:
        linked_list.append(value)
    return linked_list

def remove_dupes (linked_list):
    """Given a LinkedList, it will remove any nodee that has a value
    of a previous node (a duplicate) and return a linkedlist"""
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