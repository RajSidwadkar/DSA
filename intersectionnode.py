class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA: ListNode, headB: ListNode) :

    t1, t2 = headA, headB

    while t1 != t2:
        # If t1 reaches the end, switch to headB; else move to next
        t1 = t1.next if t1 else headB
        
        # If t2 reaches the end, switch to headA; else move to next
        t2 = t2.next if t2 else headA
           
    # If they don't intersect, both will eventually be None at the same time.
    return t1

# Time Complexity: O(N + M), where N and M are the lengths of the two linked lists.
# Space Complexity: O(1) since we are using only constant extra space.


intersect = ListNode(8)
intersect.next = ListNode(4)
intersect.next.next = ListNode(5)

# 2. Create List A: 4 -> 1 -> [shared]
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = intersect

# 3. Create List B: 5 -> 6 -> 1 -> [shared]
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = intersect

# Run the solution
result = getIntersectionNode(headA, headB) 

if result:
    print(f"Intersected at node with value: {result.val}")
else:
    print("No intersection found.")