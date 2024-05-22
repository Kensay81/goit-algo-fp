class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" -> ")
            curr = curr.next
        print("None")

def reverse_linked_list(linked_list):
    prev = None
    current = linked_list.head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    linked_list.head = prev

def merge_sort_linked_list(head):
    if not head or not head.next:
        return head

    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    left = merge_sort_linked_list(head)
    right = merge_sort_linked_list(next_to_middle)

    sorted_list = sorted_merge(left, right)
    return sorted_list

def get_middle(head):
    if not head:
        return head

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def sorted_merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left.data <= right.data:
        result = left
        result.next = sorted_merge(left.next, right)
    else:
        result = right
        result.next = sorted_merge(left, right.next)
    
    return result

def merge_sorted_linked_lists(list1, list2):
    dummy = Node(0)
    tail = dummy

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:
        if l1.data <= l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

# Приклад використання

# Створення та заповнення першого однозв'язного списку
list1 = LinkedList()
for i in [10, 3, 5, 1, 7]:
    list1.append(i)

print("Початковий список 1:")
list1.print_list()

# Реверсування першого списку
reverse_linked_list(list1)
print("Список 1 після реверсування:")
list1.print_list()

# Сортування першого списку
list1.head = merge_sort_linked_list(list1.head)
print("Відсортований список 1:")
list1.print_list()

# Створення та заповнення другого однозв'язного списку
list2 = LinkedList()
for i in [8, 6, 2, 9, 4]:
    list2.append(i)

print("Початковий список 2:")
list2.print_list()

# Сортування другого списку
list2.head = merge_sort_linked_list(list2.head)
print("Відсортований список 2:")
list2.print_list()

# Об'єднання двох відсортованих списків
merged_list = merge_sorted_linked_lists(list1, list2)
print("Об'єднаний відсортований список:")
merged_list.print_list()
