class Node(object):
    def __init__(self):
        self.val = None
        self.next = None



def create_list(array_list):
    head = None
    current = None
    for i in array_list:
        
        if head is None:
            current = Node()
            head = current
        else:
            current.next = Node()
            current = current.next
        current.val = i
    return head


def print_list(current):
    while current is not None:
        print(current.val)
        current = current.next

def reverse_list(head):
    if head is None or head.next is None:
        return head
    new_head = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return new_head
   
def reverse_list_2(head):
    pre = None
    cur = head
    nex = head
    while cur is not None:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverse_interval(head, tail):
    pre = None
    cur = head
    nex = head
    while pre is not tail:
        next = cur.next
        cur.next = pre
        pre = cur
        cur = next
    return pre

def reverse_N_group_list(head, n):
    if head is None:
        return head
    tail = head
    count = n
    while count > 1:
        tail = tail.next
        if tail is None:
            return head
        count -= 1
    
    new_head = reverse_N_group_list(tail.next, n)
    reverse_interval(head, tail)
    head.next = new_head
    return tail
    

if __name__ == "__main__":
    head = create_list([1,2,3,4,5,6])
    #tail = head.next.next.next
    #pre = reverse_interval(head, tail)
    #print_list(pre)
    # new_head = reverse_list(head)
    # new_head = reverse_list_2(head)
    #print_list(new_head)
    new_head = reverse_N_group_list(head, 2)
    print_list(new_head)
    




