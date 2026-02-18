def revll(head):
    curr = head
    prev = None

    while curr:
        newnode = curr.next
        curr.next = prev
        prev = curr
        curr = newnode

    return prev