import sys

class ListNode:
    def __init__(self , val= 0, next= None):
        self.val = val 
        self.next = next
        
def build_ll(arr):
    
    head = ListNode(arr[0])
    dummy = head
    for i in range(1, len(arr)):
        curr = ListNode(arr[i])
        dummy.next = curr
        dummy = dummy.next
    return head
        
def print_linked_list(head):
    while head:
        print(head.val , end=" ")
        head = head.next 
        print("------>" , end=" ")
    print()

if __name__ == "__main__":
    # 3 20 30 40 
    tokens = iter(sys.stdin.read().split())
    n = int(next(tokens))
    arr = [int(next(tokens)) for _ in range(n)]
    
    head = build_ll(arr)
    print_linked_list(head)
    