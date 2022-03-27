class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def convert(l1, l2):
    val1 = l1.val
    val2 = l2.val
    sum1 = val1 + val2
    shift_number, part2 = divmod(sum1, 10)
    node = ListNode(part2)
    next1 = l1.next
    next2 = l2.next
    current_node = node

    while next1 is not None or next2 is not None or shift_number:
        val1 = next1.val if next1 else 0
        val2 = next2.val if next2 else 0
        sum1 = val1 + val2 + shift_number

        shift_number, part2 = divmod(sum1, 10)
        new_node = ListNode(part2)
        current_node.next = new_node
        current_node = new_node

        if next1:
            next1 = next1.next
        if next2:
            next2 = next2.next

    return node

# assert convert(ListNode(2, ListNode(4, ListNode(3))),
#                ListNode(5, ListNode(6, ListNode(4)))) == ListNode(7, ListNode(0, ListNode(8)))
# assert convert(ListNode(0), ListNode(0)) == ListNode(0)

# assert convert(ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9))))))),
#                ListNode(9, ListNode(9, ListNode(9, ListNode(9))))) == ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))
