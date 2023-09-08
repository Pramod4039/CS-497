import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKSortedLists(lists):
    min_heap = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst.val, i))
            lists[i] = lst.next

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, i = heapq.heappop(min_heap)
        current.next = ListNode(val)
        current = current.next

        if lists[i]:
            heapq.heappush(min_heap, (lists[i].val, i))
            lists[i] = lists[i].next

    return dummy.next

def listsToLinkedLists(lists):
    linkedLists = []
    for lst in lists:
        linkedLists.append(listToLinkedList(lst))
    return linkedLists

def listToLinkedList(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedListToList(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

lists1 = [[1, 4, 5], [1, 3, 4], [2, 6]]
linkedLists1 = listsToLinkedLists(lists1)
result1 = mergeKSortedLists(linkedLists1)
print("Output 1:", linkedListToList(result1))

lists2 = []
linkedLists2 = listsToLinkedLists(lists2)
result2 = mergeKSortedLists(linkedLists2)
print("Output 2:", linkedListToList(result2))

lists3 = [[]]
linkedLists3 = listsToLinkedLists(lists3)
result3 = mergeKSortedLists(linkedLists3)
print("Output 3:", linkedListToList(result3))