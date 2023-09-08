class ListNode:
    def __init__(self, num=0, next=None):
        self.num = num
        self.next = next

def removeEndNth(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return dummy.next

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.num)
        current = current.next
    return lst

head1 = list_to_linkedlist([1])
n1 = 1
result1 = removeEndNth(head1, n1)
print("Output 1:", linkedlist_to_list(result1))

head2 = list_to_linkedlist([1, 2])
n2 = 1
result2 = removeEndNth(head2, n2)
print("Output 2:", linkedlist_to_list(result2))
